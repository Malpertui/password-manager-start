from tkinter import *
from random import choice
from tkinter import messagebox
import pyperclip
import json

special_characters = ['!', '#', '$', '%', '&', '(', ')', '*',
                      '+', ',', '-', '.', '/', ':', ';', '<', '=',
                      '>', '?', '@', '[', ']', '^', '_', '{', '|',
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
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)
    pyperclip.copy(password)

def write_into_file():
    email = email_entry.get()
    password = password_entry.get()
    website = website_entry.get()
    new_data = {website:
                {'email': email,
                'password': password,}
                }

    if len(email) < 1 or len(password) < 1 or len(website) < 1:
        messagebox.showinfo(title='OOOooops!', message='It appears you leave'
                                                       ' some of the fields empty.\n'
                                                       'Please fill in all fields')

    # ---------------------------- My version ------------------------------- #
    else:
        # messagebox.showinfo(title='Title', message='Message')
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: '
                                                      f'\nEmail: {email}\nPassword: {password}. '
                                                      f'Is it ok to save?')
        if is_ok:

            # with open(f'data.json', 'w') as file:
            #     json.dump(new_data, file, indent = 4)

            # with open('data.json', 'r') as file:
            #     data = json.load(file)
            #     print(data)
            try:
                with open('data.json', 'r') as file:
                    data = json.load(file)
                    data.update(new_data)

                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=4)
            except FileNotFoundError:
                with open('data.json', 'w') as file:
                    json.dump(new_data, file, indent=4)

    # I did not use finally and else blocks, and I added update and write into try block
    # Also I used these lines:
    #         email_entry.delete(0, 'end')
    #         email_entry.insert(0, "malpertui@gmail.com")

            password_entry.delete(0, 'end')
            website_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            email_entry.insert(0, "malpertui@gmail.com")

    # ---------------------------- End of my version ------------------------------- #

    # ---------------------------- Angela's version ------------------------------- #
    # else:
    #     try:
    #         with open('data.json', 'r') as file:
    #             data = json.load(file)
    #
    #     except FileNotFoundError:
    #         with open('data.json', 'w') as file:
    #             json.dump(new_data, file, indent=4)
    #     else:
    #         data.update(new_data)
    #
    #         with open('data.json', 'w') as file:
    #             json.dump(data, file, indent=4)
    #
    #     finally:
    #         password_entry.delete(0, 'end')
    #         website_entry.delete(0, 'end')

    # ---------------------------- End of Angela's version ------------------------------- #



window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.config(bg='white')

canvas = Canvas(width=200, height=200, highlightthickness=0, bg='white')
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg='white', font=("Arial", 14))
website_label.grid(column=0, row=1)
website_label.config(padx=10, pady=10)

website_entry = Entry(width=48, bd=2)
website_entry.grid(column=1, row=1, columnspan=2, sticky='e')
website_entry.focus()

email_label = Label(text="Email/Username:", bg='white', font=("Arial", 14))
email_label.grid(column=0, row=2)
email_label.config(padx=10, pady=10)

email_entry = Entry(width=48, bd=2)
email_entry.grid(column=1, row=2, columnspan=2, sticky='e')
email_entry.insert(0, "malpertui@gmail.com")

password_label = Label(text="Password:", bg='white', font=("Arial", 14))
password_label.grid(column=0, row=3)
password_label.config(padx=10, pady=10)

password_entry = Entry(width=27, bd=2)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_empty_label = Label(text="", bg='white', font=("Arial", 14))
add_empty_label.grid(column=0, row=4)
add_empty_label.config(padx=10, pady=10)

add_button = Button(text="Add", width=41, command=write_into_file)
add_button.grid(column=1, row=4, columnspan=2, sticky='e')

window.mainloop()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #