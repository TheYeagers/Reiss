import socket
import datetime
from time import sleep
import os
import sys
sleep(1)
print("""
.d8888.  .d88b.   .o88b. db   dD d88888b d888888b      
88'  YP .8P  Y8. d8P  Y8 88 ,8P' 88'     `~~88~~'      
`8bo.   88    88 8P      88,8P   88ooooo    88         
  `Y8b. 88    88 8b      88`8b   88~~~~~    88         
db   8D `8b  d8' Y8b  d8 88 `88. 88.        88         
`8888Y'  `Y88P'   `Y88P' YP   YD Y88888P    YP         
""")
hostname=input("Host name --# ")
print("\n")
time.sleep(0.5)
try:
    ip=socket.gethostbyname(hostname)
except:
    print("We can find the host .")
    sleep(92718173)
print("IP: ", ip)
print("\n")
sleep(0.5)
deftime=int(input("DEFFULT TIME OUT (RECOMMENDED : 5) ; "))
print("\n")
time.sleep(0.5)
try:
    socket.setdefaulttimeout(deftime)
except:
    print("something went wrong")
    sleep(188381378137)
port=int(input("PORT: "))
print("\n")
sleep(0.5)
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    conn =sock.connect((ip, port))
except:
    print("maybe this port unavabile on this host, scan the host with NMAP too see which port avabile on this site .")
    time.sleep(9999999)
