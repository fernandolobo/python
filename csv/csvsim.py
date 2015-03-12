import csv, sqlite3
from collections import OrderedDict

con = sqlite3.connect("sim.sqlite")
cur = con.cursor()
with open('AF201401.CPF', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    to_db = OrderedDict((row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                         row[7], row[8], row[9:]) for row in reader)
cur.executemany("INSERT INTO CPF (TipoDocumento, CodMunicipio, "+
                "Exercicio, Orgao, UnidadeOrcamentaria, DataCompetencia, "+
                "TipoFolha, DataFolha, NumCPF, Ingresso) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
    


#    reader = csv.reader(csvfile)
#    for row in reader:
#        print ', '.join(row)
