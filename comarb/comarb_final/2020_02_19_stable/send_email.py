import os
import smtplib
import ssl
from email.mime.text import MIMEText

# my = the sender's email address
# you ==the recipient's email address
sender_gmail = "python.notificaciones@gmail.com"
sender_gmail_passwords = os.environ.get("PYTHON_GMAIL_PASSWORD")
# ,"mvmotter@chaco.gob.ar","franco.biolchi@chaco.gob.ar", "atp.somontiel@chaco.gob.ar]
receive_mail = ["alejandro.mfe@gmail.com"]
host = "smtp.gmail.com"
port = 465


def send(subject, message):
    # Configuración del mail
    # my = the sender's email address
    # you ==the recipient's email address
    text = MIMEText(message)
    text["From"] = sender_gmail
    #text["To"] = receive_mail
    text["Subject"] = subject

    # Crea un contexto seguro de SSL con el servidor
    # y envia el email.
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        # me logueo
        server.login(sender_gmail, sender_gmail_passwords)
        # Enviamos el text
        # con el for puedo enviar multiples mails
        for email in receive_mail:
            text["To"] = email
            server.sendmail(sender_gmail, email, text.as_string())

        # la conexion se cierra automaticamente
        # al salir del with

#import time
#message = f"Este es un mensaje de prueba {time.ctime()}"
#send("Prueba", message)
