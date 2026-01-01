#collect user preferences for a password
# - length
# - should contain at least one special character
# - should contain at least one upper case
# - should contain at least one digit

# get all available characters
# randomly pick characters up to the length
# ensure we have at least one of these character types
#ensure length is valid


import random
import string

def generate_password():
    length = int(input("Enter the length of the password: ").strip())
    if length < 4:
        print("Password must be at least 4 characters long")
        return
    include_special_character = input("Do you want a special character in your password (yes/no)?: ").strip().lower()
    if include_special_character != "yes" and include_special_character != "no":
        print("You need to enter either 'yes' or 'no'")
        return
    include_upper_case = input("Do you want an upper case in your password (yes/no)?: ").strip().lower()
    if include_upper_case != "yes" and include_upper_case != "no":
        print("You need to enter either 'yes' or 'no'")
        return
    include_lower_case = input("Do you want an lower case in your password (yes/no)?: ").strip().lower()
    if include_lower_case != "yes" and include_lower_case != "no":
        print("You need to enter either 'yes' or 'no'")
        return
    include_digits = input("Do you want an lower case in your password (yes/no)?: ").strip().lower()
    if include_digits != "yes" and include_digits != "no":
        print("You need to enter either 'yes' or 'no'")
        return

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_upper_case == "yes" else ""
    special = string.punctuation if include_special_character == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""

    all_characters = lower+upper+special+digits
    required_characters = []

    if include_upper_case == 'yes':
        required_characters.append(random.choice(upper))
    if include_lower_case == 'yes':
        required_characters.append(random.choice(lower))
    if include_special_character == 'yes':
        required_characters.append(random.choice(special))
    if include_digits == 'yes':
        required_characters.append(random.choice(digits))

    remaining_length =    length - len(required_characters)
    password = required_characters

    for _ in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)

    random.shuffle(password)
    return "".join(password)


random_password=generate_password()
print("Your random password is:", random_password)