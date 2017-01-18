from django.core.mail import EmailMessage


def send_email(body, subject, to):
    email = EmailMessage(subject, body, to=to)
    return email.send()

