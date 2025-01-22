from fastapi import UploadFile, APIRouter
import shutil

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
    with open(f'app/static/images/{original_filename}.webp', "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
