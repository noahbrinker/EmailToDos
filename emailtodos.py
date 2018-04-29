# This app will go to Trello, find a Specific list of cards on a
# board (my to do today list), and email that list to me each day at 7 AM CST.


# API Key = ee01b6b704ffd6861ce7f85989f860a6
# Token = 2a5ddadcb53c47023d190b5f43e026f4141d23c87f811673db42fdc9f8692621
# Trello List ID = 5a5057e3d204a0aa3f33fa2d



import requests
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from threading import Timer


# Run this function every day at 7 AM CST
x = datetime.today()
y = x.replace(day = x.day+1, hour = 7, minute = 0, second = 0, microsecond = 0)
delta_t = y-x

secs=delta_t.seconds+1


# Get To Do List from Trello
url = "https://api.trello.com/1/lists/5a5057e3d204a0aa3f33fa2d/cards?key=ee01b6b704ffd6861ce7f85989f860a6&token=2a5ddadcb53c47023d190b5f43e026f4141d23c87f811673db42fdc9f8692621"
querystring = {"fields":"name","key":"ee01b6b704ffd6861ce7f85989f860a6","token":"2a5ddadcb53c47023d190b5f43e026f4141d23c87f811673db42fdc9f8692621"}
response = requests.request("GET", url, params = querystring)



# Send To Do List to Email
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("email@gmail.com", "password")

def send_email():
            try:
                msg = MIMEText(response.text)
                msg["From"] = "email@gmail.com"
                msg["To"] = "email@gmail.com"
                msg["Subject"] = "To Do Today"
                s.sendmail("email@gmail.com", "email@gmail.com", msg.as_string())
                s.quit()
            except:
                 print("Error sending email.")

t = Timer(secs, send_email())
t.start()
