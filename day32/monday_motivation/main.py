import smtplib
import datetime as dt
import random

sender_address = "example@example.com"
password = "XXXXXXXX"
receiver_addresses = ["example2@example.com"]
is_valid = False


def get_quote():
    with open("quotes.txt") as file:
        quotes = file.read().splitlines()
        return random.choice(quotes)


def send_mail(quote):
    if not is_valid:
        print("sent")
        return
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_address, password=password)
        connection.sendmail(
            from_addr=sender_address,
            to_addrs=receiver_addresses,
            msg=f"Subject:Monday Motivation\n\n{quote}",
        )


today_of_the_week = dt.datetime.now().weekday()
if today_of_the_week == 0:
    quote = get_quote()
    print(quote)
    send_mail(quote=quote)
