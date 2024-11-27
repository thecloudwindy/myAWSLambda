import json
import boto3
import random

client = boto3.client('s3')
def lambda_handler(event, context):
    createS3Bucket = client.create_bucket(
        Bucket = f"mybucket-{random.randint(1000, 9999)}",
        CreateBucketConfiguration = {
            'LocationConstraint': 'ap-southeast-1' 
        }
    )
    print(createS3Bucket)

# Nếu bạn đang ở Region: us-east-1 thì không cần chỉ định nơi tạo S3 nếu chỉ định sẽ bị lỗi, chỉ định ở một Region khác thì ok
