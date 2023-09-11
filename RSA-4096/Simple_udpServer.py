from csv import reader
import pickle
from socket import *
from rsa_tool import get_keys, decrypt
from time import time

rsa_keys = get_keys()

serverPort = 12500
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("UDP server\n")

while 1:
    data, clientAddress = serverSocket.recvfrom(2048)
    start = time()
    print('Decrypting...')
    message = pickle.loads(data)
    text = decrypt(message, rsa_keys['D'], rsa_keys['N'])
    end = time()
    print("Received from Client: ", text)
    print("Time: ", end - start)
