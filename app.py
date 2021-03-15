from aws_cdk import core
from data_platform.data_lake.stack import DataLakeStack
from data_platform.common_stack import CommonStack
from data_platform.redshift.stack import RedshiftStack

app = core.App()
data_lake = DataLakeStack(app)
common_stack = CommonStack(app)
redshift = RedshiftStack(app, data_lake_raw=data_lake.data_lake_raw_bucket, data_lake_processed=data_lake.data_lake_processed_bucket, common_stack=common_stack)


app.synth()
