import json
import uuid
import boto3
import time
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Rating')
    respone = table.put_item(
        Item = {
            'partyid': event['partyid'],
            'userEmail': event['userEmail'],
            'ratingpoints': str(event['ratingpoints']),
            'ratingreview': event['ratingreview'],
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
        KeyConditionExpression = Key('id').eq(event['partyid'])
    )
    partyName = response['Items'][0]['partyName']
    hostEmail = response['Items'][0]['hostEmail']
    
    discoverTable = dynamodb.Table('Discover')
    content = userName + " rated " + str(event['ratingpoints']) + " star to the party '" + partyName + "' and said " + str(event['ratingreview'])
    response = discoverTable.put_item(
        Item = {
            'userEmail': event['userEmail'],
            'eventTime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            'partyId': event['partyid'],
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
    content = "The party " + partyName + " you hosted was rated just now. You could check it online."
    snsresponse = client.publish(
        PhoneNumber = '+1' + phone_number,
        Message= content
    )
    
    return {
        'statusCode': 200,
        'body': 'Rate successfully!'
    }
