from fastapi import UploadFile, APIRouter
import shutil
from app.tasks.tasks import resize_pic

router = APIRouter(
    prefix='/images',
    tags=['upload photos']
)


@router.post('/movies')
async def add_movies_images(file: UploadFile, name: int | None = None):
    if name:
        original_filename = name
    else:
        original_filename = file.filename.split('.')[0]
    im_path= f'app/static/images/{original_filename}.webp'
    with open(im_path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    resize_pic.delay(im_path)
