from app.tasks.celery import celery
from PIL import Image
from pathlib import Path
from app.tasks.email_templates import email_new_user_created
from pydantic import EmailStr
import smtplib
from config import SMTP_HOST,SMTP_PORT,SMTP_USER,SMTP_PASS
@celery.task
def resize_pic(
        path: str,
):
    im_path= Path(path)
    img= Image.open(im_path)
    resized_1000_500= img.resize((1000,600))
    resized_200_100= img.resize((200,100))
    resized_1000_500.save(f'app/static/images/{im_path.name}_resized_1000_600.webp', format='WEBP')
    resized_200_100.save(f'app/static/images/{im_path.name}_resized_200_100.webp', format='WEBP')

@celery.task
def send_confirmation_to_registered_user(
        user: dict,
        email_to: EmailStr
):
    msg_content= email_new_user_created(user, email_to)
    with smtplib.SMTP_SSL(SMTP_HOST,SMTP_PORT) as server:
        server.login(SMTP_USER,SMTP_PASS)
        server.sendmail(
            from_addr=SMTP_USER,
            to_addrs=email_to,
            msg=msg_content.as_string()
        )
