import socket
import threading
host = '127.0.0.1'
port = 8000
import os
import platform

# AUTHOR THE KING OF THE GLORY TELEGRAM -- https://t.me/TheKingOfTheGloryOfficall #

print("[$] AUTHOR THE KING OF THE GLORY TELEGRAM -- https://t.me/TheKingOfTheGloryOfficall") 
print("[#] HELEKI BAGLANTI YOXDUR BAGLANTI GOZLENILIR ...")

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
            broadcast('\33[31m{}\33[0m Getdi !'.format(nickname).encode('ascii'))
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
            ("[-]SIZIN OPERATING SYSTEMINIZ DESTEKLENMIR !!")
            exit()

        print("[$] AUTHOR THE KING OF THE GLORY TELEGRAM -- https://t.me/TheKingOfTheGloryOfficall")
        print("[+] CIHAZ BAGLANTISI QEBUL EDILDI !!")
    
        print("[+] Bununla Qosuldu {}".format(str(address)))
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print("[+] Nickname budur {}".format(nickname))
        broadcast("\33[31m{}\33[0m Chata Qatildi ! ".format(nickname).encode('ascii'))
        client.send('\n[+] Servere Qosuldunuz !'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()


    





    