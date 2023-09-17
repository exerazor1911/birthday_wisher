##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import pandas as pd
import random
import smtplib as sm
import os


now = dt.datetime.now()
day = now.day
month = now.month
MY_EMAIL = 'aeg9145@gmail.com'
MY_PASSWORD = os.environ.get('MAIL_APP_PASS')


df = pd.read_csv('birthdays.csv')
result = df.query('month == @month and day == @day')


def send_email(name, email):
    file_num = random.randint(1, 3)
    with open(f'letter_templates/letter_{file_num}.txt') as letter_file:
        data = letter_file.read().replace('[NAME]', name)
    with sm.SMTP('smtp.gmail.com') as conn:
        conn.starttls()
        conn.login(user=MY_EMAIL, password=MY_PASSWORD)
        conn.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f'Subject:Happy Birthday {name}\n\n{data}')


if not result.empty:
    result.apply(
        lambda row:
            send_email(row['name'], row['email'])
        , axis=1
    )
