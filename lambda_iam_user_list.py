import boto3
import json

def lambda_handler(event, context):
    # Create an IAM client
    iam = boto3.client('iam')

    # List all IAM users
    response = iam.list_users()

    # Extract the user names
    user_names = [user['UserName'] for user in response['Users']]

    # Build the response object
    response = {
        "statusCode": 200,
        "body": json.dumps(user_names)
    }

    return response
  
  
  
  #Configure Test Event#
  
{
  "headers": {
    "Accept": "application/json"
  },
  "httpMethod": "GET",
  "path": "/users",
  "queryStringParameters": {},
  "requestContext": {
    "identity": {
      "userAgent": "curl/7.54.0"
    }
  },
  "body": ""
}
