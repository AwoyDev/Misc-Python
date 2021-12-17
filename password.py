from getpass import getpass
from dotenv import load_dotenv
import os
load_dotenv()

username = input("Enter username : ")
if username == os.getenv("USERNAME"):
    password = getpass("Enter password : ")
    if password == os.getenv("PASSWORD"):
        print(f"Bienvenue \033[1m{username}\033[m")
    else:
        print("Mauvais identifiants")