#!/usr/bin/env python3
#Coded By : A_Asaker 

import socket
import threading
import time
import sys
import os
import signal

def send(s):
	message=input(" >>> (YOU) : ")
	message_size=str(len(message))
	s.send(bytes(message_size,"UTF-8"))
	time.sleep(.3)
	s.send(bytes(message,"UTF-8"))
	if(message.lower()=='close'):
		s.close()
		sys.exit("\n \t Bye !")
	    return False
	return True

def recieve(s):
	while 1:
		size=int(s.recv(9).decode())
		data=str(s.recv(size).decode())
		if (data.lower()=='close'):
			s.send(bytes(str(len("close")),"UTF-8"))
			time.sleep(.5)
			s.send(bytes("close","UTF-8"))
			s.close()
			print("\n [*] Server Has Closed The Connection With You !\n \t Bye !")
			os._exit(0)
		elif(data=="KILL ME"):
			s.close()
			print("")
			print(" [*] Server Is Down Now !\n \t Bye !")
			os._exit(0)
		else:
			print("",end="\r")
			print(' << Server >> : ',data ,end="\n >>> (YOU) : ")
			
def ctrlc_handler(signum,frm):
	print("\n If You Want To Close, Type : CLOSE \n >> ", end='')


def main():
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	host=''
	port=1122
	signal.signal(signal.SIGINT, ctrlc_handler)
	s.connect((host,port))
	print("\n [*] Connected To {} Via Port {} \n".format(host, port))
	thread = threading.Thread(target=recieve, args=(s,))
	thread.daemon = True
	thread.start()
	while send(s):
		pass
	sys.exit("Bue3")
	return
if __name__=="__main__":
	main()
