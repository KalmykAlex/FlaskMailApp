from flask import Flask
from flask_mail import Mail, Message

SUBJECT = 'your message'
SENDER = 'sender@example.com'
RECIPIENT = 'recipient@example.com'
BODY = 'message body'
URL = '/'

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.server'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'username'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)


@app.route(URL)
def index():
    msg = Message(SUBJECT,
                  sender=SENDER,
                  recipients=[RECIPIENT])
    msg.body = BODY
    mail.send(msg)
    return 'Sent mail!'


if __name__ == '__main__':
    app.run(debug=True)
