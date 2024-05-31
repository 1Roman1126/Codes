from datetime import date
import boto3
from nepseRequestParser import nepseReqParser
from responseParser import responseParser
import json

def lambda_handler(event, context):
    _date = date.today()
    bucket_name = 'minorproject-forbes'  # Your S3 bucket name
    local_path = f"/tmp/nepse_data_{_date}.csv"  # Path to save the file locally
    
    try:
        response = nepseReqParser(_date)
        if len(response.text) < 300:
            print("NO DATA AS OF TODAY DUE TO MARKET CLOSED!")
        else:
            responseParser(response, _date, bucket_name, local_path)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        # Optionally, to see what's in the event that triggered the Lambda:
        print(f"Event received: {json.dumps(event)}")
        raise e

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function executed successfully!')
    }
