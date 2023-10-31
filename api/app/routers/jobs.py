from fastapi import APIRouter, UploadFile, HTTPException, status
from utils.s3 import s3_upload

router = APIRouter()

@router.post("/upload")
async def upload_jobs(file: UploadFile):
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
  file_name = f"jobs/{file.filename}"

  try: 
      s3_upload(file_content, file_name)
      return {"message": f"{file_name} uploaded successfully"}
  except Exception as e:
      raise HTTPException(
          status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
          detail=str(e),
      )

