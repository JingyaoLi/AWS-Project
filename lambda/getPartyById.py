import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # TODO implement
    event = event['params']['querystring']

    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Party')
    party = ''
    response = table.query(KeyConditionExpression=Key('id').eq(event['partyId']))
    if response['Count'] == 1:
        party = response['Items'][0]
        party['relation'] = False
        if party['hostEmail'] == event['userEmail']:
            party['relation'] = True
        ratingTable = dynamodb.Table('Rating')
        rates = ratingTable.query(KeyConditionExpression=Key('partyid').eq(event['partyId']))
        print rates
        if rates['Count'] > 0:
            count = rates['Count']
            sum = 0
            for i in rates['Items']:
                sum += float(i['ratingpoints'])
            party['rate'] = sum / count
        
        AttendTable = dynamodb.Table('Attend')
        party['status'] = False
        attendparty = AttendTable.query(
            KeyConditionExpression=Key('partyId').eq(event['partyId'])
        )
        party['number'] = attendparty['Count']
        
        attends = AttendTable.query(
            KeyConditionExpression=Key('partyId').eq(event['partyId'])&Key('guestEmail').eq(event['userEmail'])
        )
        party['attendPeople'] = []
        if attends['Count'] == 1:
            party['status'] = True
        if party['status'] or party['relation']:
            userTable = dynamodb.Table('User')
            attendlist = attendparty['Items']
            count = 0;
            for i in attendlist:
                attendemail = i['guestEmail']
                user = userTable.query(
                    KeyConditionExpression=Key('email').eq(attendemail)
                )
                if user['Count'] == 1:
                    guest = {}
                    guest['name'] = user['Items'][0]['name']
                    guest['gender'] = user['Items'][0]['gender']
                    guest['email'] = user['Items'][0]['email']
                    party['attendPeople'].append(guest)
         
        Category = dynamodb.Table('Category')
        temp = Category.query(
            KeyConditionExpression=Key('partyId').eq(event['partyId'])
        )
        party["category"] = []
        for i in temp["Items"]:
            party["category"].append(i["category"])
            
    return {
        'statusCode': 200,
        'body': party
    }
