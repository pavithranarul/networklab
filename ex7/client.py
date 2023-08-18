import socket
s=socket.socket()
host=input(str("please enter the host addr of sender:"))
port=8080
s.connect((host,port))
print("connected...")
filename=input(str("enter filename:"))
file=open(filename,"wb")
file_data=s.recv(1024)
file.write(file_data)
file.close()
print("file has benn received successfully")