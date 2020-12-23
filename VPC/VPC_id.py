import boto3
import json

with open('..\\..\\config.json') as f:
   data = json.load(f)

session = boto3.Session(
    aws_access_key_id=data["aws_access_key_id"],
    aws_secret_access_key=data["aws_secret_access_key"])

ec2 = session.resource('ec2',region_name='us-east-2')
vpc = ec2.Vpc('vpc-07236283060448f8a')

print(f' VPC ID #{vpc.id}')
