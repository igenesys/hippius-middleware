
import subprocess
import json

class Hippius:
    def __init__(self, mnemonic):
        self.mnemonic = mnemonic

    def upload(self, file_path):
        try:
            # Execute hippius CLI command with the mnemonic
            cmd = ['hippius', '--mnemonic', self.mnemonic, 'upload', file_path]
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                # Parse the CID from the CLI output
                # Assuming the CLI returns JSON or a parseable format
                return result.stdout.strip()
            else:
                raise Exception(f"Upload failed: {result.stderr}")
                
        except Exception as e:
            raise Exception(f"Upload error: {str(e)}")
