from email.message import EmailMessage

from pydantic import EmailStr

import os
from dotenv import load_dotenv

load_dotenv()

SMTP_USER = os.getenv("SMTP_USER")

def email_new_user_created(
        user: dict,
        email_to: EmailStr
):
    email = EmailMessage()
    email['Subject'] = 'User created confirmation'
    email['From'] = SMTP_USER
    email['To'] = email_to
    email.set_content(
        f""" 
        <h3>Здравствуйте, {user['name']}. Вы зарегистрировались на нашем сервисе c почтовым ящиком {user['email']}.</h3>
        """,
        subtype='html'
    )
    return email
