import boto3
import json

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        bucket_lists = []
        response = s3_client.list_buckets()
        for bucket in response['Buckets']:
            bucket_lists.append(bucket['Name'])
        return {
                'ststusCode' : 200,
                'body': json.dumps(bucket_lists)
        }

    except Exception as e:
        return {
            'ststusCode' : 500,
            'body': json.dumps(f"Lỗi khi liệt kê S3 Buckets: => {e}")
        }
