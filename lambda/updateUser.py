import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('User')
    email = event['email']
    name = event['name']
    gender = event['gender']
    birthday = event['birthday']
    hobby = event['hobby']
    phone_number = event['phone_number']
    respone = table.put_item(
        Item = {
            'email': email,
            'name': name,
            'gender': gender,
            'birthday': birthday,
            'hobby': hobby,
            'phone_number': phone_number
        }    
    )
    
    client = boto3.client('sns')
    snsresponse = client.publish(
        PhoneNumber = '+1' + phone_number,
        Message= "You have updated your user information successfully."
    )
    
    return {
        'statusCode': 200,
        'body': 'update successfully!'
    }
