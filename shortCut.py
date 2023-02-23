import json
import os
import playsound
import colorsys
import random

os.system("clear")

totle = 0
error = 0

json_file = open("shortKey.json")
json_file = json.load(json_file)

while(True):
    jsonKey = list(json_file.keys())
    jsonKey = random.choice(jsonKey)

    b = (f'**** {jsonKey} ****')
    print(b)
    j = input("Inset > ")

    if j.lower().find('exit') == 0:
        os.system("clear")
        exit(f'**** Result **** \nTotal attempt > {totle}\nTotal error > {error}\nCorrect attempt > {totle-error}\n'+"*"*22)

    elif j.lower().find("clear") == 0:
        os.system("clear")

    elif j != json_file[jsonKey]:
        print('**** 🤬️ ****')
        print(f'Ans > {json_file[jsonKey]}')
        print("=" * len(b))
        playsound.playsound("Error.wav")
        error +=1
        totle +=1
    else:
        totle +=1
        print("=" * len(b))