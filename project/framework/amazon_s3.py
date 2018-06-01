import boto3
import os
from boto3.s3.transfer import S3Transfer

class AmazonS3():

    s3 = None
    transfer = None

    def __init__(self):
        self.s3 = boto3.client(
            's3',
            aws_access_key_id='YOUACCESSKEY',
            aws_secret_access_key='YOUSECRETKEY',
        )
        self.transfer = S3Transfer(self.s3)

    def upload_file(self, file, bucket, alias):
        self.s3.upload_file(file, bucket, alias, ExtraArgs={'ACL': 'public-read', 'ContentDisposition': 'inline'})
        file_url = '%s/%s' % ('http://cloudfront.net', alias)
        return file_url
