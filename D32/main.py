import smtplib

my_email = "mek.chou@gmail.com"
password = "itzmaoqyfcsbcgae"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email
        , to_addrs="mek.chou@outlook.com"
        , msg="Subject: Hello\n\nThis is the body of my email."
        )