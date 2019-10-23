import socket

socked = socket.socket()
socked.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ADDR = ("0.0.0.0",8686)
socked.bind(ADDR)
socked.listen(3)
while True:
    try:
        conned,addr = socked.accept()
        print(addr)
    except KeyboardInterrupt as e:
        print(e)
        break
    while True:
        data = conned.recv(1024)
        if not data:
            break
        print(data)
        n=conned.send(b"OK")
    conned.close()

socked.close()