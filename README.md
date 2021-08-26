[![Generic badge](https://img.shields.io/badge/python_version-3.9-blue.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/flask_version-2.0.1-blue.svg)](https://shields.io/)
## FLask Mail App

### FIELDS TO BE EDITED:
    - SUBJECT:                      email subject
    - SENDER:                       email of the sender
    - RECIPIENT:                    email of the recipient
    - BODY:                         email body
    - URL:                          URL that triggers the email to be send on GET request
    - app.config['MAIL_SERVER']:    mail server address
    - app.config['MAIL_PORT']:      mail server port
    - app.config['MAIL_USERNAME']   mail server username
    - app.config['MAIL_PASSWORD']   mail server password
    - app.config['MAIL_USE_TLS']    use TLS (false/true)
    - app.config['MAIL_USE_SSL']    use SSL (false/true)
    - return of index():            message/status code/whatever is returned when email is sent