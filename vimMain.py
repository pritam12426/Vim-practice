permetion = input("Enter 'N' for Navigation \n'S' for Short cut mode\nInset > ")

if permetion.lower().find("n") == 0:
    import Navigation
    Navigation.Navigation()

elif permetion.lower().find("s") == 0:
    import shortCut
    shortCut.key()

else:
    print("Run it again")