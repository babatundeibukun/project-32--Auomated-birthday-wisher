import datetime as dt
import pandas as pd
import random
import smtplib
now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)
data = pd.read_csv("birthdays.csv")

birthdays_dict = {(row.month, row.day): row
                  for (index, row) in data.iterrows()}

with open("letter_templates/letter_1.txt") as first_letter:
    first = first_letter.read()
with open("letter_templates/letter_2.txt") as first_letter:
    second = first_letter.read()
with open("letter_templates/letter_3.txt") as first_letter:
    third = first_letter.read()

list_letters = (first, second, third)

if (today_month, today_day) in birthdays_dict:
    birthday_person = (birthdays_dict[today])
    random_index = random.randint(0, 2)
    letter = list_letters[random_index]
    final_letter = letter.replace("[NAME]", birthday_person["name"])
    my_email = "babatundeibukun981@gmail.com"
    password = "Barbie4sure"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person['email'],
                            msg=f"Subject:Happy Birthday\n\n{final_letter}")

