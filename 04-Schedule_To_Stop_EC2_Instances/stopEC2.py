import boto3

def lambda_handler(event, context):
    # Liệt kê danh sách các Regions
    ec2_client = boto3.client('ec2')

    response = ec2_client.describe_regions()

    # Lấy danh sách các vùng từ response
    regions_data = response['Regions']

    # Tạo danh sách các vùng (RegionName)
    regions = []
    for region in regions_data:
        regions.append(region['RegionName'])

    # In kết quả
    # print(regions)

    #regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
    
    for region in regions:
        ec2 = boto3.resource('ec2', region_name = region)
        # Liet ke danh sach Instances co trong Region
        instances = ec2.instances.filter(
            Filters=[
                {
                    'Name': 'instance-state-name',
                    'Values': [
                        'running',
                    ]
                },
            ],
        )
        for instance in instances:
            instance.stop()
            print("Stop Instance: ", instance.id)
