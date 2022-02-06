import json
import boto3
import logging
from feb_2022_attempt.custom_encoder import CustomEncoder

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodbTableName = 'branch_customers_feb'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(dynamodbTableName)

getMethod = 'GET'
postMethod = 'POST'
patchMethod = 'PATCH'
deleteMethod = 'DELETE'
healthPath = '/health'
customerPath = '/customer'
customersPath = '/customers'

def lambda_handler(event, context):
  logger.info(event)
  httpMethod = event['httpMethod']
  path = event['path']
  if httpMethod == getMethod and path == healthPath:
    response = buildResponse(200)
  elif httpMethod == getMethod and path == customerPath:
    repsonse = getCustomer(event['queryStringParamaters']['branchId'])
  elif httpMethod == getMethod and path == customersPath:
    response = getAllCustomers()
  elif httpMethod == postMethod and path == customerPath:
    response = createCustomer(json.loads)


def buildResponse(statusCode, body=None):
  response = {
    'statusCode': statusCode,
    'headers': {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': "*"  #will allow access if front-end URL is renamed
    }
  }
  if body is not None:
    response['body'] = json.dumps(body, cls=CustomEncoder)
  return response