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
for csvFile in glob.glob(os.path.join(sys.argv[2], "*.*")):
    tableName = os.path.splitext(os.path.basename(csvFile))[0]
 
    with open(csvFile, "rb") as f:
        reader = csv.reader(f, delimiter=';')
 
        header = True
        for row in reader:
            if header:
                header = False
                sql = "DROP TABLE IF EXISTS %s" % tableName
                c.execute(sql)
                sql = "CREATE TABLE %s (%s)" % (tableName,
                          ", ".join([ "%s text" % column for column in row ]))
                c.execute(sql)
 
                for column in row:
                    if column.lower().endswith("_id"):
                        index = "%s__%s" % ( tableName, column )
                        sql = "CREATE INDEX %s on %s (%s)" % ( index, tableName, column )
                        c.execute(sql)
 
                insertSql = "INSERT INTO %s VALUES (%s)" % (tableName,
                            ", ".join([ "?" for column in row ]))
                rowLen = len(row)
            else:
                if len(row) == rowLen:
                    c.execute(insertSql, row)

        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
 
        conn.commit()
        
 
c.close()
conn.close()
