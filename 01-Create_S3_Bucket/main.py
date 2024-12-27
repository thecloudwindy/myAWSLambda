import json
import boto3
import random

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    # Tạo tên bucket mặc định với dãy số ngẫu nhiên 6 chữ số
    random_suffix = ''.join(str(random.randint(0, 9)) for _ in range(6))
    default_bucket_name = f's3bucket-{random_suffix}'

    bucket_name = event.get('bucket_name', default_bucket_name)

    try:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}
        )
        return {
            'statusCode': 200,
            'body': json.dumps(f"Bucket '{bucket_name}' đã được tạo thành công!")
        }
    except Exception as e: 
        return {
            'statusCode': 400,
            'body': json.dumps(f"Lỗi khi tạo bucket: {e}")
        }
