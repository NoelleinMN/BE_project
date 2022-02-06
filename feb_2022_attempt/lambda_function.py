import json
from urllib import response
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
    response = getCustomer(event['queryStringParamaters']['branchId'])
  elif httpMethod == getMethod and path == customersPath:
    response = getAllCustomers()
  elif httpMethod == postMethod and path == customerPath:
    response = createCustomer(json.loads(event['body']))
  elif httpMethod == patchMethod and path == customerPath:
    requestBody = json.loads(event['body'])
    response = updateCustomer(requestBody['branchId'], requestBody['updateKey'], requestBody['updateValue'])
  elif httpMethod == deleteMethod and path == customerPath:
    requestBody = json.loads(event['body'])
    response = deleteCustomer(requestBody['branchId'])
  else:
    response = buildResponse(404, 'Not Found')
  
  return response

def getCustomer(branchId):
  try:
    response = table.get_item(
      Key={
        'branchId': branchId
      }
    )
    if 'Item' in response:
      return buildResponse(200, response['Item'])
    else:
      return buildResponse(404, {'Message': 'branchId: %s not found' % branchId})
  except:
    logger.exception('An exception has occured.')

def getAllCustomers():
  try:
    response = table.scan()
    result = response['Item']

    while 'LastEvaluatedKey' in response:
      response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
      result.extend(response['Item'])

    body = {
      'cusomters': response
    }
    return buildResponse(200, body)
  except:
    logger.exception('An exception has occured.')

def createCustomer(requestBody):
  try:
    table.put_item(Item=requestBody)
    body = {
      'Operation': 'SAVE',
      'Message': 'SUCCESS',
      'Item': requestBody
    }
    return buildResponse(200, body)
  except:
    logger.exception('An exception has occured.')

def updateCustomer(branchId, updateKey, updateValue):
  try:
    response = table.update_item(
      Key={
        'branchId': branchId
      },
      UpdateExpression='set %s = :value' % updateKey,
      ExpressionAttributeValues={
        ':value': updateValue
      },
      ReturnValues='UPDATED_NEW'
    )
    body = {
      'Operation': 'SAVE',
      'Message': 'SUCCESS',
      'UpdatedAttributes': response
    }
    return buildResponse(200, body)
  except:
    logger.exception('An exception has occured.')

def deleteCustomer(branchId):
  try:
    response = table.delete_item(
      Key={
        'branchId': branchId
      },
      ReturnValues='ALL_OLD'
    )
    body = {
      'Operation': 'SAVE',
      'Message': 'SUCCESS',
      'deletedItem': response
    }
    return buildResponse(200, body)
  except:
    logger.exception('An exception has occured.')

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