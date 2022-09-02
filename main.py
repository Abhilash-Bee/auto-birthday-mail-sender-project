import pandas
import datetime as dt
import smtplib
from random import randint
USER_NAME = "iambee8498@gmail.com"
PASSWORD = "pocdyoxiikrhlqui"

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
data_detail_dict = data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
date = now.day
month = now.month

for record in data_detail_dict:
    if record["day"] == date and record["month"] == month:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        # actual name from birthdays.csv
        letter_no = randint(1, 3)
        with open(f"./letter_templates/letter_{letter_no}.txt") as file:
            letter = file.read()
        letter = letter.replace("[NAME]", record["name"])
        # print(letter)

# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=USER_NAME, password=PASSWORD)
            connection.sendmail(
                from_addr=USER_NAME,
                to_addrs=record["email"],
                msg=f"Subject:Happy Birthday\n\n{letter}"
            )
            print("Successfully sent")
