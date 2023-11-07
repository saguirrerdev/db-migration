from fastapi import APIRouter, UploadFile, HTTPException, status
from utils.s3 import s3_upload
from db.database import RedshiftConnection
from utils.read_file import read_file
from models import departments

router = APIRouter()

@router.post("/upload")
async def upload_departments(file: UploadFile):
    try:
        await departments.upload_departments_csv(file)
        return {"message": "Filed uploaded succesfully"}
    except Exception as e:
        raise e
  
@router.get("/hires_by_quarter")
async def hires_by_quarter_2021():
    try:
        query = read_file("app/queries/employes_by_quarter.sql")
        response = RedshiftConnection() \
            .query(query) \
            .fetch_json()
        return response
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )

@router.get("/over_mean_hires")
async def over_mean_hires_2021():
    try:
        query = read_file("app/queries/department_hires.sql")
        response = RedshiftConnection() \
            .query(query) \
            .fetch_json()
        return response
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )


