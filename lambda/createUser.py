import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    # return event
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('User')
    email = event['userEmail']
    response = table.query(
        KeyConditionExpression = Key('email').eq(email)    
    )
    if len(response['Items']) == 1:
        return {
            'statusCode': 200,
            'body': 'The user has already existed.'
        }
    respone = table.put_item(
        Item = {
            'name': event['userName'],
            'email': event['userEmail'],
            'gender': event['gender'],
            'phone_number': event['phone_number']
        }    
    )
    
    return {
        'statusCode': 200,
        'body': 'create user successfully!'
    }
