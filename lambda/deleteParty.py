import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    # TODO implement
    
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    attendTable = dynamodb.Table('Attend')
    PartyTable = dynamodb.Table('Party')
    RatingTable =  dynamodb.Table('Rating')
    CategoryTable = dynamodb.Table('Category')
    UserTable = dynamodb.Table('User')
    DiscoverTable = dynamodb.Table('Discover')
    
    response = PartyTable.query(
        KeyConditionExpression = Key('id').eq(event['partyId']) 
    )
    partyName = response['Items'][0]['partyName']
    
    
    response = attendTable.query(
        KeyConditionExpression=Key('partyId').eq(event['partyId'])
    )
    
    client = boto3.client('sns')
    for item in response["Items"]:
        tmp = UserTable.get_item(
            Key = {
                'email': item['guestEmail']
            }    
        )
        snsresponse = client.publish(
            PhoneNumber = '+1' + tmp['Item']['phone_number'],
            Message= partyName + " has been deleted by host. Please check it online."
        )
    
    
    for item in response["Items"]:
        delete_item(attendTable, 'partyId', 'guestEmail', item['partyId'], item['guestEmail'])
        
    
    response = CategoryTable.query(
        KeyConditionExpression=Key('partyId').eq(event['partyId'])
    )
    
    for item in response["Items"]:
        delete_item(CategoryTable, 'partyId', 'category', item['partyId'], item['category'])
    
    
    response = DiscoverTable.query(
        IndexName='partyId-index',
        KeyConditionExpression=Key('partyId').eq(event['partyId'])
    )
    
    for item in response["Items"]:
        delete_item(DiscoverTable, 'userEmail', 'eventTime', item['userEmail'], item['eventTime'])
        
    response = RatingTable.query(
        KeyConditionExpression=Key('partyid').eq(event['partyId'])
    )
    
    for item in response["Items"]:
        delete_item(RatingTable, 'partyid', 'userEmail', item['partyid'], item['userEmail'])
        
    response = PartyTable.query(
        KeyConditionExpression=Key('id').eq(event['partyId'])
    )
    
    for item in response["Items"]:
        delete_item(PartyTable, 'id', 'hostEmail', item['id'], item['hostEmail'])

    
    
    
    return {
        'statusCode': 200,
        'body': 'Delete party successfully!'
    }


def delete_item(table, rangename, sortname, key1, key2):
    respone = table.delete_item(
        Key={
            rangename: key1,
            sortname: key2
        }
    )