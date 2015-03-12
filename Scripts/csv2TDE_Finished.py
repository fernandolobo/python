import csv,os,datetime
import dataextract as tde

#Step 1: Create the Extract File and open the .csv
try:
    tdefile = tde.Extract('SuperStoreCSVExtract.tde')
except:
    os.remove('SuperStoreCSVExtract.tde')
    tdefile = tde.Extract('SuperStoreCSVExtract.tde')

csvReader = csv.reader(open('SuperStoreCSV.csv','rb'), delimiter=',', quotechar='"')

#Step 2: Create the tableDef
tableDef = tde.TableDefinition()
tableDef.addColumn('Row ID', tde.Type.CHAR_STRING)
tableDef.addColumn('Order Date', tde.Type.DATE)
tableDef.addColumn('Sales', tde.Type.DOUBLE)
tableDef.addColumn('Profit', tde.Type.DOUBLE)
tableDef.addColumn('Customer Name', tde.Type.CHAR_STRING)
tableDef.addColumn('Zip Code', tde.Type.INTEGER)
tableDef.addColumn('Product Category', tde.Type.CHAR_STRING)

#Step 3: Create the table in the image of the tableDef
table = tdefile.addTable('Extract',tableDef)

#Step 4: Loop through the csv, grab all the data, put it into rows
#and insert the rows into the table
newrow = tde.Row(tableDef)
csvReader.next() #Skip the first line since it has the headers
for line in csvReader:
    newrow.setCharString(0, str(line[0]))
    date = datetime.datetime.strptime(line[1], "%m/%d/%Y")
    newrow.setDate(1, date.year, date.month, date.day)
    newrow.setDouble(2,float(line[2]))
    newrow.setDouble(3,float(line[3]))
    newrow.setCharString(4,line[4])
    newrow.setInteger(5,int(line[5]))
    newrow.setCharString(6,line[6])
    table.insert(newrow)

#Step 5: Close the tde
tdefile.close()
