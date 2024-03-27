import socket
import threading
import re
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
final = ''
class Chat:
	def __init__(self,conType,crypto,ip,port = 0):
		self.conType = conType
		self.crypto = crypto
		self.ip = ip
		self.port = port


def CHAT(tipo):
	if tipo == 1:
		while status == 0:
			conversa = input('')
			conversa = Crypto(crypto,conversa)
			env = ((conversa).encode())
			s.sendall(env)
	if tipo == 2:
		while status == 0:
			resp = s.recv(1024)
			resp = Descrypto(resp.decode('utf-8'),crypto)
			print(resp)
	if tipo == 3:
		while True:
			resp = con.recv(1024)
			resp = Descrypto(resp.decode('utf-8'),crypto)
			print(resp)
	if tipo == 4:
		while True:
			conversa = input('')
			conversa = Crypto(crypto,conversa)
			env = ((conversa).encode())
			con.sendall(env)
fala = threading.Thread(target=CHAT, args=[2])
falas = threading.Thread(target=CHAT, args=[3])
conversa = threading.Thread(target=CHAT, args=[1])
conversas = threading.Thread(target=CHAT, args=[4])

ip = '127.0.0.1'
tipo = int(input('Selecione o que você vai ser:\r\n1-Client\r\n2-Server\r\n--> '))
crypto = int(input('chave criptográfica:(8 caracteres)\r\n--> '))
dict = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def Crypto(crypto,mesg):
	result = []
	global dict
	msg = mesg
	for x in msg:
		if x == " ":
			converted = ' '
			result.append(converted)
		else:
			converted = (dict.index(x) + crypto) %26
			result.append(dict[converted])
	final = ''.join(result)
	return final
def Descrypto(msg,crypto):
	global dict
	back = []
	for x in msg:
		if x == " ":
			origin = ' '
			back.append(origin)
		else:
			converted = (dict.index(x) - crypto) %26
			back.append(dict[converted])
	final = ''.join(back)
	return final
if (tipo == 1):
	ip = input('qual o Ip do servidor:\r\n--> ');
	port = int(input('qual a porta de conexão:\r\n--> '))
	con1 = Chat(tipo,crypto,ip,port)
	print('Conectando ao Servidor ....\r\n')
	status = s.connect_ex((con1.ip,con1.port))
	if (status == 0):
		print("Conetado ao Servidor\r\n\r\n")
		conversa.start()
		fala.start()
elif (tipo == 2):
	port = int(input('Selecione a porta em que você irá abrir sua conexão (escolha sempre portas mais altas):\r\n--> '))
	con1 = Chat(tipo,crypto,ip,port)

	s.bind((con1.ip,con1.port))
	s.listen(1)
	print('Servidor iniciado\r\n')
	while True:
		con, cliente = s.accept()
		print(f'{cliente} Conetou\r\n')
		falas.start()
		conversas.start()
