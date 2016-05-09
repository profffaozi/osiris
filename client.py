# client.py  
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 4212

# connection to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes
data = '56.67'
tm = s.send(data)                                     

s.close()

print("The time got from the server is %s" )
