import socket
import ctypes  
import time
import random
from datetime import datetime

def get_clients():

    #info
    UDP_IP = "85.144.225.131"
    UDP_PORT = 20100
    padding = b"\xff\xff\xff\xff" 
    info = b"getinfo xxx\n"
    MESSAGE = padding + info

    #send packet
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    data = sock.recvfrom(1024)
    clients_connected = int(str(data).split("\\")[33])
    return clients_connected


def main():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if get_clients() > 0:
            print(f"{current_time} Players: {get_clients()}")
            if get_clients() >= 4:
                ctypes.windll.user32.MessageBoxW(0, f"Vier of meer spelers zijn verbonden", "-=|TeA|=- Hitman's Server Stalker", 0x00040000)
        time.sleep(600) #Check every 20 min


main()
