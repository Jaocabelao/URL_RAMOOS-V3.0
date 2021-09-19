#!/usr/bin/python3
#Created by @jaoramoo

import os
from time import sleep
import pyshorteners


def banner():
    print("\033[93m--------------------------------------------")
    print("                URLRAMOO V3.0        fechar programa  CTRL+Z         ")
    print("                              ")
    print("   encurtar URL para engenharia social   ")
    print("--------------------------------------------")

def programm():
    os.system('clear')
    banner()
    print("\nColoque url que vai ficar visivel")
    original_domain = str(input("\nEx:facebook.com: "))

    os.system('clear') 
    
    banner()
    print("\ncoloque tags Exemplo: video-do-presidente-jair-messias-bolsonaro-falou")
    postlink = str(input("Postlink: "))

    os.system('clear')
    
    banner()
    url_to_short = str(input("coloque o link que você quer esconder:"))
    s = pyshorteners.Shortener()
    shorten=(s.dagd.short(f'{url_to_short}'))
    withoutprotocol = shorten[8:]
    
    os.system('clear')
    banner()
    print(f"\033[95m\nSeu link encurtado: https://{original_domain}-{postlink}@{withoutprotocol}")


    defanother()
    

def defanother():
    another=str(input("\033[93m\nconverter outro link? (S/N): ")) 
    if another == "s":
        programm()

    elif another == "n":
        exit()

    else:
        print("Retry")
        sleep(3)
        os.system('clear')
        defanother()

programm()


        
