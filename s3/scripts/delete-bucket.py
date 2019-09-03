#!/usr/bin/env python
import sys
import boto3

def delete_empty_buket():
	s3 = boto3.resource('s3')
	for bucket_name in sys.argv[1:]:
	    bucket = s3.Bucket(bucket_name)
	try:
	    response = bucket.delete()
	    # print response
	except Exception as error:
	    print (error)


def empty_bucket():

	s3 = boto3.resource('s3')
	for bucket_name in sys.argv[1:]:
	    bucket = s3.Bucket(bucket_name)
	    for key in bucket.objects.all():
	        try:
	            response = key.delete()
	            print (response)
	        except Exception as error:
	            print (error)


empty_bucket();

# delete_empty_buket()

# empty_bucket();