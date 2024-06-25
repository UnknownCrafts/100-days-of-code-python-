# Python password manager using tkinter, shifting to using json instead of txt files for saving data

from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letter_list = string.ascii_letters + string.digits + '!@#$%^&*()_'

    password_length = random.randint(10, 15)
    password = [random.choice(letter_list) for char in range(password_length + 1)]

    random.shuffle(password)
    password = "".join(password)
    
    pyperclip.copy(password)
    password_input.delete(0, END)
    password_input.insert(0,password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website: {
                    "email": email,
                    "password": password,
            },
        }
    messagebox_message = "These are the details that are entered: \nEmail: " + email + "\nPassword: " + password + "\nIs it ok to save?"
    
    if len(website.strip()) == 0 or len(password.strip()) == 0 or len(email.strip()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        answer = messagebox.askokcancel(title=website, message=messagebox_message)
        if answer:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
            website_input.delete(0, END)
            password_input.delete(0, END)
            
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.eval('tk::PlaceWindow . center')

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=35, justify="left")
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = Entry(width=35, justify="left")
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "dummy@email.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=21, justify="left")
password_input.grid(column=1, row=3, padx=12)

generate_pass_button = Button(text="Generate Password", width=11, command=generate)
generate_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()