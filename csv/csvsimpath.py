from __future__ import print_function
import sqlite3
import csv
import os
import glob
import sys
from time import gmtime, strftime

print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

db = sys.argv[1]
 
conn = sqlite3.connect(db)
conn.text_factory = str  
c = conn.cursor()
for csvfile in glob.glob(os.path.join(sys.argv[2], "*.*")):
    tablename = os.path.splitext(os.path.basename(csvfile))[0]
 
    with open(csvfile, "rb") as f:
        reader = csv.reader(f, delimiter=';')
 
        header = True
        for row in reader:
            if header:
                header = False
                sql = "DROP TABLE IF EXISTS %s" % tablename
                c.execute(sql)
                sql = "CREATE TABLE %s (%s)" % (tablename,
                          ", ".join([ "%s text" % column for column in row ]))
                c.execute(sql)
 
                for column in row:
                    if column.lower().endswith("_id"):
                        index = "%s__%s" % ( tablename, column )
                        sql = "CREATE INDEX %s on %s (%s)" % ( index, tablename, column )
                        c.execute(sql)
 
                insertsql = "INSERT INTO %s VALUES (%s)" % (tablename,
                            ", ".join([ "?" for column in row ]))
                rowlen = len(row)
            else:
                if len(row) == rowlen:
                    c.execute(insertsql, row)

        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
 
        conn.commit()
        
 
c.close()
conn.close()
