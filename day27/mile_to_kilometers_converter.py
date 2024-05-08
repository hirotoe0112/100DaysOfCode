from tkinter import *

font = ("Arial", 20, "normal")


def click_calculate_button():
    mile = mile_entry.get()
    km = float(mile) * 1.609
    result_label["text"] = round(km, 4)


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

mile_entry = Entry(width=10, font=font)
mile_entry.grid(column=1, row=0)
mile_entry.focus()

mile_label = Label(text="Miles", font=font)
mile_label.config(padx=10, pady=10)
mile_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to", font=font)
is_equal_to_label.config(padx=10, pady=10)
is_equal_to_label.grid(column=0, row=1)

result_label = Label(text="0", font=font)
result_label.config(padx=10, pady=10)
result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=font)
km_label.config(padx=10, pady=10)
km_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=click_calculate_button)
calc_button.config(padx=10, pady=10)
calc_button.grid(column=1, row=2)

window.mainloop()
