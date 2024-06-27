import requests
import datetime as dt
import smtplib
import time

MY_LOCATION = {"latitude": 35.181446, "longitude": 136.906403}
is_valid = False


def get_iss_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return (iss_latitude, iss_longitude)


def is_iss_over_me():
    iss_location = get_iss_location()
    iss_latitude = iss_location[0]
    iss_longitude = iss_location[1]
    if (
        iss_latitude - 5 <= MY_LOCATION["latitude"] <= iss_latitude + 5
        and iss_longitude - 5 <= MY_LOCATION["longitude"] <= iss_longitude + 5
    ):
        return True
    return False


def is_currently_dark():
    params = {
        "lat": MY_LOCATION["latitude"],
        "lng": MY_LOCATION["longitude"],
        "tzid": "Asia/Tokyo",
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now = dt.datetime.now().hour
    if now <= sunrise or sunset <= now:
        return True
    return False


def send_mail():
    if not is_valid:
        print("sent")
        return
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="test@example.com", password="test")
        connection.sendmail(
            from_addr="test@example.com",
            to_addrs=["test@example.com"],
            msg=f"Subject:Look Up\n\nThe ISS is above you in the sky.",
        )


while True:
    if is_iss_over_me() and is_currently_dark():
        send_mail()
    time.sleep(60)
