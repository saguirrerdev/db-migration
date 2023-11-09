import boto3
import json

from botocore.exceptions import ClientError

def get_secret(key_name=None):
    if not key_name:
        return None

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name='us-east-1'
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=key_name
        )
    except ClientError as e:
        raise e
    
    secret = json.loads(get_secret_value_response['SecretString'])

    return secret
