import socket
import wmi
UDP_IP = "127.0.0.1"
UDP_PORT = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT)) #
while True:
    # buffer size is 1024 bytes 
    data, addr = sock.recvfrom(1024)
    str=data.decode("utf-8")
    print ("Received message:", str) 
    print(" opening ", str);
    conn = wmi.WMI()
    pid, retval= conn.Win32_Process.Create(CommandLine=str)
