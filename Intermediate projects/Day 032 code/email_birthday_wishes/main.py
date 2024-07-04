# Automatic birthday emailer

import smtplib
import datetime
import random
import os
import csv # Since its usually faster than pandas for smaller datasets

def read_letter(file_name):
    with open(file_name, "r") as file:
        return file.readlines()

date_today = str(datetime.date.today())
from_name = "" # put your name here
from_email = "" # put your email here
password = "" # put the password for the email here
smtp_service = "" # generated smtp token from email service

with open("birthdays.csv", mode = "r") as file:
    csv_reader = csv.DictReader(file)
    
    data_list = []
    
    for row in csv_reader:
        data_list.append(row)

for data in data_list:
    if data["year"] + "-" + data["month"] + "-" + data["day"] == date_today:
        
        letter_content = read_letter(f"letter_templates/{random.choice(os.listdir('letter_templates'))}")
        message = ""
        
        # Editing the letter message so that its more personalised
        for lines in letter_content:
            message += lines.replace("[NAME]", data["name"]).replace("[FROM]", from_name)
            
        with smtplib.SMTP(smtp_service) as connection:
            connection.starttls()
            connection.login(from_email, password)
            connection.sendmail(
                from_addr=from_email, 
                to_addrs=data["email"], 
                msg=f"Subject: Happy Birthday\n\n{message}"
            )