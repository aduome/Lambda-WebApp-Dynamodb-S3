import json
import boto3
from time import gmtime, strftime

dynamodb = boto3.client('dynamodb')
table_name = 'your_table_name'

def lambda_handler(event, context):
    first_name = event['firstName']
    last_name = event['lastName']
    age = event['age']
    occupation = event['occupation']
    nationality = event['nationality']
    maritalstatus = event['maritalstatus']
    email = event['email']
    name = f"{first_name} {last_name}"
    
    now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

    response = dynamodb.put_item(
        TableName=table_name,
        Item={
            'ID': {'S': name},
            'LatestGreetingTime': {'S': now},
            'Age': {'N': str(age)},
            'Occupation': {'S': occupation},
            'Nationality': {'S': nationality},
            'MaritalStatus': {'S': maritalstatus},
            'Email': {'S': email}
        }
    )
    
    # Create the email message
    subject = 'Registration Confirmation'
    message = f'Dear {first_name} {last_name},\n\nThank you for registering. Your registration has been confirmed.'
    message += '\n\nRegards,\nThe Gold Grid Family'

    # Send the email using Amazon SES
    ses = boto3.client('ses')
    response = ses.send_email(
        Source='verified email',  # Replace with your email address
        Destination={'ToAddresses': [email]},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': message}}
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Confirmation email sent.')
    }
