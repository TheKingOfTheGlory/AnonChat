import socket
import threading
import os
import platform

# AUTHOR THE KING OF THE GLORY

NIP = str(input("[+] NGROK IP GIR: "))
NPORT = int(input("[+] NGROK PORTUNU GIR: "))
nickname = input("[+] AD YAZ: ")


if platform.system() == "Linux":
    os.system("clear")       
elif platform.system() == "Windows":
    os.system("cls")
else:
    ("[-]SIZIN OPERATING SYSTEMINIZ DESTEKLENMIR !!")
    exit()


print("""
\33[31m    
:::'###::::'##::: ##::'#######::'##::: ##::'######::'##::::'##::::'###::::'########:::::::'##::::::::::'#####:::
::'## ##::: ###:: ##:'##.... ##: ###:: ##:'##... ##: ##:::: ##:::'## ##:::... ##..::::::'####:::::::::'##.. ##::
:'##:. ##:: ####: ##: ##:::: ##: ####: ##: ##:::..:: ##:::: ##::'##:. ##::::: ##::::::::.. ##::::::::'##:::: ##:
'##:::. ##: ## ## ##: ##:::: ##: ## ## ##: ##::::::: #########:'##:::. ##:::: ##:::::::::: ##:::::::: ##:::: ##:
 #########: ##. ####: ##:::: ##: ##. ####: ##::::::: ##.... ##: #########:::: ##:::::::::: ##:::::::: ##:::: ##:
 ##.... ##: ##:. ###: ##:::: ##: ##:. ###: ##::: ##: ##:::: ##: ##.... ##:::: ##:::::::::: ##:::'###:. ##:: ##::
 ##:::: ##: ##::. ##:. #######:: ##::. ##:. ######:: ##:::: ##: ##:::: ##:::: ##::::::::'######: ###::. #####:::
..:::::..::..::::..:::.......:::..::::..:::......:::..:::::..::..:::::..:::::..:::::::::......::...::::.....::::

$ AUTHOR THE KING OF THE GLORY TELEGRAM -- https://t.me/TheKingOfTheGloryOfficall USE NGROK !! $
# SUALI OLAN TG YAZA BILER NGROKLA LOCAL XARICI CHAT ACA BILERSINIZ #
# OUR LEGAL TEAM -- TURANCYBERTEAM -- Want To Join Write Us #  
\33[0m      
""")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((NIP, NPORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except: 
            print("[-] SERVER DAYANDI !!")
            client.close()
            break

def write():
    while True:
        try:
            message = '\33[31m{}:\33[0m {}'.format(nickname, input('\n'))
            client.send(message.encode('ascii'))
        except Exception as w:
            print("[-] SISTEM NE YAZIQKI TURK VE AZERBAYCANCA KARAKTER DESTEKLEMIR ")

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()




