import json
import boto3
import time
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    # partyTable = dynamodb.Table('Party')
    # response = partyTable.query(
    #     KeyConditionExpression = Key('id').eq(event['partyId'])    
    # )
    # if response['Items'][0]['number'] == response['Items'][0]['maxNumber']:
    #     return {
    #         'statusCode': 200,
    #         'body': "The number of the party is full!"
    #     }
    
    attendTable = dynamodb.Table('Attend')
    respone = attendTable.put_item(
        Item = {
            'partyId': event['partyId'],
            'guestEmail': event['userEmail'],
            'attendTime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }    
    )
    
    userTable = dynamodb.Table('User')
    response = userTable.get_item(
        Key = {
            'email': event['userEmail']
        }    
    )
    userName = response['Item']['name']
    
    partyTable = dynamodb.Table('Party')
    response = partyTable.query(
        KeyConditionExpression = Key('id').eq(event['partyId'])
    )
    partyName = response['Items'][0]['partyName']
    hostEmail = response['Items'][0]['hostEmail']
    
    
    discoverTable = dynamodb.Table('Discover')
    content = userName + " joined the party '" + partyName + "'"
    response = discoverTable.put_item(
        Item = {
            'userEmail': event['userEmail'],
            'eventTime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            'partyId': event['partyId'],
            'content': content
        }    
    )
    
    response = userTable.get_item(
        Key = {
            'email': hostEmail
        }    
    )
    phone_number = response['Item']['phone_number']
    
    client = boto3.client('sns')
    content = userName + " has joined your party " + partyName + " just now. You could check it online."
    snsresponse = client.publish(
        PhoneNumber = '+1' + phone_number,
        Message= content
    )
    
    
    return {
        'statusCode': 200,
        'body': "Attend the party successfully!"
    }
