import smtplib
import os

GMAIL_SMTP = "smtp.gmail.com"
GMAIL_PORT = 587


class NotificationManager:
    def __init__(self) -> None:
        self.my_email = os.environ.get("ENV_MY_EMAIL")
        self.my_password = os.environ.get("ENV_MY_PASSWORD")
        self.receiver = "mek.chou@outlook.com"

    def send_email(self, content):
        with smtplib.SMTP(host=GMAIL_SMTP, port=GMAIL_PORT) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.my_password)
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs=self.receiver,
                msg=f"Subject: Flight Price Alert\n\n{content}",
            )
