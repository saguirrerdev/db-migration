from fastapi import UploadFile, HTTPException, status
from db.db import DB
from datetime import datetime

import pandas as pd
import io

COLUMNS_NAMES = ["id", "name", "datetime", "department_id", "job_id"]
MAX_ROWS_EXPECTED = 1000
AMOUNT_COLUMNS_EXPECTED = 5
FILENAME='hired_employees.csv'
DTYPES = {
  3: pd.Int64Dtype(),
  4: pd.Int64Dtype()
}
async def upload_hired_employees_csv(file: UploadFile):
  try:
    validate_csv(file)

    hired_employees_df = pd.read_csv(io.BytesIO(await file.read()), header=None, dtype=DTYPES)

    validate_csv_data(hired_employees_df)

    hired_employees_df.columns = COLUMNS_NAMES
    hired_employees_df["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    hired_employees_df.to_sql(
      "hired_employees_staging",
      con=DB().conn,
      if_exists='append',
      index=False
    )

    DB().query("CALL load_hired_employees();").callproc()
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
  
  if df[0].dtypes != 'int' or df[1].dtypes != 'object' or df[2].dtypes != 'object' or df[3].dtypes != pd.Int64Dtype() or df[4].dtypes != pd.Int64Dtype():
    raise HTTPException(
        detail=f"Columns data types not meet",
        status_code=status.HTTP_400_BAD_REQUEST
      )
  
  if df.shape[0] > 1000:
    raise HTTPException(
      detail=f"Maxímun rows expected {MAX_ROWS_EXPECTED}, got {df.shape[0]}",
      status_code=status.HTTP_400_BAD_REQUEST
    )