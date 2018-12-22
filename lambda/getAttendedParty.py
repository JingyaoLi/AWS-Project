import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Attend')
    response = table.query(
        IndexName='guestEmail-index',
        KeyConditionExpression=Key('guestEmail').eq(event['params']['querystring']['guestEmail'])
    )
    
    res = []
    table = dynamodb.Table('Party')
    Category = dynamodb.Table('Category')
    for item in response["Items"]:
        parties = table.query(
            KeyConditionExpression=Key('id').eq(item['partyId'])
        )
        
        for party in parties["Items"]:
            temp = Category.query(
                KeyConditionExpression=Key('partyId').eq(party['id'])
            )
            party["category"] = []
            for i in temp["Items"]:
                party["category"].append(i["category"])
            res.append(party)
            
    
    # TODO implement
    return {
        'statusCode': 200,
        'partyLists': res
    }
