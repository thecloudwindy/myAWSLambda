import boto3 

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')

    response = ec2_client.describe_regions()

    regions = []

    for region_name in response['Regions']:
        regions.append(region_name['RegionName'])

    for region in regions:
        ec2 = boto3.resource('ec2', region_name = region)
        instance_iterator = ec2.instances.filter(
            Filters=[
                {
                    'Name': 'instance-state-name',
                    'Values': [
                        'running',
                    ]
                },
            ],
            MaxResults=123
        )

        for instance in instance_iterator:
            instance.stop()
            print("Stop Instance ID: ", instance.id)



