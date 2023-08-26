from socket import *
serverName = "192.168.67.92" # IPv4 // ::1 IPv6
serverPort = 12500
clientSocket = socket(AF_INET, SOCK_DGRAM) # AF_INET6
print("UDP Client\n")
while 1:
    message = input("Input message: ")
    if message == "exit":
            break
    clientSocket.sendto(bytes(message,"utf-8"), (serverName, serverPort))
clientSocket.close()