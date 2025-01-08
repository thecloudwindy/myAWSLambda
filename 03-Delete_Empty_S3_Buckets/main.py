import boto3
import json

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = event.get('bucket_name')
    try:
        response = s3_client.delete_bucket(
            Bucket=bucket_name,
        )
        return {
                'ststusCode' : 200,
                'body': json.dumps(response)
        }

    except Exception as e:
        return {
            'ststusCode' : 500,
            'body': json.dumps(f"Lỗi khi thực hiện xóa S3 Buckets: => {e}")
        }
