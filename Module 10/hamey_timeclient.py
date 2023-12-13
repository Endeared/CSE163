# Ross Hamey
# CSE163 - P10.2
# 12/3/2023
# https://github.com/Endeared

from socket import *
from codecs import decode

HOST = "localhost" 
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

try:
    server = socket(AF_INET, SOCK_STREAM)               # Create a socket
    server.connect(ADDRESS)                             # Connect it to a host
    dayAndTime = decode(server.recv(BUFSIZE), "ascii")  # Read a string from it
    print(dayAndTime)
    server.close()   
except ConnectionRefusedError:
    print("Error connecting to the server")  
    exit()