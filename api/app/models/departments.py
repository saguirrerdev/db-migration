from fastapi import UploadFile, HTTPException, status
from db.db import DB
from datetime import datetime

import pandas as pd
import io

COLUMNS_NAMES = ["id", "department"]
MAX_ROWS_EXPECTED = 1000
AMOUNT_COLUMNS_EXPECTED = 2

async def upload_departments_csv(file: UploadFile):
  try:
    validate_csv(file)

    departments_df = pd.read_csv(io.BytesIO(await file.read()), header=None)

    validate_csv_data(departments_df)

    departments_df.columns = COLUMNS_NAMES
    departments_df["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    departments_df.to_sql(
      "departments_staging",
      con=DB().conn,
      if_exists='append',
      index=False
    )

    DB().query("CALL load_departments();").callproc()
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
  
  if file.filename != "departments.csv":
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