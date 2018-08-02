#!/usr/bin/env python3
import socket
import threading
from multiprocessing import Process
import time
import sys

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='0.0.0.0'
port=1122
s.bind((host,port))
print(" [*] Socket Established On [ {} : {} ] ".format(host,port))

def send(s,conn):
  message=""
  try:
    message=input(" >>> (YOU) : ")
    message_size=str(len(message))
    conn.send(bytes(message_size,"UTF-8"))
    time.sleep(.5)
    conn.send(bytes(message,"UTF-8"))
    if(message.lower()=='close'):
      time.sleep(1)
      # conn.shutdown(2)
      # conn.close()
      return 0
    elif(message == "KILL ME"):
      conn.shutdown(2)
      conn.close()
      s.shutdown(2)
      s.close()
      return "CLOSE"
    return True
  except:
    if (message=="KILL ME"):
      s.shutdown(2)
      s.close()
      return "CLOSE"
    return "Exception"

def recieve(s,conn,ip):
  while 1:
    rec_data=conn.recv(9).decode()
    size=int(rec_data)
    data=str(conn.recv(size).decode())
    if(data.lower() == 'close'):
      conn.shutdown(2)
      conn.close()
      print("\n [*] Client Has Closed The Connection ! \n Press [Enter] To Listen To A Client Or 'KILL ME' To EXIT  ...", end="\n ")
      return 0
    else:
      print("",end="\r")
      print(" << {} >> : ".format(ip),data,end="\n >>> (YOU) : ")

def main():
  print(" [*] Listening . . .", end="\n ")
  # print(" ",end=" ")
  s.listen(1)
  conn,addr=s.accept()
  ip=addr[0]
  print("[*] ",ip," Connected!")
  thread = threading.Thread(target=recieve, args=(s,conn,ip,))
  thread.daemon = True
  thread.start()
  while 1:
    stat=send(s,conn)
    if (stat==1):
      pass
    elif (stat==0):
      if(input(" ")=="KILL ME"):
        sys.exit(" [*] Connection Closed ! \n \t Bye\n ")
      else:
        break
    elif(stat=="Exception"):
      break
    elif (stat=="CLOSE"):
      sys.exit(" [*] Connection Closed ! \n \t Bye\n ")

  # thread.join()

while __name__=="__main__":
  main()
