from sqlalchemy import create_engine
from utils import secrets

import os

class DB:
  
    def __init__(self):
        self.conn = None
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.dbname = os.getenv("DB_NAME")
        self.query_string = None
        self.connect()

    def connect(self):
        if self.conn:
            return self
        
        conn = create_engine(self.conn_string())

        self.conn = conn

        return self
    
    def conn_string(self):
        secret_keys = secrets.get_secret(os.getenv("DB_SECRET_KEY_NAME"))

        return f"mysql+mysqlconnector://{secret_keys['username']}:{secret_keys['password']}@{self.host}:{self.port}/{self.dbname}"
    
    
    def query(self, query:str = ''):
        self.query_string = query

        return self

    def fetch_json(self):
      pass