from aws_cdk import core
from data_platform.data_lake.stack import DataLakeStack
import local_scripts.upload_file_to_s3 as upload_file_to_s3

app = core.App()
data_lake = DataLakeStack(app)
upload_file = upload_file_to_s3.upload_file()
app.synth()
