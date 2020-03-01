from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage
app = Flask(__name__)

@app.route("/email", methods=['POST','GET'])
def email():

    data = request.get_json()

    msg = EmailMessage()
    msg['Subject'] = data.get('subject')
    msg['From'] = 'marcuslam616@gmail.com'
    msg['To'] = data.get('to')
    msg.set_content(data.get('content'))
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login('marcuslam616@gmail.com','aA26761683')
        num = data.get('num')

        for x in range(int(num)+1):
            smtp.send_message(msg)

    return "email"
