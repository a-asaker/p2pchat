#!/usr/bin/env python3
#Coded By : A_Asaker 

import socket
import threading
from multiprocessing import Process
import time
import sys
import os
import signal

def send(s):
	message=input(" >>> (YOU) : ")
	message_size=str(len(message))
	s.send(bytes(message_size,"UTF-8"))
	time.sleep(.5)
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
			print("\n [*] Server Has Closed The Connection With You !\n \t Bye !",end=" ")
			os.kill(os.getpid(), signal.SIGKILL)
		elif(data=="KILL ME"):
			s.close()
			print("")
			print(" [*] Server Is Down Now !\n \t Bye !",end=" ")
			os.kill(os.getpid(), signal.SIGKILL)
		else:
			print("",end="\r")
			print(' << Server >> : ',data ,end="\n >>> (YOU) : ")
def main():
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	host=''
	port=1122
	s.connect((host,port))
	print("\n [*] Connected To {} Via Port {} \n".format(host, port))
	thread = threading.Thread(target=recieve, args=(s,))
	thread.daemon = True
	thread.start()
	while send(s):
		pass
	return
if __name__=="__main__":
	main()

''' 
IF U USE WINDOWS :
(1) ==> Replace [ os.kill(os.getpid(), signal.SIGKILL) ] In The Code with ==> [ killProcess(os.getpid()) ].
(2) ==> Add The Code Below To The Beginning Of The Project .

import subprocess as s
def killProcess(pid):
    s.Popen('taskkill /F /PID {0}'.format(pid), shell=True)
'''
