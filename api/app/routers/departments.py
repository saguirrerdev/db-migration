from fastapi import APIRouter, UploadFile, HTTPException, status
from utils.s3 import s3_upload
from db.database import RedshiftConnection
from utils.read_file import read_file

router = APIRouter()

@router.post("/upload")
async def upload_departments(file: UploadFile):
    if not file:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File not found"
        )
        
    if file.content_type != 'text/csv':
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"File type {file.content_type} not supported"
        )
        
    file_content = await file.read()
    file_name = f"departments/{file.filename}"

    try: 
        s3_upload(file_content, file_name)
        return {"message": f"{file_name} uploaded successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )
  
@router.get("/hires_by_quarter")
async def hires_by_quarter_2021():
    try:
        query = read_file("app/queries/employes_by_quarter.sql")
        response = RedshiftConnection() \
            .query(query) \
            .fetch_json()
        return response
    except Exception as e:
        raise Exception(e)

@router.get("/over_mean_hires")
async def over_mean_hires_2021():
    try:
        query = read_file("app/queries/department_hires.sql")
        response = RedshiftConnection() \
            .query(query) \
            .fetch_json()
        return response
    except Exception as e:
        raise Exception(e)


