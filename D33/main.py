import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
GMAIL_SMTP = "smtp.gmail.com"
GMAIL_PORT = 587
iss_latitude = None
iss_longitude = None
sunrise = None
sunset = None


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

with open ("credentials\email.txt") as email:
    my_email = email.readline()

with open ("credentials\pw.txt") as pw:
    my_password = pw.readline()

receiver = "mek.chou@outlook.com"

def iss_position():
    global iss_latitude, iss_longitude
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def iss_in_range():
    return MY_LAT -5 <= iss_latitude <= MY_LAT +5 and MY_LONG-5 <= iss_longitude <= MY_LONG +5

def is_dark():
    time_now = datetime.now()
    return time_now.hour > sunset or time_now.hour < sunrise


def my_position():
    global sunrise, sunset
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


def main():
    my_position()
    iss_position()
    if iss_in_range() and is_dark():
        print("ok")
        send_email(receiver=receiver, content = "Look up for ISS")
    else:
        print("no")
        # send_email(receiver=receiver, content = "Look up for ISS")
        
def send_email(receiver, content):
    with smtplib.SMTP(host=GMAIL_SMTP, port=GMAIL_PORT) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email
            , to_addrs=receiver
            , msg=f"Subject: ISS\n\n{content}"
        )

# time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


if __name__ == "__main__":
    while True:
        main()
        time.sleep(60)
