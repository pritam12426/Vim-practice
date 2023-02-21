import os

from playsound import playsound
import random
from os import system

print(' ⬆️ --> k\n', '⬇️ --> j\n', '➡️ --> l\n', '⬅️ --> h')

tole = 0
error = 0

while True:
    l = ['⬆️', '⬇️', '➡️', '⬅️']
    random.shuffle(l)
    l = l[0]
    print(f'\n  **** {l}  ****\n')
    j = input("Inset > ")

    if j is "exit":
        os.system("clear")
        exit(f'\n**** Result **** \nTotal attempt > {tole}\nTotal error > {error}\nCorrect attempt > {tole-error}\n'+'*'*22)

    elif j is "clear":
        system("clear")
    elif l == '⬆️' and j.lower() != "k":
        playsound("Error.wav")
        error +=1

    elif l == '⬇️' and j.lower() != "j":
        playsound("Error.wav")
        print('\t**** j ****')
        error +=1

    elif l == '➡️' and j.lower() != "l":
        playsound("Error.wav")
        print('\t**** l ****')
        error +=1

    elif l == '⬅️' and j.lower() != "h":
        playsound("Error.wav")    
        print('\t**** h ****')
        error +=1

    else:
        print('='*5)
        tole +=1