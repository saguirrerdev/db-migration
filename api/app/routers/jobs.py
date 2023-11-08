from fastapi import APIRouter, UploadFile, HTTPException, status
from models import jobs

router = APIRouter()

@router.post("/upload")
async def upload_jobs(file: UploadFile):
    try:
        await jobs.upload_jobs_csv(file)
        return {"message": "Filed uploaded succesfully"}
    except Exception as e:
        raise e

