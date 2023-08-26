from socket import *
from CryptoMasterBlasterTool import CriptoGaiusIuliusCaesar

cryptoMasterBlasterTool = CriptoGaiusIuliusCaesar()

serverName = "127.0.0.1" # IPv4 // ::1 IPv6
serverPort = 12500
clientSocket = socket(AF_INET, SOCK_DGRAM) # AF_INET6
print("UDP Client\n")
while 1:
    message = input("Input message: ")
    if message == "exit":
            break
    
    message = cryptoMasterBlasterTool.crypt(message)
    clientSocket.sendto(message, (serverName, serverPort))
clientSocket.close()