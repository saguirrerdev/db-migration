import redshift_connector
import utils.secrets
import os

class RedshiftConnection:
  
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
        
        secret_keys = utils.secrets.get_secret(os.getenv("DB_SECRET_KEY_NAME"))
        
        conn = redshift_connector.connect(
            host=self.host,
            database=self.dbname,
            port=self.port,
            user=secret_keys["username"],
            password=secret_keys["password"]
        )

        self.conn = conn

        return self
    
    
    def query(self, query:str = ''):
        self.query_string = query

        return self

    def fetch_json(self):
        if not self.conn:
            raise Exception("Failed connection")
        
        if not self.query:
            raise Exception("SQL Query not provided")
        
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(self.query_string)
            results = cursor.fetchall()
            cursor.close()
        
        return results
    