from fastapi import APIRouter, UploadFile, HTTPException, status
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
def hires_by_quarter_2021():
    try:
        response = departments.hires_by_quarter_2021()
        return response
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )

@router.get("/over_mean_hires")
def over_mean_hires_2021():
    try:
        response = departments.over_mean_hires_2021()
        return response
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )


