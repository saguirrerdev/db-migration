from sqlalchemy import create_engine
from utils import secrets

import os

class DB:
  
    def __init__(self):
        self.conn = None
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

        return f"mysql+mysqlconnector://{secret_keys['username']}:{secret_keys['password']}@{secret_keys['host']}:{secret_keys['port']}/{secret_keys['dbname']}"
    
    
    def query(self, query:str = ''):
        self.query_string = query

        return self

    def fetch_json(self):
      pass