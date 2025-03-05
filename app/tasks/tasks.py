import os
import smtplib
from pathlib import Path

from dotenv import load_dotenv
from PIL import Image
from pydantic import EmailStr

from app.tasks.celery import celery
from app.tasks.email_templates import email_new_user_created

load_dotenv()
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PASS = os.getenv("SMTP_PASS")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_USER = os.getenv("SMTP_USER")


@celery.task
def resize_pic(
    path: str,
):
    im_path = Path(path)
    img = Image.open(im_path)
    resized_1000_500 = img.resize((1000, 600))
    resized_200_100 = img.resize((200, 100))
    resized_1000_500.save(
        f"app/static/images/{im_path.name}_resized_1000_600.webp", format="WEBP"
    )
    resized_200_100.save(
        f"app/static/images/{im_path.name}_resized_200_100.webp", format="WEBP"
    )


@celery.task
def send_confirmation_to_registered_user(user: dict, email_to: EmailStr):
    msg_content = email_new_user_created(user, email_to)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(
            from_addr=SMTP_USER, to_addrs=email_to, msg=msg_content.as_string()
        )
