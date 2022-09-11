import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_nane=socket.gethostname()
PORT=12345
s.connect ((HOST_NAME,PORT))
