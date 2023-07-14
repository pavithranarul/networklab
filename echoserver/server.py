import socket
HOST='127.0.0.1'
PORT=9999
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,a=s.accept()
print('connected by:',a)
while 1:
    d=conn.recv(1024)
    print(d)
    if not d:
        break
    conn.send(d)
conn.close()