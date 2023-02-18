import playsound
import random
n = 0

totle = 0
error = 0

while True:
    keyName = ['Exit wihtout saving', 'Save and exit', 'Just exit', 'Just save', 'Jump forword', 'Jump back', 'Delete iner word', 'Delete single word']
    shortKey = [':q!', ':wq', ':q', ':w', 'w', 'b', 'diw', 'dw', ]

    a = random.randint(0, 7)
    l = keyName[a]

    print("-------------------")
    print(f'**** {l} ****')
    j = input("Inset > ")

    if j.lower().find('i') == 0:
        exit(f'\n**** Result **** \nTotal attempt > {totle}\nTotal error > {error}\nCorrect attempt > {totle-error}\n******************\n')

    elif j != shortKey[a]:
        print(f'**** 🤬️ ****')
        print(shortKey[a])
        playsound.playsound("Error.wav")
        error +=1
    totle +=1