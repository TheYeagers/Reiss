import socket
pc_name = input("Type the host name --# ")
try:
    socket.gethostbyname(pc_name)
except:
    print("We cant find the host .")
print("we find the host")
