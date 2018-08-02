# About
  p2p(Peer To Peer) Chat Project ,, Is A Server-client Chat Project That Can Handle Only One Client .
  
  Coded By : a-asaker
 
 # How To Use :
  Locally :
  
    1- Run Server.py On The Device Which Will Be The Server .
  
    2- Edit The Client.py File , Add The Local Ip For The Device Which Is Running The Server.py File Or Leave It Blank If You Use It On Your LocalHost .
            
    3- Run Client.py .
            
   * Note : You Can Change The Port If You Want , But The Port Should Be The Same In The Server And The Client Files .
      
  Globally :
   
    1- You Should Forward Port Which Is In The Python Files To Your Local Address . (Search For Router Port Forwarding) 
   
    2- The Same As Locally Method .
              
 #  For Windows Useres :
 To Work Properly :
          
          (1) ==> Delete The First Line From Client.py,Server.py Files "#!/usr/bin/env pythhon3"
          (2) ==> Replace [|=> os.kill(os.getpid(), signal.SIGKILL) <=|] In The Client File with ==> [|=> killProcess(os.getpid()) <=|] .
          (3) ==> Add The Code Below To The Beginning Of The Project .
          
          
   The Code :
   
    import subprocess as s
    def killProcess(pid):
        s.Popen('taskkill /F /PID {0}'.format(pid), shell=True)
