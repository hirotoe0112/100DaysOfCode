from tkinter import *
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FRONT_COLOR = "#FFFFFF"
FRONT_WORD_COLOR = "#000000"
BACK_WORD_COLOR = "#FFFFFF"
FONT_NAME = "Consolas"

# ---------------------------- GLOBAL ------------------------------- #
started = False
current_item = {}


# ---------------------------- READ DATA ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/russian_words.csv")
finally:
    data_dict = data.to_dict(orient="records")


# ---------------------------- NEXT CARD ------------------------------- #
def next_card():
    global flip_timer
    try:
        window.after_cancel(flip_timer)
    except NameError:
        pass
    global current_item
    current_item = random.choice(data_dict)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(language_text, text="Russian", fill=FRONT_WORD_COLOR)
    canvas.itemconfig(word_text, text=f"{current_item["Russian"]}", fill=FRONT_WORD_COLOR)
    flip_timer = window.after(3000, lambda: flip_card(current_item))


# ---------------------------- FLIP CARD ------------------------------- #
def flip_card(item):
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(language_text, text="English", fill=BACK_WORD_COLOR)
    canvas.itemconfig(word_text, text=f"{item["English"]}", fill=BACK_WORD_COLOR)


# ---------------------------- PRESS CHECK AND CROSS BUTTON ------------------------------- #
def press_button(is_check_button):
    global started
    if started:
        if is_check_button:
            data_dict.remove(current_item)
            pandas.DataFrame.to_csv(pandas.DataFrame(data_dict), "data/words_to_learn.csv", index=False)
    else:
        if is_check_button:
            # start the app when a user press the check button
            started = True
        else:
            # shut down the app when a user press the cross button before starting the app
            window.destroy()
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
language_text = canvas.create_text(
    400,
    150,
    text="press ☑ button",
    fill=FRONT_WORD_COLOR,
    font=(FONT_NAME, 40, "italic"),
)
word_text = canvas.create_text(
    400, 263, text="нажмите кнопку ☑", fill=FRONT_WORD_COLOR, font=(FONT_NAME, 60, "bold")
)
canvas.grid(column=0, row=0, columnspan=2)

cross_button_image = PhotoImage(file="images/wrong.png")
cross_button = Button(
    image=cross_button_image, highlightthickness=0, border=0, cursor="hand2", command=lambda: press_button(is_check_button=False)
)
cross_button.grid(column=0, row=1)

check_button_image = PhotoImage(file="images/right.png")
check_button = Button(
    image=check_button_image,
    highlightthickness=0,
    border=0,
    cursor="hand2",
    command=lambda: press_button(is_check_button=True),
)
check_button.grid(column=1, row=1)

window.mainloop()
