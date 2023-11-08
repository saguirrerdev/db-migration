from fastapi import APIRouter, UploadFile
from models import hired_employees

router = APIRouter()

@router.post("/upload")
async def upload_hired_employees(file: UploadFile):
    try:
        await hired_employees.upload_hired_employees_csv(file)
        return {"message": "Filed uploaded succesfully"}
    except Exception as e:
        raise e

