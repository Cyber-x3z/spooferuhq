#plz don't steal the prog, i know its "mid" but don't steal thx ! 

import os
import subprocess
import uuid
import socket
import getpass
import random
from faker import Faker
from colorama import Fore, Style, init
from pystyle import Write, Colors, Anime
from time import sleep
import webbrowser

os.system("title cyber spoofer")
webbrowser.open("https://x.com/cyberuhq")  #svp follow merci


init(autoreset=True)
fake = Faker()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def center_text(text):
    width = os.get_terminal_size().columns
    lines = text.split('\n')
    centered = "\n".join(line.center(width) for line in lines)
    return centered

def avertissement_clignotant():
    width = os.get_terminal_size().columns
    msg = "CETTE ACTION EST IRRÉVERSIBLE !"
    for _ in range(6):
        clear_screen()
        print("\n" * 5)
        print(Colors.yellow_to_red( msg.center(width) ))
        print("\n" * 3)
        sleep(0.5)
        clear_screen()
        print("\n" * 5)
        print(" ".center(width))
        print("\n" * 3)
        sleep(0.5)

def sauvegarder_identite_actuelle():
    hostname = socket.gethostname()
    user = getpass.getuser()
    mac_info = subprocess.getoutput("getmac").splitlines()[0]
    ip = socket.gethostbyname(hostname)
    with open("real_machine_identity.txt", "w") as f:
        f.write(f"Nom Machine: {hostname}\n")
        f.write(f"Nom Utilisateur: {user}\n")
        f.write(f"MAC: {mac_info}\n")
        f.write(f"IP: {ip}\n")

def changer_nom_pc(nouveau_nom):
    subprocess.run(f"wmic computersystem where name='%COMPUTERNAME%' call rename name='{nouveau_nom}'", shell=True)

def changer_mac_adresse():
    interface = subprocess.getoutput("getmac").splitlines()[0].split()[1]
    fake_mac = "02-%02X-%02X-%02X-%02X-%02X" % tuple(random.randint(0, 255) for _ in range(5))
    subprocess.run(f'PowerShell -Command "Set-NetAdapterAdvancedProperty -Name \'{interface}\' -DisplayName \'Network Address\' -DisplayValue \'{fake_mac}\'"', shell=True)
    return fake_mac

def spoof_machine():
    clear_screen()
    avertissement_clignotant()
    Write.Print(center_text("SPOOFING HARDWARE EN COURS...\n\n"), Colors.green_to_white, interval=0.008)
    sauvegarder_identite_actuelle()
    fake_hostname = fake.domain_word() + "-" + str(random.randint(1000,9999))
    changer_nom_pc(fake_hostname)
    mac = changer_mac_adresse()
    fake_uuid = str(uuid.uuid4())
    ip = socket.gethostbyname(socket.gethostname())

    with open("spoofed.txt", "w") as f:
        f.write(f"Nom Machine (spoofé): {fake_hostname}\n")
        f.write(f"Utilisateur: {getpass.getuser()}\n")
        f.write(f"UUID (fake): {fake_uuid}\n")
        f.write(f"MAC spoofée: {mac}\n")
        f.write(f"IP: {ip}\n")

    Write.Print(center_text("\nSpoofing effectué avec succès.\n"), Colors.green_to_cyan, interval=0.008)
    Write.Print(center_text("Redémarrage recommandé pour appliquer certains changements.\n"), Colors.red_to_yellow, interval=0.008)
    print("\n" * 2)
    print(center_text("Appuie sur Entrée pour quitter..."))
    input()

def main():
    clear_screen()
    banner = r"""
    
 ░▒▓███████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓███████▓▒░       ░▒▓█▓▒░      
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      
 ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓███████▓▒░       ░▒▓█▓▒░      
       ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      
       ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░                   
░▒▓███████▓▒░░▒▓█▓▒░       ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      
                                                                                                               
                                                                                                                                                                                             
                                                                                                                                                                 
    """
    Write.Print(center_text(banner) + "\n", Colors.purple_to_blue, interval=0.001)

    print("\n")
    Write.Print(center_text("Bienvenue dans le Spoofing Hardware UHQ\n"), Colors.red_to_white, interval=0.005)
    Write.Print(center_text("⚠️  ATTENTION: Cette action est irréversible et peut nécessiter un redémarrage.\n\n"), Colors.yellow, interval=0.005)
    Write.Print(center_text("[1] Lancer le spoofing complet\n[2] Quitter\n"), Colors.cyan, interval=0.005)
    choice = input(Fore.GREEN + center_text("Choix : "))
    if choice.strip() == "1":
        spoof_machine()
    else:
        Write.Print(center_text("Fermeture du programme..."), Colors.red, interval=0.005)
        sleep(1)
        clear_screen()

if __name__ == "__main__":
    main()