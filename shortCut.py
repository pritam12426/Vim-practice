import json
import os
import playsound
import colorsys
import random

n = random.randint(1, 99)

os.system("clear")

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
           'Open Neo_vim here',
           'Undo',
           'Delete iner ""', 
           'Delete iner ()',
           'Change whole line',
           'Change iner word',
           'Jump end of the word',
           f'Jump to line number {n}',
           'Jump to ending of the line',
           'Jump to starting of the line',
           'Jump to begning of the file',
           'Jump to ending of the file']

shortKey = [':q!',
            ':wq',
            ':q',
            ':w',
            'w',
            'b',
            'diw',
            'dw',
            'nvim .',
            'u',
            'di"',
            'di(',
            'cc',
            'ciw',
            'e',
            f'{n}g',
            '0',
            '$',
            'gg',
            'G']

if len(shortKey) != len(keyName):
    print(f"The len of word {len(keyName)}")
    print(f"The len of short key {len(shortKey)}")
    exit("Pls check the key it is not propre")

while(True):
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
        print("=" * len(b))
        playsound.playsound("Error.wav")
        error +=1

    else:
        totle +=1
        print("=" * len(b))