from scapy.all import *
import sys
import socket


if (len(sys.argv) <= 2):
	print('USO DO SCRIPT:\r\nPort_Scan.py <Ip> <tipo de Scan> <Options> (script em desenvolvimento)\r\ntipos de Scan:\r\n-ss -> Scan com TCP(tem algumas falhas) (não completa o 3 Way Hand Shake)\r\n-st -> Scan TCP (completa o 3 Way Hand Shake (mais barulhento))')
else:
	dst_ip = sys.argv[1]
	scantp = sys.argv[2]
	portas_default = [80,443,3306,2049,22,21,20,587,50,110,24,25,26]
	if (scantp == '-ss'):
		for x in portas_default:
			resp = sr1(IP(dst=dst_ip)/TCP(dport=x),verbose=False,timeout=3)
			if resp == None:
				print(f'Porta {x} [FILTRADA]')
			elif resp['TCP'].flags == 'SA':
				print(f'Porta {x} [ABERTA]')
			elif resp['TCP'].flags == 'RA':
				print(f'Porta {x} [FECHADA]')
	elif (scantp == '-st'):
		for x in portas_default:
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.settimeout(3)
			resp1 = s.connect_ex((dst_ip,x))
			s.close()
			if (resp1 == 0):
				print(f'PORTA {x} [ABERTA]')
			elif (resp1 == 11):
				print(f'PORTA {x} [FILTRADA]')
			elif (resp1 == 111):
				print(f'PORTA {x} [FECHADA]')
	else:
		print('Tipo de Scan Inválido')

print(sys.argv[0:])
