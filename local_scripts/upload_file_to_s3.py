import boto3
import os


s3 = boto3.client('s3')
with open(os.path.abspath("./files/events.gz"), "rb") as f:
    print('Uploading file')
    s3.upload_fileobj(f, "s3-juanarmond-data-platform-develop-data-lake-raw", "events")
    print('Upload Done')
