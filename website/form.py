import boto3
from django.http import HttpResponse
from config import AWS_ACCESS_KEY, AWS_SECRET_KEY

def send_email(name, email, subject, message):
    client = boto3.client(
        'ses',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name='us-west-2'
    )
    response = client.send_email(
        Destination={
            'ToAddresses': [
                'yadavpriti0210@gmail.com',
            ],
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': message,
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': subject,
            },
            'Name': {
                'Charset': 'UTF-8',
                'Data': name,
            },
        },
        Source= email,
    )
