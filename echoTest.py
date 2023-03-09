
import sys
import socket
import time
from threading import Thread



i=1
def run_server(port):
	BUFSIZE = 1024
	host = socket.gethostname()
	ip = '192.168.0.105'
	#ip = socket.gethostbyname(host)
	serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	serv.bind(('192.168.0.105',int(port)))
	serv.listen(5) # client number of people
	print("server %s: %s start..." %(ip,port))
	i=1
	while True:
		clnt,addr  = serv.accept()
		print("%d client connected..." %i )
		th = Thread(target=run_client,args=(clnt,addr))
		th.start()
		i+=1

def run_client(clnt,addr):
	while True:
		data = clnt.recv(1024)
		print("recv from %d: %s" % (i,data.decode()))
		if data.decode() == 'bye':
			clnt.close()
		clnt.sendall(data)




if __name__ == '__main__':
	try:
		run_server(sys.argv[1])
	except (IndexError, NameError) as e:
		print("Execute: %s <port>" % sys.argv[0])
