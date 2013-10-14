#! /usr/bin/env python

import os
import commands
from datetime import datetime,timedelta
import time
class dbcommands():
    def __init__(self, dbname):
        self.dbname = dbname
   
    def getfilename(self, location,days = 0):
        d = datetime.now() - timedelta(days)
        month = d.strftime('%b')
        day = d.strftime('%d')
        return location + "dbdump-%s-%s.out.gz"%(day,month)
    
    def dbbackup(self, filepath):
        outputfile = self.getfilename(filepath) 
        s = commands.getstatusoutput("sudo -u postgres pg_dump -Fc %s > %s"%(self.dbname,outputfile))
        if s[0]:
            print 'Backup Failed', s[1]
        return outputfile

    def dbrestore(self, filename):
        s = self.createdb()
        if s[0]:
            print "Database already exists", s[1]
            print self.dropdb()
            print "db is drop"
            time.sleep(5)
            print self.createdb()
        s = commands.getstatusoutput("sudo -u postgres pg_restore -d %s %s"%(self.dbname,filename))
        if s[0]:
            print 'restore Failed', s[1]

    def createdb(self):
        s = commands.getstatusoutput("sudo -u postgres createdb %s"%self.dbname)
        return s
    def dropdb(self):
        s = commands.getstatusoutput("sudo -u postgres dropdb %s"%self.dbname)
        return s


