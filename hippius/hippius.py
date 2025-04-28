
import requests
import json

class Hippius:
    def __init__(self, mnemonic):
        self.mnemonic = mnemonic
        self.api_url = "https://api.hippius.io/v1/upload"  # Replace with actual API endpoint

    def upload(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                files = {'file': file}
                headers = {
                    'Authorization': f'Bearer {self.mnemonic}'
                }
                
                response = requests.post(
                    self.api_url,
                    files=files,
                    headers=headers
                )
                
                if response.status_code == 200:
                    return response.json().get('cid')
                else:
                    raise Exception(f"Upload failed: {response.text}")
                    
        except Exception as e:
            raise Exception(f"Upload error: {str(e)}")
