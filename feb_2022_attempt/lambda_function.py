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
    response

def getAllCustomers():
  try:
    response

def createCustomer(branchId):
  try:
    response

def updateCustomer(branchId):
  try:
    response

def deleteCustomer(branchId):
  try:
    response


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