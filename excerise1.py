import socket

socked = socket.socket()
ADDR = ("127.0.0.1",8686)
socked.connect(ADDR)
while True:
    data=input(">>")
    if not data:
        print("结束啦...")
        break
    socked.send(data.encode())
    msg = socked.recv(1024)
    print(msg)
socked.close()