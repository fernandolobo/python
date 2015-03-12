import httplib
conn = httplib.HTTPConnection("mensagensamigaveis.apphb.com")
conn.request("GET", "/api/mensagens/AG/TecnoSpeedNFSE/E1023330FOR")
res = conn.getresponse()
data = res.read()
print(data)
conn.close()
