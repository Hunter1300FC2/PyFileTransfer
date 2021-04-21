import os
import socket
import time
from colorama import Fore
import tqdm

os.system("cls")
ascii_banner = f"""
   _____  _  _               _
  / ____|| |(_)             | |
 | |     | | _   ___  _ __  | |_
 | |     | || | / _ \| '_ \ | __|
 | |____ | || ||  __/| | | || |_
  \_____||_||_| \___||_| |_| \__|


"""
print(f"{Fore.RED}{ascii_banner}{Fore.WHITE}")
print(f"\n{Fore.BLUE}[!] Using version 0.2{Fore.WHITE}")
print(f"{Fore.BLUE}[!] This tools is made for local transfers.{Fore.WHITE}")
print(f"{Fore.BLUE}[!] To send a folder; zip the folder and then send the zipped file.{Fore.WHITE}")
server_port = 1300
BUFFER_SIZE = 4096

def get_file():
    file_name = input(f"\n{Fore.YELLOW}[*] Enter file to transfer (eg. example.py):{Fore.WHITE} ")
    # TO DO: VERIFY IF FILE IS THERE
    print(f"\n{Fore.GREEN}[+] '{file_name}' loaded and ready to be sent.{Fore.WHITE}")
    server_ip = input(f"\n{Fore.YELLOW}[*] Enter server IP:{Fore.WHITE} ")
    print(f"\n{Fore.GREEN}[+] Targeting '{server_ip}'.{Fore.WHITE}")
    confirm = print(f"\n{Fore.YELLOW}[*] Press enter to continue:{Fore.WHITE} ")
    send_file(server_ip, file_name)

def send_file(server_ip, file_name):
    filesize = os.path.getsize(file_name)
    s = socket.socket()
    s.connect((server_ip, server_port))
    s.send(f"{file_name}|{filesize}".encode())
    progress = tqdm.tqdm(range(filesize), f"\nSending {file_name}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(file_name, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            s.sendall(bytes_read)
            progress.update(len(bytes_read))
        s.close()
        print(f"\n\n{Fore.GREEN}[+] File sent.{Fore.WHITE}")
        confirm = input(f"\n{Fore.YELLOW}[*] Press enter to exit: {Fore.WHITE}")

get_file()
