import boto3
import json
import time
import random

# Initialize Kinesis client
kinesis = boto3.client('kinesis', region_name='us-east-1')  # Replace with your region

# Sample pages a user might visit
pages = ["/home", "/about", "/product", "/contact", "/pricing"]

# Function to generate one fake click event
def generate_event():
    return {
        "user_id": random.randint(1000, 9999),          # Random user ID
        "timestamp": time.time(),                       # Current timestamp
        "page_visited": random.choice(pages)            # Random page visit
    }

# Send events in a loop
while True:
    event = generate_event()
    print("Sending:", event)
    kinesis.put_record(
        StreamName="clickstream-data",                  # Name of your stream
        Data=json.dumps(event),                         # Convert to JSON string
        PartitionKey=str(event["user_id"])              # Group events by user ID
    )
    time.sleep(1)  # Send one event per second
