import pandas
import datetime as dt
import os
import random
import smtplib

sender_address = "example@example.com"
password = "XXXXXXXX"
is_valid = False


def get_birthday_list():
    today_month = dt.datetime.now().month
    today_day = dt.datetime.now().day

    birthday_list = pandas.read_csv("birthdays.csv")
    today_birthday_list = birthday_list[
        (birthday_list.month == today_month) & (birthday_list.day == today_day)
    ]
    return today_birthday_list


def get_letter(name):
    letters = os.listdir("letter_templates")
    selected_letter = random.choice(letters)
    with open(f"letter_templates/{selected_letter}") as letter:
        letter_content = letter.read().replace("[NAME]", name)
        return letter_content


def send_mail(receiver_email, letter):
    if not is_valid:
        print("sent")
        return
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_address, password=password)
        connection.sendmail(
            from_addr=sender_address,
            to_addrs=receiver_email,
            msg=f"Subject:Happy Birthday!\n\n{letter}",
        )


targets = get_birthday_list()
for target in targets.itertuples(index=False):
    letter = get_letter(target.name)
    send_mail(target.email, letter)
