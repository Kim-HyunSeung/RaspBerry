import sys
import socket
import time




def run_client(host,port):
	clnt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clnt.connect((host,int(port)))
	while True:
		sendData = input('send >>')
		clnt.sendall(sendData.encode())
		if sendData == 'bye':
			break
		echoData = clnt.recv(1024)
		print("echo data1: %s" % echoData.decode())
	clnt.close()






if __name__=="__main__":
	try:
		run_client(sys.argv[1],sys.argv[2])
	except(IndexError,NameError) as e:
		print("Exec : %s <IP><port>" %sys.argv[0])	
