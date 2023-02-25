from time import sleep
import json
import os
import playsound
from colorama import Fore, init, Back
import random

init(autoreset=True)

#os.system("clear")

totle = 0
error = 0

json_file = open("shortKey.json")
json_file = json.load(json_file)
class Key:
    while(True):
        jsonKey = list(json_file.keys())
        jsonKey = random.choice(jsonKey)

        b = (f'**** {Fore.GREEN+jsonKey}')
        print(b,end=" ****\n")
        j = input("Inset > ")

        if j.lower().find('exit') == 0:
            os.system("clear")
            exit(f'==== Result ==== \n{Fore.YELLOW}Total attempt > {totle}\n{Fore.RED}Total error > {error}\n{Fore.GREEN}Correct attempt > {totle-error}\n{Fore.WHITE}'+"_-"*11 +':)')

        elif j.lower().find("clear") == 0:
            os.system("clear")
            print(f'==== Result ====\n{Fore.YELLOW}Total attempt > {totle}\n{Fore.RED}Total error > {error}\n{Fore.GREEN}Correct attempt > {totle-error}\n{Fore.WHITE}'+"-_"*11)
            sleep(2)
            os.system("clear")

        elif j != json_file[jsonKey]:
            print(Fore.RED + '**** Error ****')
            print(f'{Fore.CYAN}Correct key is > {json_file[jsonKey]}')
            print(Fore.RED + "=" * len(b))
            playsound.playsound("Error.wav")
            error +=1
            totle +=1
        else:
            totle +=1
            print(Fore.CYAN+ "=" * len(b))
