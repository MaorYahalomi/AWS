import boto3
import json

with open('..\\..\\config.json') as f:
   data = json.load(f)

session = boto3.Session(
    aws_access_key_id=data["aws_access_key_id"],
    aws_secret_access_key=data["aws_secret_access_key"])


ec2 = session.resource('ec2',region_name='us-east-2',use_ssl=False)
network_interface = ec2.NetworkInterface('eni-0a476183cb0fd2628')

nl = '\n'
print(f' interface ID:{network_interface.id}{nl}')
print(f' interface Status:{network_interface.status}{nl}')
print(f' VPC ID:{network_interface.vpc_id}{nl}')
print(f' Subnet ID:{network_interface.subnet_id}{nl}')




#status = network_interface.status
IP_addresses = network_interface.private_ip_addresses
Public_ip = IP_addresses[0]["Association"]["PublicIp"]
Private_ip = IP_addresses[0]["PrivateIpAddress"]


print(f' Private Ip:{Private_ip}{nl} Public IP:{Public_ip}')

