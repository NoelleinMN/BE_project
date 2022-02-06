import json
import boto3
import logging
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
customer = '/customer'
customers = '/customers'

def lambda_handler(event, context):
  logger.info(event)
  httpMethod = event['httpMethod']
  path = event['path']
  if httpMethod == getMethod and path == healthPath:
    response = buildResponse(200)


def buildResponse(statusCode, body=None):
  response = {
    'statusCode': statusCode,
    'headers': {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': "*"  #will allow access if front-end URL is renamed
    }
  }
  if body is not None:
    response['body'] = json.dumps(body)
  return response