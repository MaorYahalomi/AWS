import boto3
import json

with open('..\\config.json') as f:
   data = json.load(f)

session = boto3.Session(
    aws_access_key_id=data["aws_access_key_id"],
    aws_secret_access_key=data["aws_secret_access_key"])

ec2 = session.resource('ec2',region_name='us-east-2')
instance1 = ec2.Instance('i-06280b0a82c1bc1c9')
instance1.start()
instance2 = ec2.Instance('i-0b937a7b63f78abf2')
instance2.start()

print("Starting Ec2 instances..")

