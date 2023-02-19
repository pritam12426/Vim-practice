import json
import os
import playsound
import colorama
import random

totle = 0
error = 0

keyName = ['Exit with out saving',
           'Save and exit', 
           'Just exit',
           'Just save',
           'Jump forword',
           'Jump back',
           'Delete iner word',
           'Delete single word',
           'Open Neo_vim']

shortKey = [':q!',
            ':wq',
            ':q',
            ':w',
            'w',
            'b',
            'diw',
            'dw',
            'nvim .']

while True:
    a = random.randint(0, len(keyName)-1)
    l = keyName[a]

    b = (f'**** {l} ****')
    print(b)
    j = input("Inset > ")

    if j.lower().find('exit') == 0:
        os.system("clear")
        exit(f'**** Result **** \nTotal attempt > {totle}\nTotal error > {error}\nCorrect attempt > {totle-error}\n'+"*"*22)

    elif j.lower().find("clear") == 0:
        os.system("clear")

    elif j != shortKey[a]:
        print('**** 🤬️ ****')
        print(f'Ans > {shortKey[a]}')
        print("=" *len(b))
        playsound.playsound("Error.wav")
        error +=1

    else:
        totle +=1
        print("=" *len(b))