from fastapi import FastAPI, UploadFile, status, HTTPException
from s3 import s3_upload

app = FastAPI()

@app.post("/upload")
async def upload_csv(file: UploadFile):
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
    file_name = file.filename

    try: 
        s3_upload(file_content, file_name)
        return {"message": f"{file_name} uploaded successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
