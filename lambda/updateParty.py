import json
import boto3
import requests
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Party')
    
    urlcomp = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query='+event['address']+'&language=en&key=AIzaSyBR0Dg4uNylIw-i4g38kvOxV3Kf8uOOAQQ'
    headers = {"Content-Type": "application/json"}
    placeres = requests.get(urlcomp, headers=headers).json()
    
    
    respone = table.update_item(
        Key = {
            'id': event['partyId'],
            'hostEmail': event['hostEmail']
        },
        UpdateExpression = "SET partyName = :partyName, discription = :discription, startTime = :startTime, endTime = :endTime, placeId = :placeId, placeName = :placeName, address = :address, lat = :lat, lng = :lng",
        ExpressionAttributeValues = { 
            ':partyName': event['name'],
            ':discription': event['discription'],
            ':startTime': event['startTime'],
            ':endTime': event['endTime'],
            ':placeId': placeres['results'][0]["place_id"],
            ':placeName': placeres['results'][0]["name"],
            ':address': placeres['results'][0]["formatted_address"],
            ':lat': str(placeres['results'][0]["geometry"]["location"]["lat"]),
            ':lng': str(placeres['results'][0]["geometry"]["location"]["lng"])
        },
        ReturnValues="UPDATED_NEW"
    )
    
    userTable = dynamodb.Table('User')
    response = userTable.get_item(
        Key = {
            'email': event['hostEmail']
        }    
    )
    userName = response['Item']['name']
    
    client = boto3.client('sns')
    content = "The party " + event['name'] + " hosted by " + userName + " has been updated. Please check online."
    
    attendTable = dynamodb.Table('Attend')
    response = attendTable.query(
        KeyConditionExpression = Key('partyId').eq(event['partyId'])
    )
    
    for item in response['Items']:
        guestEmail = item['guestEmail']
        tmp = userTable.get_item(
            Key = {
            'email': guestEmail
            } 
        )
        snsresponse = client.publish(
            PhoneNumber = '+1' + tmp['Item']['phone_number'],
            Message= content
        )
    
    
    return {
        'statusCode': 200,
        'body': 'update successfully!'
    }
