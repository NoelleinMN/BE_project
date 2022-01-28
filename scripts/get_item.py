import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('Branch')

resp = table.get_item(Key={"branchId": "818beb63-9a78-423b-9b28-5f5e0d0824f6", "crmId": "00Q4x000008tONdEAM"})

print(resp['Item'])
