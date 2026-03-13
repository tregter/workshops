import boto3

AWS_ACCESS_KEY_ID = "YOUR_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY = "YOUR_SECRET_ACCESS_KEY"
BUCKET_NAME = "your-s3-bucket-name"
OBJECT_KEY = "path/to/your/file.txt"
LOCAL_FILE_PATH = "downloaded_file.txt"

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

response = s3.get_object(Bucket=BUCKET_NAME, Key=OBJECT_KEY)
file_bytes = response['Body'].read()

with open(LOCAL_FILE_PATH, "w") as f:
    f.write(file_bytes)
