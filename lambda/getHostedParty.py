import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Party')
    response = table.query(
        IndexName='hostEmail-index',
        KeyConditionExpression=Key('hostEmail').eq(event['params']['querystring']['hostEmail'])
    )
    
    parties = response["Items"]
    
    Category = dynamodb.Table('Category')
    
    for party in parties:
        temp = Category.query(
            KeyConditionExpression=Key('partyId').eq(party['id'])
        )
        party["category"] = []
        for i in temp["Items"]:
            party["category"].append(i["category"])
    
    # TODO implement
    return {
        'statusCode': 200,
        'partyLists': parties
    }
