from app.tasks.celery import celery
from PIL import Image
from pathlib import Path
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

