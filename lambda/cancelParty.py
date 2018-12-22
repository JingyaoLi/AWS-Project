import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Attend')
    response = table.delete_item(
        Key={
            'partyId': event['partyId'],
            'guestEmail': event['userEmail']
        }
    )
    return {
        'statusCode': 200,
        'body': response
    }
