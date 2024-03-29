#!/usr/bin/env python
import sys
import boto3
s3 = boto3.resource("s3")
for bucket_name in sys.argv[1:]:
    try:
        response = s3.create_bucket(ACL= 'public-read-write',Bucket=bucket_name,
        	CreateBucketConfiguration={'LocationConstraint':'us-west-2'})
        print (response)
    except Exception as error:
        print (error)