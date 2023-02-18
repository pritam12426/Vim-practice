from playsound import playsound
import random

print(' ⬆️ --> k\n', '⬇️ --> j\n', '➡️ --> l\n', '⬅️ --> h')

tole = 0
error = 0

while True:
    l = ['⬆️', '⬇️', '➡️', '⬅️']
    random.shuffle(l)
    l = l[0]
    print("-----------------------------------------------")
    print(f'\n  **** {l}  ****\n')
    j = input("Inset > ")

    if j == "i": 
        exit(f'\n**** Result **** \nTotal attempt > {tole}\nTotal error > {error}\nCorrect attempt > {tole-error}\n******************\n')

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

    tole +=1
