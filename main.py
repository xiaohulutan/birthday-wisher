import smtplib
import datetime as dt
import random

MY_EMAIL = "your email"
MY_PASSWORD = "your password"

now = dt.datetime.now()
data_of_week = now.weekday()
if data_of_week == 4:
    with open("quotes.txt", "r") as quotes:
        quote = quotes.readlines()
        today_quote = random.choice(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() .encode('ascii', 'ignore')
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject: Quote\n\n{today_quote}")
