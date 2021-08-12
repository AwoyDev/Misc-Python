#Work only on MacOs

import os

appname = input("Que voulez-vous ouvrir ?\n")

os.system(f"open -a {appname}")
