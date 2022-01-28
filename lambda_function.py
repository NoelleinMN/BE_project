import json
import boto3
from botocore.exceptions import ClientError
# import uuid
import decimal

dynamo = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Branch')

GET_RAW_PATH = "/allCustomers"
NEW_RAW_PATH = "/newCustomer"
SEARCH_RAW_PATH = "/searchCustomer"
HOME_PATH = "/hi"

# get all customers
def lambda_handler(event, context):
    
    if event['rawPath'] == HOME_PATH:
        print("home request")
        
        return {
            'statusCode': 200,
            'body': json.dumps('Hello, Branch Energy!')
        }
        
    elif event['rawPath'] == GET_RAW_PATH:
        print("getCustomers request")
        response = get_items()

        return {
            'statusCode': 200,
            'body': json.dumps(response, indent=2, default=handle_decimal_type)
        }

    elif event['rawPath'] == SEARCH_RAW_PATH:
        print("searchCustomer request")
        print(event)
        branchId = event['queryStringParameters']['branchId']
        print(branchId)
        response = search_customer(branchId)
        
        return {
            'statusCode': 200,
            #'body': json.dumps('find customer')
            'body': json.dumps(response, indent=2, default=handle_decimal_type)
        }
    
    elif event['rawPath'] == NEW_RAW_PATH:
        # TO DO: Implement newCustomer add
        return {
            'statusCode': 200,
            'body': json.dumps('not working yet')
        }
    
    else:
        return {
            'statusCode': 200,
            'body': json.dumps('not right')
        }
        
def get_items():

    try:
        response = table.scan()
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response.get('Items', [])

def search_customer(branchId):

    try:
        payload = table.get_item(Key={'branchId': branchId})
        response = payload["Item"]
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response


def handle_decimal_type(obj):
    if isinstance(obj, decimal.Decimal):
        if float(obj).is_integer():
            return int(obj)
        else:
            return float(obj)
    raise TypeError