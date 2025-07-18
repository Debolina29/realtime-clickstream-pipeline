# realtime-clickstream-pipeline
AWS Real-Time Streaming Project using Kinesis, Lambda, DynamoDB

# Real-Time Clickstream Analytics Pipeline (AWS)

## 🚀 Project Overview
This project demonstrates a real-time data engineering pipeline using AWS.

**Architecture:**
- Simulated clickstream events (user_id, timestamp, page_visited) are streamed using Python.
- Data is ingested via **Amazon Kinesis**
- Processed using **AWS Lambda**
- Stored in **Amazon DynamoDB**

## 🛠️ Technologies Used
- AWS Kinesis
- AWS Lambda (Python 3.13)
- DynamoDB
- Python (Boto3)
- CloudWatch

## 📁 Project Structure
- `simulate_clickstream.py` - Script to simulate clickstream events
- `lambda_function.py` - Lambda function to process stream and write to DynamoDB

## ✨ Author
Your Name | [LinkedIn](https://linkedin.com/in/yourname)

