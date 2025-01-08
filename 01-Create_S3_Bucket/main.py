import boto3
import random
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    random_suffix = ''.join(str(random.randint(0, 9)) for _ in range(6))
    default_bucket_name = f"s3bucket-{random_suffix}"

    bucket_name = event.get('bucket_name', default_bucket_name)

    try:
        response = s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': 'ap-southeast-2'}
        )
        return {
            'ststusCode' : 200,
            'body': json.dumps(f"Bucket {bucket_name} đã tạo thành công!")
        }

    except Exception as e:
        return {
            'ststusCode' : 400,
            'body': json.dumps(f"Lỗi khi tạo S3 Bucket: => {e}")
        }

