from flask_mail import Message
from . import mail
from flask import render_template


# def mail_message(subject, sender, recepients, text_body, html_body):
#     msg = Message(subject,sender=sender,recipients=recepients)
#     msg.body = text_body
#     msg.html = html_body
#     mail.send(msg)

def send_reset_email(user):
    token = user.get_reset_password_token()
    send_email('Reset Password',sender=app.config['MAIL_USERNAME'],recepients=[user.email],text_body=render_template('auth/reset_password.txt',user=user, token=token),html_body=render_template('auth/reset_password.html',user=user, token=token))
def mail_message(subject,template,to,**kwargs):
    sender_email ='chegehannah45@gmail.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)