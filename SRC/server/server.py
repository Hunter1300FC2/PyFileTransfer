import socket
import tqdm
import os
from colorama import Fore

os.system("cls")
ascii_banner = f"""
   _____
  / ____|
 | (___    ___  _ __ __   __ ___  _ __
  \___ \  / _ \| '__|\ \ / // _ \| '__|
  ____) ||  __/| |    \ V /|  __/| |
 |_____/  \___||_|     \_/  \___||_|


"""
print(f"{Fore.RED}{ascii_banner}{Fore.WHITE}")
print(f"\n{Fore.BLUE}[!] Using version 0.2{Fore.WHITE}")
print(f"{Fore.BLUE}[!] This tools is made for local transfers.{Fore.WHITE}")
hostname = socket.gethostname()
SERVER_HOST = socket.gethostbyname(hostname)
SERVER_PORT = 1300

BUFFER_SIZE = 4096
s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"\n{Fore.YELLOW}[*] Listening as {SERVER_HOST}:{SERVER_PORT}{Fore.WHITE}")
client_socket, address = s.accept()
print(f"\n{Fore.GREEN}[+] {address} is connected.{Fore.WHITE}")
print(" ")
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split("|")
filename = os.path.basename(filename)
filesize = int(filesize)
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
    while True:
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        f.write(bytes_read)
        progress.update(len(bytes_read))
client_socket.close()
s.close()
print(f"\n\n{Fore.GREEN}[+] File recieved.{Fore.WHITE}")
confirm = input(f"\n{Fore.YELLOW}[*] Press enter to exit: {Fore.WHITE}")
