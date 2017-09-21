import random
import tkinter
from tkinter import messagebox


class PassKeyGenerator:
    tk_root = tkinter.Tk()
    tk_dropdown_value = tkinter.StringVar(tk_root)
    tk_generated_key = tkinter.StringVar(tk_root)
    categories = ["Finance", "Mail", "Utilities", "Misc Important", "Misc Unimportant"]
    default_category = "Misc Unimportant"
    user_category_choice = ""
    generated_passkey = ""
    last_passkey_written = False
    database_loaded = False
    not_in_database = True
    number_of_digits = 5
    database = dict()

    def generate_random_digit(self):
        digit = random.randint(0, 9)
        return digit

    def generate_random_passkey(self):
        self.set_category()
        if not self.database:
            self.load_database_from_file()
            self.database_loaded = True
        while True:
            self.generated_passkey = str(self.user_category_choice)
            for _ in range(self.number_of_digits):
                while True:
                    generated_digit = str(self.generate_random_digit())
                    if generated_digit not in self.generated_passkey:
                        self.generated_passkey += generated_digit
                        break
            if self.generated_passkey not in self.database:
                break
        self.last_passkey_written = False
        self.tk_generated_key.set(self.generated_passkey)

    def set_category(self):
        self.user_category_choice = str(self.categories.index(self.tk_dropdown_value.get()) + 1)

    def load_database_from_file(self):
        with open("./existing_passphrase.txt", 'r') as db:
            read_passkey = db.readline().rstrip().lstrip()
            self.database[read_passkey] = True

    def add_passkey_to_database(self):
        if self.generated_passkey == "":
            tkinter.messagebox.showerror("Save to file", "Passkey cannot be an empty string")
            return
        with open("./existing_passphrase.txt", 'a') as db:
            db.write(f"{self.generated_passkey}\n")
        self.database[self.generated_passkey] = True
        tkinter.messagebox.showinfo("Save to file", "Key has been saved to database")
        self.last_passkey_written = True

    def exit_handler(self):
        if self.last_passkey_written == False and self.generated_passkey != "":
            if tkinter.messagebox.askquestion("Save to database",
                                              "Passkey has not been written to database\nDo you wish to save before exit?"):
                self.add_passkey_to_database()
                self.tk_root.destroy()
        elif tkinter.messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.tk_root.destroy()

    def start_gui(self):
        self.tk_root.title("Pass-Key Generator")
        main_window_frame = tkinter.Frame(self.tk_root)
        main_window_frame.grid()
        label_for_choice = tkinter.Label(text="Step 1. Select your choice",
                                         padx=10,
                                         pady=10,
                                         font=("Helvetica", 10))
        label_for_choice.grid(row=0,
                              column=0,
                              sticky="E")
        # ------------- Dropdown menu related declarations -------------------
        self.tk_dropdown_value.set(self.default_category)
        choice_dropdown = tkinter.OptionMenu(self.tk_root,
                                             self.tk_dropdown_value,
                                             *self.categories)
        choice_dropdown.grid(row=0,
                             column=1,
                             padx=10,
                             pady=10,
                             sticky="W")
        label_for_generate = tkinter.Label(text="Step 2. Generate random Key",
                                           padx=10,
                                           pady=10,
                                           font=("Helvetica", 10))
        label_for_generate.grid(row=1,
                                column=0,
                                sticky="E")
        # -------- Button for generating the key based on category in the drop down menu -----------
        generate_key_button = tkinter.Button(self.tk_root,
                                             text="Generate New Key",
                                             activebackground="GRAY",
                                             activeforeground="GHOST WHITE",
                                             padx=5,
                                             pady=5,
                                             command=self.generate_random_passkey,
                                             font=("Helvetica", 10))
        generate_key_button.grid(row=1,
                                 column=1,
                                 padx=10,
                                 pady=10,
                                 sticky="W")
        # ------------ Label for generated key -----------------
        label_for_tk_generated_key_text = tkinter.Label(self.tk_root,
                                                        text="Generated key is - ",
                                                        font=("Helvetica", 10))
        label_for_tk_generated_key_text.grid(row=2,
                                             column=0,
                                             padx=15,
                                             pady=15,
                                             sticky="E")
        label_for_tk_generated_key = tkinter.Label(self.tk_root,
                                                   textvariable=self.tk_generated_key,
                                                   font=("Helvetica", 14))
        label_for_tk_generated_key.grid(row=2,
                                        column=1,
                                        padx=15,
                                        pady=15,
                                        sticky="W")
        label_for_save = tkinter.Label(text="Step 3. Save Key to File",
                                       padx=10,
                                       pady=10,
                                       font=("Helvetica", 10))
        label_for_save.grid(row=3,
                            column=0,
                            sticky="E")
        # ---------------- Button for saving the key to the file ---------------------------
        save_tk_generated_key_button = tkinter.Button(self.tk_root,
                                                      text="Save Key to File",
                                                      activebackground="GRAY",
                                                      activeforeground="GHOST WHITE",
                                                      padx=5,
                                                      pady=5,
                                                      command=self.add_passkey_to_database,
                                                      font=("Helvetica", 10))
        save_tk_generated_key_button.grid(row=3,
                                          column=1,
                                          padx=10,
                                          pady=10,
                                          sticky="W")
        self.tk_root.protocol("WM_DELETE_WINDOW", self.exit_handler)
        self.tk_root.mainloop()


if __name__ == "__main__":
    passKeyObj = PassKeyGenerator()
    passKeyObj.start_gui()
