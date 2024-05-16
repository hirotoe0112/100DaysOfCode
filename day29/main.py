from tkinter import *
from tkinter import messagebox
import random

FONT = ("Consolas", 12)
DEFAULT_EMAIL = "example@example.com"
LETTERS_COUNT = 8
NUMBERS_COUNT = 2
SYMBOLS_COUNT = 2
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    password_characters = (
        [random.choice(letters) for _ in range(LETTERS_COUNT)]
        + [random.choice(numbers) for _ in range(NUMBERS_COUNT)]
        + [random.choice(symbols) for _ in range(SYMBOLS_COUNT)]
    )
    random.shuffle(password_characters)
    password = "".join(password_characters)
    password_entry.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)
    password_entry.focus()
    password_entry.selection_range(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = user_entry.get()
    password = password_entry.get()

    if website == "" or username == "" or password == "":
        messagebox.showerror(
            title="Error", message="Please don't leave any fields empty."
        )
        return

    is_continue = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered: \n\nWebsite: {website} \nEmail: {username} \nPassword: {password} \n\nIs it ok to save?",
    )
    if not is_continue:
        return

    try:
        with open("data.txt", "a") as file:
            file.write(f"{website} | {username} | {password}\n")
        messagebox.showinfo(title="Success", message="Password saved!")
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()
    except:
        print("Error saving password")
        messagebox.showerror(
            title="Error", message="Sorry, there was an error saving the password."
        )


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=0, row=0, columnspan=3)

website_label = Label(text="Website:", font=FONT, pady=5)
website_label.grid(column=0, row=1, sticky="e")

user_label = Label(text="Email/Username:", font=FONT, pady=5)
user_label.grid(column=0, row=2, sticky="e")

password_label = Label(text="Password:", font=FONT, pady=5)
password_label.grid(column=0, row=3, sticky="e")

website_entry = Entry(width=40, font=FONT)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w", padx=3)
website_entry.focus()

user_entry = Entry(width=40, font=FONT)
user_entry.insert(0, DEFAULT_EMAIL)
user_entry.grid(column=1, row=2, columnspan=2, sticky="w", padx=3)

password_entry = Entry(width=21, font=FONT)
password_entry.grid(column=1, row=3, sticky="w", padx=3)

password_button = Button(
    text="Generate Password", font=FONT, command=lambda: generate_password()
)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=24, height=2, font=FONT, command=lambda: save())
add_button.grid(column=1, row=4, columnspan=2, sticky="w", pady=5)

window.mainloop()
