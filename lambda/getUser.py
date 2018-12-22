import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    event = event['params']['querystring']
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('User')
    response = table.get_item(
        Key = {
            'email': event['email']
        }    
    )
    
    # response = table.query(
    #     KeyConditionExpression=Key('email').eq(event['email'])
    # )
    return {
        'statusCode': 200,
        'body': response['Item']
    }
