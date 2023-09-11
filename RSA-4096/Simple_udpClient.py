from csv import reader
import pickle
from socket import *
from rsa_tool import get_keys, encrypt
from time import time

rsa_keys = get_keys()

serverName = "127.0.0.1"  # IPv4 // ::1 IPv6
serverPort = 12500
clientSocket = socket(AF_INET, SOCK_DGRAM)  # AF_INET6

print("UDP Client\n")

message = "The information security is of significant importance to ensure the privacy of communications"
start = time()
print('message: ', message)
print('encrypting...')
message = encrypt(message, rsa_keys['E'], rsa_keys['N'])
data = pickle.dumps(message)
print('encrypted message: ', data)
clientSocket.sendto(bytes(data), (serverName, serverPort))
end = time()
print("Time: ", end - start)
clientSocket.close()
