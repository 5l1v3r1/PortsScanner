import threading
import socket

target = input("Host : ")

def portscan(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)# 

    try:
        con = s.connect((target,port))

        print('Port :',port,"Open")

        con.close()
    except: 
        pass
r = 1 
for x in range(1,500): 

    t = threading.Thread(target=portscan,kwargs={'port':r}) 

    r += 1     
    t.start() 