import random
import tkinter

def generate_random_digit():
    digit = random.randint(0, 9)
    return digit


def generate_random_passphrase(passphrase="", number_of_digits=5):
    for _ in range(number_of_digits):
        while True:
            generated_digit = str(generate_random_digit())
            if generated_digit not in passphrase:
                passphrase += generated_digit
                break
    return passphrase


def compare_against_database(passphrase):
    return 0


def get_category_from_user():
    print(" Passphrase Generation Script")
    print("------------------------------")
    print("Categories")
    print("1. Finance")
    print("2. Mail")
    print("3. Utilities")
    print("4. Misc Important")
    print("5. Misc Un-important")
    maximum_number_of_choices = 5
    while True:
        user_response = input("\nEnter your choice : ")
        try:
            user_response = int(user_response)
            if 0 < user_response <= maximum_number_of_choices:
                break
            else:
                print(f"\nInvalid choice ! Try again")
        except ValueError:
            print("\nNon numeral input received ! Try again")
    return user_response


def load_database():
    database = dict()
    with open("./existing_passphrase.txt", 'r') as db:
        passphrase = db.readline().rstrip().lstrip()
        database[passphrase] = True
    return database


def append_to_database(passphrase):
    with open("./existing_passphrase.txt", 'a') as db:
        db.write(f"{passphrase}\n")


def main():
    starting_passphrase = str(get_category_from_user())
    database = load_database()
    while True:
        generated_passphrase = generate_random_passphrase(passphrase=starting_passphrase)
        if generated_passphrase not in database:
            break
    append_to_database(generated_passphrase)
    print(f"Generated passphrase is - {generated_passphrase}")


if __name__ == "__main__":
    main()
