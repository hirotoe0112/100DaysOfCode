from tkinter import *


def button_clicked():
    my_label["text"] = input.get()


window = Tk()
window.title("day27")
window.config(padx=20, pady=20)

my_label = Label(bg="#cccccc", text="Test Label", font=("Arial", 18, "bold"))
my_label["text"] = "My Brilliant Wonderful Fantastic GUI Program"
my_label.config(padx=20, pady=20)
my_label.grid(column=0, row=0)

button = Button(text="Click", command=button_clicked)
button.config(padx=20, pady=10)
button.grid(column=1, row=1)

new_button = Button(text="Don't Click")
new_button.config(padx=20, pady=10)
new_button.grid(column=2, row=0)

input = Entry(width=50)
input.insert(0, "default text")
input.insert(4, "aaaaaa")
input.grid(column=3, row=2)


window.mainloop()
