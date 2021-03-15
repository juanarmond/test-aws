import boto3
import os


def upload_file():
    s3 = boto3.client('s3')
    with open(os.path.abspath("./files/events"), "rb") as f:
        s3.upload_fileobj(f, "s3-juanarmond-data-platform-develop-data-lake-raw", "events")
