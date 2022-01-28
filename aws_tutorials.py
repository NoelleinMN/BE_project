import json
import boto3

print('Loading function')
dynamo = boto3.client('dynamodb')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.

    To scan a DynamoDB table, make a GET request with the TableName as a
    query string parameter. To put, update, or delete an item, make a POST,
    PUT, or DELETE request respectively, passing in the payload to the
    DynamoDB API as a JSON body.
    '''
    #print("Received event: " + json.dumps(event, indent=2))

    operations = {
        'DELETE': lambda dynamo, x: dynamo.delete_item(**x),
        'GET': lambda dynamo, x: dynamo.scan(**x),
        'POST': lambda dynamo, x: dynamo.put_item(**x),
        'PUT': lambda dynamo, x: dynamo.update_item(**x),
    }

    operation = event['httpMethod']
    if operation in operations:
        payload = event['queryStringParameters'] if operation == 'GET' else json.loads(event['body'])
        return respond(None, operations[operation](dynamo, payload))
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))

# def lambda_handler(event, context):
#     print(event)
#     if event['rawPath'] == GET_RAW_PATH:
#         print("GetCustomer request")
#         branchId = event['queryStringParameters']['branchId']
#         print("Received request with branchId= " + branchId)
#         return { "branchId": "818beb63-9a78-423b-9b28-5f5e0d0824f6" }
#     # elif event['rawPath'] == ADD_RAW_PATH:
#     #     print("Received createCustomer request")
#     #     decodedBody = json.loads(event['body'])
#     #     branchId = decodedBody['branchId']
#     #     return { "branchId": str(uuid.uuid1())}
#     #     print("Start Request for AddCustomer")
#     else:
#         print("Method not permitted")
    
    
       # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }