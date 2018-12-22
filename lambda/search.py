import json
import boto3
import time
from boto3.dynamodb.conditions import Key, Attr
import requests
from math import sin, cos, sqrt, atan2, radians


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    categoryTable = dynamodb.Table('Category')
    partyTable = dynamodb.Table('Party')
    event = event['params']['querystring']
    # print time.localtime()
    
    
    if event['type'] == 'name':
        name = event['keyword']
        # print name
        if name == "":
            response = partyTable.scan(
                Limit = 100,
                FilterExpression=Attr('startTime').gt(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            )
        else:
            response = partyTable.scan(
                FilterExpression=Attr('partyName').contains(name) & Attr('startTime').gt(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            )
        parties = response['Items']
    
        for party in parties:
            temp = categoryTable.query(
                KeyConditionExpression=Key('partyId').eq(party['id'])
            )
            party["category"] = []
            for i in temp["Items"]:
                party["category"].append(i["category"])
        
        return {
            'statusCode': 200,
            'partyLists': parties
        }
    
    
    
    if event['type'] == 'category':
        type = event['keyword']
        response = categoryTable.query(
            IndexName='category-index',
            KeyConditionExpression=Key('category').eq(type)
        )
        
        parties = response['Items']
        
        res = []
        for party in parties:
            response = partyTable.query(
                KeyConditionExpression=Key('id').eq(party['partyId']),
                FilterExpression=Attr('startTime').gt(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            )
            if len(response['Items']) == 0:
                continue
            currParty = response['Items'][0]
            temp = categoryTable.query(
                KeyConditionExpression=Key('partyId').eq(currParty['id'])    
            )
            currParty['category'] = []
            for i in temp['Items']:
                currParty['category'].append(i['category'])
            res.append(currParty)
        return {
            'statusCode': 200,
            'partyLists': res
        }
        
        
    if event['type'] == 'location':
        urlcomp = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query='+event['keyword']+'&language=en&key=AIzaSyBR0Dg4uNylIw-i4g38kvOxV3Kf8uOOAQQ'
        headers = {"Content-Type": "application/json"}
        placeres = requests.get(urlcomp, headers=headers).json()
        lat = placeres['results'][0]["geometry"]["location"]["lat"]
        lng = placeres['results'][0]["geometry"]["location"]["lng"]
        response = partyTable.scan(
                Limit = 100,
                FilterExpression=Attr('startTime').gt(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            )
        
        res = []
        for item in response["Items"]:
            dis = caldistance(lat,lng, float(item['lat']), float(item['lng']))
            if dis < 1:
                res.append(item)
        
        return {
            'statusCode': 200,
            'partyLists': res
        }
    

def caldistance(la1,lo1,la2,lo2):
    R = 6373.0

    lat1 = radians(la1)
    lon1 = radians(lo1)
    lat2 = radians(la2)
    lon2 = radians(lo2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance