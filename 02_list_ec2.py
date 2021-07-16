'''
Created on 13 mar. 2021
A test to access an "aws credentials" account and describe its instances.
@author: jframosg
'''
import boto3
import os

os.environ['AWS_PROFILE'] = 'YOUR_AWS_PROFILE'
os.environ['AWS_DEFAULT_REGION'] = 'YOUR_AWS_DEFAULT_REGION'

if  __name__ =='__main__':
    i=0
    ec2 = boto3.client('ec2', str(os.environ['AWS_DEFAULT_REGION']))
    response = ec2.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print(instance)
            i+=1
    print(i, "instances.")