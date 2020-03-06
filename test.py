from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage
app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>welcome</h1>"

@app.route("/email", methods=['POST','GET'])
def email():

    data = request.get_json()

    msg = EmailMessage()
    msg['Subject'] = data.get('subject')
    msg['From'] = 'xxxxxx@gmail.com'
    msg['To'] = data.get('to')
    msg.set_content(data.get('content'))
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login('xxxxxx@gmail.com','xxxxx')
        num = data.get('num')

        for x in range(int(num)):
            smtp.send_message(msg)

    return "email"

if __name__ == "__main__":
    app.run(threaded=True, port=5000)
