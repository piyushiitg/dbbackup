import s3
import dbops

if __name__ == "__main__":
    d = dbops.dbcommands("math")
    filename = d.getfilename('')
    destpath = "/tmp/" + filename
    s = s3.S3Api("XXXXXXXXXXXXXXXXXXXXXXXXX","XXXXXXXXXXXXXXXXXXXXXXXXXXXx", "db-backups")
    i = 1
    print filename
    while(s.checkfile(filename) is None and i < 10):
        filename = d.getfilename('',days=i)
        i= i + 1
    if i >= 10:
        print "Error: Some problem with fetching from S3"
    
    print filename
    s.download(filename, destpath)
    d.dbrestore(destpath)


