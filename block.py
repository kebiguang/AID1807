from socket import *
from time import sleep,ctime 

s = socket()
s.bind(('127.0.0.1',8889))
s.listen(5)

#设置套接字设置成非阻塞
s.settimeout(2)

while True:
    print("Waiting from connect...")
    try:
        c,addr = s.accept()
    except timeout:
        print(ctime())
        continue
    else:
        print('connect from',addr)
        while True:
            data=c.recv(1024)
            if not data:
                break
            print(data.decode())
    c.close()
s.close()