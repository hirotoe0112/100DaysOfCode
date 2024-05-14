from tkinter import *
import winsound

# ---------------------------- CONSTANTS ------------------------------- #
# https://colorhunt.co/palette/dcf2f17fc7d93654860f1035
BASE_COLOR = "#DCF2F1"
SUB_COLOR = "#7FC7D9"
FONT_COLOR = "#0F1035"
TIMER_COLOR = "#DCF2F1"
CHECK_COLOR = "#365486"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer_id = None


def convert_seconds_to_minutes(seconds):
    minutes = seconds // 60
    seconds = str(seconds % 60).zfill(2)
    return f"{minutes}:{seconds}"


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer_id)
    start_button.config(state="normal")
    reset_button.config(state="disabled")
    global reps
    reps = 0
    title_label.config(text="Timer")
    check_label.config(text="")
    canvas.itemconfig(count_text, text=convert_seconds_to_minutes(WORK_MIN * 60))


# ---------------------------- TIMER MECHANISM ------------------------------- #
def increase_check():
    check_label["text"] += "✔"


def start_timer():
    start_button.config(state="disabled")
    reset_button.config(state="normal")
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Break")
        winsound.PlaySound("break.wav", winsound.SND_FILENAME)
        count_down(long_break_seconds)
    elif reps % 2 == 0:
        title_label.config(text="Break")
        winsound.PlaySound("break.wav", winsound.SND_FILENAME)
        count_down(short_break_seconds)
    else:
        title_label.config(text="Work")
        winsound.PlaySound("work.wav", winsound.SND_ASYNC)
        count_down(work_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    formatted_timer = convert_seconds_to_minutes(count)
    if count > 0:
        global timer_id
        timer_id = window.after(1000, count_down, count - 1)
        canvas.itemconfig(count_text, text=formatted_timer)
    else:
        start_timer()
        if reps % 2 == 0:
            increase_check()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BASE_COLOR)

title_label = Label(text="Timer", fg=FONT_COLOR, bg=BASE_COLOR, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=204, height=224, bg=BASE_COLOR, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=image)
count_text = canvas.create_text(
    102,
    130,
    text=convert_seconds_to_minutes(WORK_MIN * 60),
    fill=TIMER_COLOR,
    font=(FONT_NAME, 35, "bold"),
)
canvas.grid(column=1, row=1)

start_button = Button(
    text="Start",
    highlightthickness=0,
    border=0,
    bg=SUB_COLOR,
    fg=FONT_COLOR,
    font=(FONT_NAME, 15),
    command=lambda: start_timer(),
)
start_button.grid(column=0, row=2)

reset_button = Button(
    text="Reset",
    highlightthickness=0,
    border=0,
    bg=SUB_COLOR,
    fg=FONT_COLOR,
    font=(FONT_NAME, 15),
    command=lambda: reset_timer(),
    state="disabled",
)
reset_button.grid(column=2, row=2)

check_label = Label(text="", fg=CHECK_COLOR, bg=BASE_COLOR, font=(FONT_NAME, 15))
check_label.grid(column=1, row=3)

window.mainloop()
