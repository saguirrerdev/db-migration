from fastapi import UploadFile, HTTPException, status
from db.db import DB
from datetime import datetime

import pandas as pd
import io

COLUMNS_NAMES = ["id", "job"]
MAX_ROWS_EXPECTED = 1000
AMOUNT_COLUMNS_EXPECTED = 2
FILENAME='jobs.csv'


async def upload_jobs_csv(file: UploadFile):
  try:
    validate_csv(file)

    jobs_df = pd.read_csv(io.BytesIO(await file.read()), header=None)

    validate_csv_data(jobs_df)

    jobs_df.columns = COLUMNS_NAMES

    jobs_df["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    jobs_df.to_sql(
      "jobs_staging",
      con=DB().conn,
      if_exists='append',
      index=False
    )

    DB().query("CALL load_jobs();").callproc()
  except Exception as e:
    raise e    

def validate_csv(file: UploadFile):
  if not file:
    raise HTTPException(
      detail="File not found",
      status_code=status.HTTP_400_BAD_REQUEST
    )
        
  if file.content_type != 'text/csv':
    raise HTTPException(
      detail=f"File type {file.content_type} not supported",
      status_code=status.HTTP_400_BAD_REQUEST
    )  
  
  if file.filename != FILENAME:
    raise HTTPException(
      detail="The name of the file does not match the requirement",
      status_code=status.HTTP_400_BAD_REQUEST
    )
  
def validate_csv_data(df: pd.DataFrame):

  if len(df.columns) != AMOUNT_COLUMNS_EXPECTED:
    raise HTTPException(
      detail=f"Expected {AMOUNT_COLUMNS_EXPECTED} columns, got {len(df.columns)}",
      status_code=status.HTTP_400_BAD_REQUEST
    )
  
  if df[0].dtypes != 'int' or df[1].dtypes != 'object':
    raise HTTPException(
        detail=f"Columns data types not meet",
        status_code=status.HTTP_400_BAD_REQUEST
      )
  
  if df.shape[0] > 1000:
    raise HTTPException(
      detail=f"Maxímun rows expected {MAX_ROWS_EXPECTED}, got {df.shape[0]}",
      status_code=status.HTTP_400_BAD_REQUEST
    )