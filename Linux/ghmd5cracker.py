#imports

import pyfiglet
import hashlib
import time
import os,sys
import colorama
from colorama import *


colorama.init()

flag = 0


os.system("clear")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")


print(Fore.RED + "                      <============================== INITIALIZING THE PROGRAM....... ==============================>            ")
time.sleep(3)
os.system("clear")


print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")

print("                                                                    Please wait...                                                      " + Fore.RESET)
time.sleep(5)


os.system("clear")

#logo
print(Fore.LIGHTBLUE_EX + "")
logo = pyfiglet.figlet_format("GH MD5 CRACKER         ")
print(logo)
print("-" * 60)
print("    Created By Mata | https://www.greekhacking.gr/     ")
print("    Donations:   paypal.me/vbourant    ")
print("-" * 60)
print("" + Fore.RESET)


#input

print(Fore.LIGHTYELLOW_EX + "")

wordlist = input("      Enter the wordlist PATH:   ")
print("")
hash2crack = input("      Enter the MD5 HASH: ")
print("" + Fore.RESET)


#file reading
try:

    wordlistlines = open(wordlist,"r").readlines()
except:
    print("No file Found!")
    sys.exit()

#looping
for i in range(0,len(wordlistlines)):
    hash2comp = hashlib.md5(wordlistlines[i].replace("\n","").encode()).hexdigest()
    print(Fore.RED + "  [-] " + Fore.WHITE + "<=================",str(hash2crack) + "   =   " + str(wordlistlines[i]) + "\n")
    time.sleep(1)

    #compare
    if hash2crack == hash2comp:
        print("")
        print(Fore.GREEN + "  [+] " + Fore.WHITE + "  Password Found:  " + Fore.RED + wordlistlines[i].replace("\n",""))
        print("")
        print("")
        print("")
        print("")
        print("")
        flag = 1
        break
        

