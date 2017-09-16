import random


def generate_random_digit():
    digit = random.randint(0, 9)
    return digit


def generate_random_passphrase(number_of_digits, passphrase=""):
    already_exists = True
    while already_exists:
        for _ in range(number_of_digits):
            while True:
                generated_digit = generate_random_digit()
                if generated_digit not in passphrase:
                    passphrase += generated_digit
                    break
        already_exists = compare_against_database(passphrase)


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
    while True:
        user_response = input("\nEnter your choice : ")
        try:
            user_response = int(user_response)
            if 0 < user_response <= len(digit_for_category):
                break
            else:
                print(f"\nInvalid choice ! Try again")
        except ValueError:
            print("\nNon numeral input received ! Try again")
    return user_response


def main():
    digit_for_category = [
        "FINANCE"         : 1,
        "MAIL"            : 2,
        "UTILITIES"       : 3,
        "MISC IMPORTANT"  : 4,
        "MISC UNIMPORTANT": 5,
    ]



if __name__ == "__main__":
    main()
