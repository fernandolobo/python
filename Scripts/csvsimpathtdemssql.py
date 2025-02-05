from __future__ import print_function
import os
import dataextract as tde
import datetime
import pymssql

print(str(datetime.datetime.now()))

conn = pymssql.connect(host='10.1.254.74\sqlexpress', user='ET', password='@3T0615', database='ET')
cursor = conn.cursor()
cursor.execute('SELECT * FROM REG')
tableName = 'REG'
if os.path.isfile(tableName+'.tde'):
    os.remove(tableName+'.tde')
tdeFile = tde.Extract(tableName+'.tde')
tableDef = tde.TableDefinition()
tableDef.addColumn('ID', tde.Type.INTEGER)
tableDef.addColumn('HoraRegistro', tde.Type.DATETIME)
tableDef.addColumn('SerialHD', tde.Type.CHAR_STRING)
tableDef.addColumn('PlacaRede', tde.Type.CHAR_STRING)
tableDef.addColumn('VersaoWin', tde.Type.CHAR_STRING)
tableDef.addColumn('UsuarioWin', tde.Type.CHAR_STRING)
tableDef.addColumn('NomeMaq', tde.Type.CHAR_STRING)
tableDef.addColumn('IPMaq', tde.Type.CHAR_STRING)
tableDef.addColumn('HoraMaq', tde.Type.DATETIME)
tableDef.addColumn('ProcessadorMaq', tde.Type.CHAR_STRING)
tableDef.addColumn('MemoriaMaq', tde.Type.CHAR_STRING)
tableDef.addColumn('NomeLic', tde.Type.CHAR_STRING)
tableDef.addColumn('CNPJLic', tde.Type.CHAR_STRING)
tableDef.addColumn('NrSerieLic', tde.Type.CHAR_STRING)
tableDef.addColumn('SistemaLic', tde.Type.CHAR_STRING)
tableDef.addColumn('EstadoLic', tde.Type.CHAR_STRING)
tableDef.addColumn('BombaLic', tde.Type.DATETIME)
tableDef.addColumn('IPLic', tde.Type.CHAR_STRING)
tableDef.addColumn('DataLic', tde.Type.DATETIME)
tableDef.addColumn('CaminhoSis', tde.Type.CHAR_STRING)
tableDef.addColumn('VersaoSis', tde.Type.CHAR_STRING)
tableDef.addColumn('NomeSis', tde.Type.CHAR_STRING)
tableDef.addColumn('NavegadorPadrao', tde.Type.CHAR_STRING)
tableDef.addColumn('UFEmp', tde.Type.CHAR_STRING)
tableDef.addColumn('CidadeEmp', tde.Type.CHAR_STRING)
tableDef.addColumn('EnderecoEmp', tde.Type.CHAR_STRING)
tableDef.addColumn('CNPJEmp', tde.Type.CHAR_STRING)
tableDef.addColumn('VERSAOSGDB', tde.Type.CHAR_STRING)
tableDef.addColumn('HoraReg', tde.Type.DATETIME)

table = tdeFile.addTable('Extract',tableDef)

for row in cursor:
    newRow = tde.Row(tableDef)
    newRow.setInteger(0, int(row[0]))
    data = datetime.datetime.strptime(str(row[1]), "%Y-%m-%d %H:%M:%S")
    newRow.setDateTime(1, data.year, data.month, data.day, data.hour, data.minute, data.second, data.microsecond)
    newRow.setCharString(2, str(row[2].encode('utf-8')))
    newRow.setCharString(3, str(row[3].encode('utf-8')))
    newRow.setCharString(4, str(row[4].encode('utf-8')))
    newRow.setCharString(5, str(row[5].encode('utf-8')))
    newRow.setCharString(6, str(row[6].encode('utf-8')))
    newRow.setCharString(7, str(row[7].encode('utf-8')))
    data = datetime.datetime.strptime(str(row[8]), "%Y-%m-%d %H:%M:%S")
    newRow.setDateTime(8, data.year, data.month, data.day, data.hour, data.minute, data.second, data.microsecond)
    newRow.setCharString(9, str(row[9].encode('utf-8')))
    newRow.setCharString(10, str(row[10].encode('utf-8')))
    newRow.setCharString(11, str(row[11].encode('utf-8')))
    newRow.setCharString(12, str(row[12].encode('utf-8')))
    newRow.setCharString(13, str(row[13].encode('utf-8')))
    newRow.setCharString(14, str(row[14].encode('utf-8')))
    newRow.setCharString(15, str(row[15]).encode('utf-8'))
    data = datetime.datetime.strptime(str(row[16]), "%Y-%m-%d %H:%M:%S")
    newRow.setDateTime(16, data.year, data.month, data.day, data.hour, data.minute, data.second, data.microsecond)
    newRow.setCharString(17, str(row[17].encode('utf-8')))
    data = datetime.datetime.strptime(str(row[18]), "%Y-%m-%d %H:%M:%S")
    newRow.setDateTime(18, data.year, data.month, data.day, data.hour, data.minute, data.second, data.microsecond)
    table.insert(newRow)

tdeFile.close()

print(str(datetime.datetime.now()))