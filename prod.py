import s3
import dbops

if __name__ == "__main__":
    filepath = "/tmp/"
    d = dbops.dbcommands()
    outputfile = d.dbbackup(filepath)
    print outputfile
    #s = s3.S3Api(access_key, secret_key, bucket_name)
    s = s3.S3Api("XXXXXXXXXXXXXXXXXXXXXX","XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", "db-backups")
    s.upload(outputfile)


