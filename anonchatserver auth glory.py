import socket
import threading
host = '127.0.0.1'
port = 8000
import os
import platform

# AUTHOR THE KING OF THE GLORY TELEGRAM -- https://t.me/TheKingOfTheGloryOfficall #

if platform.system() == "Linux":
    os.system("clear")       
elif platform.system() == "Windows":
    os.system("cls")
else:
    ("\33[1;31m[-]\33[1;0m SIZIN OPERATING SYSTEMINIZ DESTEKLENMIR !!")
    exit()

print("\33[1;31m[$] AUTHOR THE KING OF THE GLORY TELEGRAM -- https://t.me/TheKingOfTheGloryOfficall\33[1;0m") 
print("\33[1;33m[#] HELEKI BAGLANTI YOXDUR BAGLANTI GOZLENILIR ...\33[1;0m")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try: 
            message = client.recv(1024)
            broadcast(message)
        except:   
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('\33[1;31m{}\33[1;31m Getdi !'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        if platform.system() == "Linux":
             os.system("clear")       
        elif platform.system() == "Windows":
             os.system("cls")
        else:
            ("\33[1;31m[-]\33[1;0m SIZIN OPERATING SYSTEMINIZ DESTEKLENMIR !!")
            exit()

        print("\33[1;31m[$] AUTHOR THE KING OF THE GLORY TELEGRAM -- https://t.me/TheKingOfTheGloryOfficall\33[1;0m") 
        print("\33[1;33m[#] HELEKI BAGLANTI YOXDUR BAGLANTI GOZLENILIR ...\33[1;0m")
    
        print("\33[1;32m[+]\33[1;0m Bununla Qosuldu {}".format(str(address)))
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print("\33[1;32m[+]\33[1;0m Nickname budur {}".format(nickname))
        broadcast("\33[32m{}\33[0m Chata Qatildi ! ".format(nickname).encode('ascii'))
        client.send('\n\33[1;32m[+]\33[1;0m Servere Qosuldunuz !'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
