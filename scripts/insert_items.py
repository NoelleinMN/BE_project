import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('Branch')

with table.batch_writer() as batch:
    batch.put_item(Item={"branchId": "818beb63-9a78-423b-9b28-5f5e0d0824f6", "crmId": "00Q4x000008tONdEAM"})

    batch.put_item(Item={"branchId": "89b626c1-4623-4860-8f79-c21af04d63ee", "crmId": "00Q4x000008tOuhEAE"})

    batch.put_item(Item={"branchId": "aece63bb-cd2e-46bf-93e4-005d25882e28", "crmId": "00Q4x000008tEGxEAM"})

