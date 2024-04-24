import datetime as dt
import random as rand
import smtplib

GMAIL_SMTP = "smtp.gmail.com"
GMAIL_PORT = 587

with open ("credentials\email.txt") as email:
    my_email = email.readline()

with open ("credentials\pw.txt") as pw:
    my_password = pw.readline()

# load txt into list
with open("D32\quotes.txt", "r") as data_file:
    data = data_file.readlines()
    quotes = [quote.rstrip() for quote in data]
    # print(quotes)
    

# function to pick random quotes
def random_quote():
    quote = rand.choice(quotes)
    return quote

# function to check day of the week
def day_of_week():
    today = dt.datetime.now()
    today_day = today.weekday()
    return today_day


# check if Wednesday
if day_of_week() == 2:
    # function to send email
    with smtplib.SMTP(host=GMAIL_SMTP, port=GMAIL_PORT) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email
            , to_addrs="mek.chou@outlook.com"
            , msg=f"Subject: Motivational Quote\n\n{random_quote()}"
        )
    print("Today is Wed, quote sent")
else:
    print("Today is not Wed, quote not sent")