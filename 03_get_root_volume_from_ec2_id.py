'''
Created on 11 jul. 2021
A test to get EBS root volume attached from ec2 instance id
@author: jframosg
'''

import boto3
import os

os.environ['AWS_PROFILE'] = 'YOUR_AWS_PROFILE'
os.environ['AWS_DEFAULT_REGION'] = 'YOUR_AWS_DEFAULT'

if  __name__ =='__main__':
    ec2 = boto3.client('ec2', str(os.environ['AWS_DEFAULT_REGION']))
    instance_id = 'YOUR_EC2_INSTANCE_ID'
    print('Instance id = ', instance_id)
    instance = ec2.describe_instances(InstanceIds=[instance_id])
    if instance:
        instance = instance['Reservations'][0]['Instances'][0]
        root_device_name = instance['RootDeviceName']
        for volume in instance['BlockDeviceMappings']:
            if volume['DeviceName'] == root_device_name:
                print('Bastion root volume id =', volume['Ebs']['VolumeId'])
        