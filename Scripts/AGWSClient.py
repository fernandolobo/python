from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import
import datetime
import suds


#Tratamento de erros que ocorriam ao realizar o GetObjetoContasaReceber
#Update: Problema corrigido ao ativar as propriedades soRootRefNodesToBody soUTF8InHeader soUTF8EncodeXML no HTTPSoapPascalInvoker 
#import logging
#logging.getLogger('suds.bindings.multiref').setLevel(logging.CRITICAL)
#logging.getLogger('suds.umx.typed').setLevel(logging.CRITICAL)
####

imp = Import('http://schemas.xmlsoap.org/soap/encoding/')
url= 'http://127.0.0.1:81/cgi-bin/AGWS.exe/wsdl/IAG'
d = ImportDoctor(imp)
client = Client(url, doctor=d)

print('\n##### ECO #####\n')
msg = client.service.Eco('Teste')
print(msg.encode('utf-8'))

print('\n##### PREPARAR CRE #####\n')
data = datetime.datetime.today()

vCre = client.factory.create('ns1:TVencimentosaReceber')
vCre.agenteCobrador
vCre.vencimento = data
vCre.valor = 150.45
vCre.tipoDocumento = '001'
vCre.titulo = '123'
vCre.agenteCobrador = '0001'
vCre.descontoPrevisto = 0
vCre.idBloquete = 0
vCre.codigo = ''
vCre.sequencial = 0
vCre.nrBoleto = ''

vchcre = client.factory.create('ns1:TVencimentosChequeaReceber')
vchcre.vencimento = data
vchcre.valor = 150
vchcre.bancoNumero = '031'
vchcre.agencia = '123'
vchcre.cc = '0001'
vchcre.numero = '123456'
vchcre.titular = 'Luiz'
vchcre.codBanco = ''
vchcre.sequencial = 0
vchcre.codigo = ''

vcacre = client.factory.create('ns1:TVencimentosCartaoaReceber')
vcacre.vencimento = data
vcacre.valor = 100
vcacre.administradora = '0001'
vcacre.TAD_Valor = 33
vcacre.sequencial = 0
vcacre.codigo = ''

vsecre = client.factory.create('ns1:TServicosaReceber')
vsecre.servico = '0001'
vsecre.modalidade = '01'
vsecre.valor = 200.45
vsecre.sequencial = 0
vsecre.codigo = ''

vitcre = client.factory.create('ns1:TItensaReceber')
vitcre.Produto = '0000000001'
vitcre.Quantidade = 10
vitcre.Valor = 20
vitcre.CFOP_Codigo = '5102'
vitcre.STA_Codigo = '0'
vitcre.STB_Codigo = '00'
vitcre.AliquotaICMS = 0
vitcre.AliquotaIPI = 0
vitcre.AliqICMSSubst = 0
vitcre.BaseICMSSubst = 0
vitcre.ValorICMSSubst = 0
vitcre.Frete = 0
vitcre.CompDescricao = ''
vitcre.Unidade = ''
vitcre.Sequencial = 0
vitcre.Codigo = ''

avcre = client.factory.create('ns1:TArrayofVencimentosaReceber')
avcre.item = [vCre]

avchcre = client.factory.create('ns1:TArrayofVencimentosChequeaReceber')
avchcre.item = [vchcre]

avcacre = client.factory.create('ns1:TArrayofVencimentosCartaoaReceber')
avcacre.item = [vcacre]

avsecre = client.factory.create('ns1:TArrayofServicosaReceber')
avsecre.item = [vsecre]

avitcre = client.factory.create('ns1:TArrayofItensaReceber')
avitcre.item = [vitcre]

icre = client.factory.create('ns1:TContasaReceber')
icre.estabelecimento = '0001'
icre.centroResultados = '001'
icre.cliente = '03744126000169'
icre.receita = '4010010001'
icre.documento = '111'
icre.tipoGeracao = 'A'
icre.mesAno = '201501'
icre.emissao = data
icre.exportaAC = 1
icre.ISS = 0
icre.IRRF = 0
icre.INSS = 0
icre.PIS = 0
icre.obs = 'obs'
icre.vencimentosaReceber = avcre
icre.vencimentosChequeaReceber = avchcre
icre.vencimentosCartaoaReceber = avcacre
icre.servicosaReceber = avsecre
icre.itensaReceber = avitcre

print('\n##### ECO CONTAS A RECEBER #####\n')
print(client.service.EcoContasAReceber(icre).encode('utf-8'))

print('\n##### INCLUIR CRE #####\n')
msg = client.service.IncluiContasaReceber(icre)
print(msg.encode('utf-8'))

print('\n##### GET CRE #####\n')
teste = client.service.getObjetoContasaReceber(msg)
print(teste)

print('\n##### PREPARAR BAIXA CRE #####\n')
data = datetime.datetime.today()
bcre = client.factory.create('ns2:TBaixaContasaReceber')
bcre.CRE_Codigo = msg#'20130100006'
bcre.Data = data
bcre.Desconto = 0
bcre.ExportaAC = 0
bcre.Juros = 0
bcre.Multa = 0
bcre.Sequencial = 1
bcre.SequencialVencimento = 1
bcre.Valor = 150.45
bcre.LAN_CRD_Desconto = '11303'
bcre.LAN_ContaFinanceira = '0001'
bcre.LAN_CRD_Juros = ''
bcre.LAN_CRD_Multa = ''
bcre.LAN_Historico = ''

print('\n##### INCLUIR BAIXA CRE #####\n')
msg = client.service.IncluiBaixaContasReceber(bcre)
print(msg.encode('utf-8'))

print('\n##### PREPARAR CLIENTE #####\n')
cli = client.factory.create('ns1:TCliente')
cli.nome = 'Luiz Carlos';
cli.nomeFantasia = 'Luiz';
cli.cnpjcpf = '44228633000127';
cli.grupo = '0001';
cli.receita = '4010010003';
cli.agenteCobrador = '0001';
cli.Vencimento = 10;
cli.Etiqueta = 1;
cli.GeraNFAuto = 1;
cli.RetemISS = 1;
cli.RetemINSS = 0;
cli.IM = '1478522';
cli.AliquotaISS = 12.5;
cli.identificador = '123456'
print(cli)

print('\n##### INCLUIR CLIENTE #####\n')
msg = client.service.IncluiCliente(cli)
print(msg.encode('utf-8'))

print('\n##### getClienteWithIdentificador #####\n')
msg = client.service.getClienteWithIdentificador('123456')
print(msg.encode('utf-8'))

print('\n##### ExcluiClienteWithCNPJCPF #####\n')
msg = client.service.ExcluiClienteWithCNPJCPF('44228633000127')
print(msg.encode('utf-8'))
