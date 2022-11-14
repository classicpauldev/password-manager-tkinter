from tkinter import *
from tkinter.messagebox import *
import tkinter.messagebox
import random
WHITE = "#FFF"
BLACK = "#000"
FONT = ("Arial", 15)
ALPHABETS = "qwertyuiopasdfghjklzxcvbnm"
SYMBOLS = "!@#$%^&*()|}{/?<>~"
INFO = "These are the details entered:\n\n"
IS_OK = "\n\nIs this okay?"

screen = Tk()
screen.title("Password Manager")
screen.config(bg=WHITE, padx=100, pady=100)

# Creating the button functions


def generate_password():
    password_entry.clipboard_clear()  # Clear previous clipboard data
    password_entry.delete(0, END)  # Delete current entry, in case of new password generated
    password = []
    for i in range(random.randint(3, 7)):
        password.append(random.choice(ALPHABETS))
    for i in range(random.randint(3, 7)):
        password.append(random.choice(ALPHABETS.upper()))
    for i in range(random.randint(3, 5)):
        password.append(random.choice(SYMBOLS))
    for i in range(random.randint(3, 5)):
        password.append(str(random.randint(0, 9)))
    random.shuffle(password)
    password = "".join(password)
    password_entry.insert(END, string=password)
    password_entry.clipboard_append(string=password)  # Auto save the password to your clipboard


def add_info():
    website = website_entry.get()
    email_user = email_username_entry.get()
    password = password_entry.get()
    new_credential = f"{website} | {email_user} | {password}"
    if len(website) == 0 or len(email_user) == 0 or len(password) == 0:
        tkinter.messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        answer = askyesno(title=f"{website}", message=f"{INFO}Email: {email_user}\nPassword: {password}{IS_OK}")
        if answer:
            with open('data.txt', mode='a') as file:
                file.write(f"{new_credential}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            tkinter.messagebox.showinfo(title="Success", message=f"{website} credentials added successfully")


# Creating the Labels

website_label = Label(text="Website:", fg=BLACK, bg=WHITE, font=FONT)
website_label.config(pady=3)
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:", fg=BLACK, bg=WHITE, font=FONT)
email_username_label.config(pady=3)
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:", fg=BLACK, bg=WHITE, font=FONT)
password_label.config(pady=3)
password_label.grid(column=0, row=3)

# Creating the Entries

website_entry = Entry(width=35, fg=WHITE, highlightthickness=0)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=35, fg=WHITE, highlightthickness=0)
email_username_entry.insert(END, string="1337@classicpaul.dev")
email_username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=20, fg=WHITE, highlightthickness=0)
password_entry.grid(column=1, row=3)

# Creating buttons

generate_password = Button(width=11, text="Generate Password", highlightbackground=WHITE, command=generate_password)
generate_password.grid(column=2, row=3)

add_button = Button(width=33, text="Add", highlightbackground=WHITE, command=add_info)
add_button.grid(column=1, row=4, columnspan=2)

# Displaying the image
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

screen.mainloop()
