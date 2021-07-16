'''
Created on 11 jul. 2021
A test to get EBS root volume attached from ec2 instance with tag name
@author: jframosg
'''

import boto3
import os

os.environ['AWS_PROFILE'] = 'YOUR_AWS_PROFILE'
os.environ['AWS_DEFAULT_REGION'] = 'YOUR_AWS_DEFAULT_REGION'

if  __name__ =='__main__':
    ec2 = boto3.client('ec2', str(os.environ['AWS_DEFAULT_REGION']))
    instance_name = 'YOUR_INSTANCE_NAME'
    print('Instance name = ', instance_name)
    custom_filter = [{
        'Name':'tag:Name', 
        'Values': [instance_name]}]   
    instance = ec2.describe_instances(Filters=custom_filter)
    if instance:
        instance = instance['Reservations'][0]['Instances'][0]
        instance_id = instance['InstanceId']
        print('Instance id = ', instance_id)
        root_device_name = instance['RootDeviceName']
        for volume in instance['BlockDeviceMappings']:
            if volume['DeviceName'] == root_device_name:
                print('Bastion root volume id =', volume['Ebs']['VolumeId'])
        