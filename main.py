from flask import Flask
from flask_mail import Mail, Message

SUBJECT = 'your message'
SENDER = 'sender@example.com'
RECIPIENT = 'recipient@example.com'
BODY = 'message body'
URL = '/'

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '7ba3199c5fff19'
app.config['MAIL_PASSWORD'] = '19b108e3235d30'
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
