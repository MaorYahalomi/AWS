import boto3
import json

with open('..\\config.json') as f:
   data = json.load(f)

session = boto3.Session(
    aws_access_key_id=data["aws_access_key_id"],
    aws_secret_access_key=data["aws_secret_access_key"])

ec2 = session.client('ec2', region_name='us-east-2')
All_inst_dict = ec2.describe_instances()

for dict_index in range(len(All_inst_dict["Reservations"])):
    if len(All_inst_dict["Reservations"][dict_index]["Instances"]) > 1:
        for instance_index in range(len(All_inst_dict["Reservations"][dict_index]["Instances"])):
            for tag_index in range(len(All_inst_dict["Reservations"][dict_index]["Instances"][instance_index]["Tags"])):
                if All_inst_dict["Reservations"][dict_index]["Instances"][instance_index]["Tags"][tag_index]["Key"] == "Name":
                              print(All_inst_dict["Reservations"][dict_index]["Instances"][instance_index]["Tags"][tag_index]["Value"])

    else:
        for tag_index in range(len(All_inst_dict["Reservations"][dict_index]["Instances"][0]["Tags"])):
            if All_inst_dict["Reservations"][dict_index]["Instances"][0]["Tags"][tag_index]["Key"] == "Name":
                print(All_inst_dict["Reservations"][dict_index]["Instances"][0]["Tags"][tag_index]["Value"])
       
