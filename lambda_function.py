import json
import boto3
import base64
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ClickstreamEvents')

def lambda_handler(event, context):
    for record in event['Records']:
        # Decode base64 data first
        decoded_data = base64.b64decode(record['kinesis']['data'])
        payload = json.loads(decoded_data, parse_float=Decimal)
        
        user_id = int(payload["user_id"])
        timestamp = int(payload["timestamp"])
        page_visited = payload["page_visited"]
        
        # Optional: derive page category
        page_category = "info" if "about" in page_visited or "contact" in page_visited else "action"

        # Insert into DynamoDB
        table.put_item(
            Item={
                'user_id': user_id,
                'timestamp': timestamp,
                'page_visited': page_visited,
                'page_category': page_category
            }
        )
        
    return {'statusCode': 200, 'body': 'Records processed.'}
