import boto3

AWS_BUCKET = "dbmigrationdata"

s3 = boto3.resource('s3')
bucket = s3.Bucket(AWS_BUCKET)

def s3_upload(contents:bytes, name:str):
  try:
    bucket.put_object(Body=contents, Key=name)
  except Exception as e:
    raise Exception("Error uploading the file object")