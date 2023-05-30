import os
from dotenv import load_dotenv
import boto3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

load_dotenv()

AWS_REGION = os.getenv('AWS_REGION')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/fileupload', methods=['POST'])
def file_upload():
    file = request.files['file']
    s3 = boto3.client('s3', region_name=AWS_REGION, aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY )
    s3.put_object(
        ACL="public-read",
        Bucket="python-prac",
        Body=file,
        Key=file.filename,
        ContentType=file.content_type)
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)