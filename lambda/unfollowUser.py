import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Follow')
    
    response = table.get_item(
        Key = {
            'fromEmail': event['fromEmail'],
            'toEmail': event['toEmail']
        }    
    )
    # print response.has_key['Item']
    if 'Item' not in response.keys():
        return {
            'statusCode': 200,
            'body': 'You have not followed him!'
        }
    respone = table.delete_item(
        Key={
            'fromEmail': event['fromEmail'],
            'toEmail': event['toEmail']
        }
    )
    return {
        'statusCode': 200,
        'body': 'Unfollow successfully!'
    }
