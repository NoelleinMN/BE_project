import boto3
from boto3.dynamodb.conditions import Key

# boto3 is the AWS SDK library for Python.
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('Branch')

# When making a Query API call, we use the KeyConditionExpression parameter to specify the hash key on which we want to query.
# We're using the Key object from the Boto3 library to specify that we want the attribute name ("branchId")
# to equal "818beb63-9a78-423b-9b28-5f5e0d0824f6" by using the ".eq()" method.
resp = table.query(KeyConditionExpression=Key('branchId').eq('818beb63-9a78-423b-9b28-5f5e0d0824f6'))

print("The query returned the following items:")
for item in resp['Items']:
    print(item)
