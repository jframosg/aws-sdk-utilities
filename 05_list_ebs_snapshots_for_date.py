'''
Created on 11 jul. 2021
List the ebs snapshots done in a date
@author: jframosg
'''
import boto3
import os
from datetime import datetime


my_date = '2021-07-11'
os.environ['AWS_PROFILE'] = 'YOUR_AWS_PROFILE'
os.environ['AWS_DEFAULT_REGION'] = 'YOUR_AWS_DEFAULT_REGION'

if  __name__ =='__main__':
    d = datetime.strptime(my_date,'%Y-%m-%d')
    d = d.date()
    ec2 = boto3.client('ec2', str(os.environ['AWS_DEFAULT_REGION']))
    response = ec2.describe_snapshots(OwnerIds=['self'])
    print('Volumes with snapshot done in', my_date, ':')
    for snapshot in response['Snapshots']:
        if snapshot['StartTime'].date() == d:
            print(snapshot['VolumeId'], '-->', snapshot)

    
