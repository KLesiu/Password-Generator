import sys
import random
import string




password = []
characters_left = -1
def update_characters_left(characters_entered):
    global characters_left
    if characters_entered > characters_left or characters_entered < 0:
        print("Error. Number of entered characters are bigger than number of available characters or enetered number is lower than 0. Available characters: ",characters_left)
        sys.exit(0)
    else:
        characters_left -= characters_entered
        print("Characters left: ",characters_left)



def is_a_number(num):
    
    try:
        int(num)
    except ValueError:
        print(num,"Is not a natural number")
        sys.exit(0)
    else: return True




password_length = input("How long password do you want? ")

if is_a_number(password_length) is True:
    password_length = int(password_length)


if password_length < 5:
    print("Password must be longer than 5 characters! ")
    sys.exit(0)
else:
    characters_left = password_length


lowercase_letters = input("How many lowercase letters do you want in your password? ")
if is_a_number(lowercase_letters) is True:
    lowercase_letters = int(lowercase_letters)
update_characters_left(lowercase_letters)

uppercase_letters = input("How many uppercase letters do you want in your password? ")
if is_a_number(uppercase_letters) is True:
    uppercase_letters = int(uppercase_letters)

update_characters_left(uppercase_letters)


special_characters = input("How many special characters do you want in your password? ")
if is_a_number(special_characters) is True:
    special_characters = int(special_characters)
update_characters_left(special_characters)
digits = input("How many digits do you want in your password? ")
if is_a_number(digits) is True:
    digits= int(digits)
update_characters_left(digits)


if characters_left > 0:
    print("You didnt use all characters. Application will add to your password lowercase letters insted of characters available. ")
    lowercase_letters += characters_left



print()
print("Password length: ", password_length)
print("Lowercase letters: ", lowercase_letters)
print("Uppercase letters: ", uppercase_letters)
print("Special characters: ",special_characters)
print("Digits: ", digits)

for _ in range(password_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1


random.shuffle(password)
print("Generated password:", "".join(password))
