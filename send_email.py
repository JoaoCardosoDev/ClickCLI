import smtplib, ssl
import click
from email.mime.text import MIMEText

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "eticnewstest@gmail.com"
receiver_email = "eticnewstest+breakfastorder@gmail.com"
password = "odam kbgi evww jhql"

@click.command()
@click.option('--room', prompt='[Room number]: ', help='Please provide your room number.')
@click.option('--order', prompt='Please provide a description of what you would like for breakfast:\n', help='List items youd like to have for breakfast. Reception number for help dial 9.')
def change_body(room, order):
    subject = room
    body = order

    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = receiver_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    click.echo("Order registered. ETA for room service is 45 minutes. Dial 9 for reception for any inquire.")
