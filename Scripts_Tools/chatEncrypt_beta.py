import socket
import threading

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

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
			env = ((conversa).encode())
			s.sendall(env)
	if tipo == 2:
		while status == 0:
			resp = s.recv(1024)
			print(resp.decode('utf-8'))
	if tipo == 3:
		while True:
			resp = con.recv(1024)
			print(resp.decode('utf-8'))
	if tipo == 4:
		while True:
			conversa = input('')
			env = ((conversa).encode())
			con.sendall(env)
fala = threading.Thread(target=CHAT, args=[2])
falas = threading.Thread(target=CHAT, args=[3])
conversa = threading.Thread(target=CHAT, args=[1])
conversas = threading.Thread(target=CHAT, args=[4])

ip = '127.0.0.1'
tipo = int(input('Selecione o que você vai ser:\r\n1-Client\r\n2-Server\r\n--> '))
crypto = input('chave criptográfica:(8 caracteres ou menos)\r\n--> ')
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
