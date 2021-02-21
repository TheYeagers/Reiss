import socket
print("""
.d8888.  .d88b.   .o88b. db   dD d88888b d888888b      
88'  YP .8P  Y8. d8P  Y8 88 ,8P' 88'     `~~88~~'      
`8bo.   88    88 8P      88,8P   88ooooo    88         
  `Y8b. 88    88 8b      88`8b   88~~~~~    88         
db   8D `8b  d8' Y8b  d8 88 `88. 88.        88         
`8888Y'  `Y88P'   `Y88P' YP   YD Y88888P    YP         
host = "0.0.0.0"
port = 8080
""")

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port2 = port.connet_ex((host,port))
if b == 0:
    print("You are connected")
else:
    print("You are not connected")
