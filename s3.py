import boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import os

class S3Api():
    def __init__(self,access_key, secret_key, bucket_name):
        self.access_key = access_key
        self.secret_key = secret_key
        self.conn = S3Connection(self.access_key, self.secret_key)
        self.bucket_name = bucket_name
        self.bucket = self.get_bucket(self.bucket_name)
    
    def get_bucket(self, bucket_name):
        bucket = self.conn.get_bucket(bucket_name)
        return bucket
    
    def upload(self, filepath):
        k = Key(self.bucket)
        key = os.path.basename(filepath)
        fn = filepath
        k.key = key
        k.set_contents_from_filename(fn)

    def download(self, filename,destpath):
        fn = self.bucket.get_key(filename)
        fn.get_contents_to_filename(destpath)

    def checkfile(self, key):
        fn = self.bucket.get_key(key)
        return fn
