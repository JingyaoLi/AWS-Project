import json
import uuid
import time
import boto3
import requests


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Party')
    id = str(uuid.uuid4())
    
    urlcomp = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query='+event['address']+'&language=en&key=AIzaSyBR0Dg4uNylIw-i4g38kvOxV3Kf8uOOAQQ'
    headers = {"Content-Type": "application/json"}
    placeres = requests.get(urlcomp, headers=headers).json()
    
    respone = table.put_item(
        Item = {
            'id': id,
            'partyName': event['name'],
            'hostEmail': event['hostEmail'],
            'maxNumber': event['maxNumber'],
            'discription': event['discription'],
            'startTime': event['startTime'],
            'endTime': event['endTime'],
            'placeId': placeres['results'][0]["place_id"],
            'placeName': placeres['results'][0]["name"],
            'address': placeres['results'][0]["formatted_address"],
            'lat': str(placeres['results'][0]["geometry"]["location"]["lat"]),
            'lng': str(placeres['results'][0]["geometry"]["location"]["lng"])
        }    
    )
    categoryTable = dynamodb.Table('Category')
    for category in event['category']:
        response = categoryTable.put_item(
            Item = {
                'partyId': id,
                'category': category
        } 
    )
    
    userTable = dynamodb.Table('User')
    response = userTable.get_item(
        Key = {
            'email': event['hostEmail']
            
        }    
    )
    userName = response['Item']['name']
    # print userName
    
    discoverTable = dynamodb.Table('Discover')
    content = userName + " created a new party '" + event['name'] + "'"
    response = discoverTable.put_item(
        Item = {
            'userEmail': event['hostEmail'],
            'eventTime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            'partyId': id,
            'content': content
        }    
    )
    return {
        'statusCode': 200,
        'body': "success!"
    }
