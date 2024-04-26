##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import datetime as dt
import random as rand
import pandas as pd
import smtplib

PLACEHOLDER = "[NAME]"
FILE_PATHS = [f"letter_{n}.txt" for n in range(1,4)]
GMAIL_SMTP = "smtp.gmail.com"
GMAIL_PORT = 587
letters = []

with open ("credentials\email.txt") as email:
    my_email = email.readline()

with open ("credentials\pw.txt") as pw:
    my_password = pw.readline()

# read csv into dict
birthdays_df = pd.read_csv(r"data\birthdays.csv")
birthdays_dict = birthdays_df.to_dict(orient="records")
# print(birthdays_dict)

# read letter's into list
for file_path in FILE_PATHS:
    with open(f"D32/{file_path}", "r") as file:
        content = file.read()
        letters.append(content)
# print(letters)

# check date function
def check_date(receiver):
    today = dt.datetime.now()
    today_month = today.month
    today_date = today.day
    return receiver["month"] == today_month and receiver["day"] == today_date

# pick random letter
def pick_random_letter():
    return rand.choice(letters)

# replace name in letter
def replace_name(name, letter):
    new_letter = letter.replace(PLACEHOLDER, name)
    return new_letter
    
    
def send_email(receiver, letter):
    with smtplib.SMTP(host=GMAIL_SMTP, port=GMAIL_PORT) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email
            , to_addrs=receiver
            , msg=f"Subject: Happy Birthday!\n\n{letter}"
        )


for receiver in birthdays_dict:
    if check_date(receiver):
        print(f"{receiver["name"]}'s birthday is {receiver["month"]}/{receiver["day"]}, it's today!")
        letter = pick_random_letter()
        new_letter = replace_name(receiver["name"], letter)
        send_email(receiver["email"], new_letter)
        # print(new_letter)
    else:
        print(f"{receiver["name"]}'s birthday is {receiver["month"]}/{receiver["day"]}, not today.")
        



