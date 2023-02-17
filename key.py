import playsound
import random
n = 0

totle = 0
error = 0

while True:
    l = [':q!', ':qw', ':q', ':w']

    random.shuffle(l)
    l = l[0]

    print("-------------------")
    print(f'**** {l} ****')
    j = input("Inset > ")

    if j.lower().find('i') == 0:
        exit(f'\n**** Result **** \nTotal attempt > {totle}\nTotal error > {error}\nCorrect attempt > {totle-error}\n******************\n')

    elif j != l:
        print(f'**** {l} ****')
        playsound.playsound("Error.wav")
        erroe +=1
    totle +=1
