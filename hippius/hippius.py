
import subprocess
import os

class Hippius:
    def __init__(self, mnemonic):
        self.mnemonic = mnemonic
        
    def upload(self, file_path):
        try:
            if not os.path.exists(file_path):
                raise Exception(f"File not found: {file_path}")
                
            # Run the hippius CLI command
            result = subprocess.run(['hippius', 'upload', file_path], 
                                 env={'HIPPIUS_MNEMONIC': self.mnemonic},
                                 capture_output=True,
                                 text=True)
            
            if result.returncode != 0:
                raise Exception(f"Upload failed: {result.stderr}")
                
            return result.stdout.strip()
                
        except Exception as e:
            raise Exception(f"Upload error: {str(e)}")
