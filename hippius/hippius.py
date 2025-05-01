
from hippius.client import Client as HippiusClient
import os

class Hippius:
    def __init__(self, mnemonic):
        self.client = HippiusClient(mnemonic=mnemonic)
        
    def upload(self, file_path):
        try:
            if not os.path.exists(file_path):
                raise Exception(f"File not found: {file_path}")
                
            # Upload using the Python client
            cid = self.client.upload(file_path)
            return cid
                
        except Exception as e:
            raise Exception(f"Upload error: {str(e)}")
