from __future__ import print_function
import csv
import os
import glob
import sys
import dataextract as tde
import datetime

print(str(datetime.datetime.now()))

for csvFile in glob.glob(os.path.join(sys.argv[1], "*.*")):
    tableName = os.path.splitext(os.path.basename(csvFile))[0]
    if os.path.isfile(tableName+'.tde'):
        os.remove(tableName+'.tde')
    tdeFile = tde.Extract(tableName+'.tde')
    tableDef = tde.TableDefinition()

    with open(csvFile, "rb") as f:
        reader = csv.reader(f, delimiter=';')

        header = True
        for row in reader:
            if header:
                header = False
                for column in row:
                    tableDef.addColumn(str(column), tde.Type.CHAR_STRING)
                table = tdeFile.addTable('Extract',tableDef)
                newRow = tde.Row(tableDef)
                rowLen = len(row)
            else:
                if len(row) == rowLen:
                    i = 0
                    for column in row:
                        newRow.setCharString(i, str(column))
                        i += 1
                    table.insert(newRow)

        print(str(datetime.datetime.now()))
    tdeFile.close()