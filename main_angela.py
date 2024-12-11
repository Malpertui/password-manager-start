from tkinter import *
import random
import pyperclip

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    print(type(nr_letters))
    print(type(nr_symbols))
    print(type(nr_numbers))
    print(nr_letters)
    # password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_list = [random.choice(letters) for char in range(nr_letters)]
    print(password_list)

    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    random.shuffle(password_list)


    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    # password = ""
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    with open("data_angela.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)





# ---------------------------- UI SETUP ------------------------------- #
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

website_entry = Entry(width=45)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:", bg='white', font=("Arial", 14))
email_label.grid(column=0, row=2)
email_label.config(padx=10, pady=10)

email_entry = Entry(width=45)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "malpertui@gmail.com")

password_label = Label(text="Password:", bg='white', font=("Arial", 14))
password_label.grid(column=0, row=3)
password_label.config(padx=10, pady=10)

password_entry = Entry(width=27)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_empty_label = Label(text="", bg='white', font=("Arial", 14))
add_empty_label.grid(column=0, row=4)
add_empty_label.config(padx=10, pady=10)

add_button = Button(text="Add", width=41, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky='e')

window.mainloop()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


