import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    # TODO implement
    event = event['params']['querystring']
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    followtable = dynamodb.Table('Follow')
    response = followtable.query(
        KeyConditionExpression=Key('fromEmail').eq(event['userEmail'])
    )
    
    friends = []
    for item in response["Items"]:
        friends.append(item["toEmail"])
    
    
    discovertable = dynamodb.Table('Discover')
    res = []
    for friendEmail in friends:
        response = discovertable.query(
            KeyConditionExpression=Key('userEmail').eq(friendEmail)
        )
        for item in response["Items"]:
            res.append(item)
    
    
    
    
    sortedRes = sorted(res, key=lambda x: x["eventTime"], reverse=True)
    
    return {
        'statusCode': 200,
        'body': sortedRes
    }
