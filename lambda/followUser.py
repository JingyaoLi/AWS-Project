import json
import boto3
import time
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Follow')
    response = table.query(
        KeyConditionExpression = Key('fromEmail').eq(event['fromEmail']) & Key('toEmail').eq(event['toEmail'])    
    )
    if len(response['Items']) == 1:
        return {
            'statusCode': 200,
            'body': 'You have already followed him!'
        }
    
    response = table.put_item(
        Item = {
            'fromEmail': event['fromEmail'],
            'toEmail': event['toEmail'],
            'followTime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }    
    )
    
    return {
        'status': 200,
        'body': 'Follow the user successfully!'
    }