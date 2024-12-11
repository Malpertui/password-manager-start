from random import choice, shuffle

special_characters = ['!', '#', '$', '%', '&', '(', ')', '*',
                      '+', ',', '-', '.', '/', ':', ';', '<', '=',
                      '>', '?', '@', '[', ']', '^', '_`', '{', '|',
                      '}', '~']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z']

def generate_password():
    password_len = 9
    password=''
    for _ in range(password_len):
        what_symbol = choice([1, 2, 3])
        if what_symbol == 1:
            upper_or_lower = choice([1, 2])
            if upper_or_lower == 1:
                password += choice(letters)
            else:
                password += choice(letters).lower()
        elif what_symbol == 2:
            password += str(choice(numbers))
        else:
            password += choice(special_characters)
    print(password)
    print(len(password))
    shuffle(password)
    print(password)
    print(len(password))

generate_password()
