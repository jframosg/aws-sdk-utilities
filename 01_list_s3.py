'''
Created on 11 jul. 2021
A test to access an "aws credentials" account and describe its s3 buckets.
@author: jframosg
'''
import boto3
import os

os.environ['AWS_PROFILE'] = 'YOUR_AWS_PROFILE'
os.environ['AWS_DEFAULT_REGION'] = 'YOUR_AWS_DEFAULT_REGION'

if  __name__ =='__main__':
    s3 = boto3.client('s3', str(os.environ['AWS_DEFAULT_REGION']))
    response = s3.list_buckets()
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')
        