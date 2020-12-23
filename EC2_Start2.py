import boto3
session = boto3.Session(aws_access_key_id="xx", aws_secret_access_key="xx")

ec2 = session.resource('ec2',region_name='us-east-1',use_ssl=False)
instance = ec2.Instance('i-0dcdb13da50d530b0')
instance.start()
print("ssdfa")
