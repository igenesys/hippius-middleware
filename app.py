
from flask import Flask, request, jsonify
from flask_cors import CORS
from hippius import Hippius
import os

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        if 'file' not in request.files or 'mnemonic' not in request.form:
            return jsonify({'error': 'Missing file or mnemonic'}), 400

        file = request.files['file']
        mnemonic = request.form['mnemonic']
        
        # Initialize Hippius with mnemonic
        hippius = Hippius(mnemonic=mnemonic)
        
        # Save file temporarily
        temp_path = f"/tmp/{file.filename}"
        file.save(temp_path)
        
        # Upload to Hippius
        cid = hippius.upload(temp_path)
        
        # Clean up
        os.remove(temp_path)
        
        return jsonify({'cid': cid})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
