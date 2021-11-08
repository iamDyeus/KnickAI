#still in progress will be ready soon!

import time


def playgame():
    print("\nNOTE : this is a BETA feature,and can make the assistant not working properly")
    print('Which Game Would you like to play Today :')
    print(''' 
    list of available games:
            \n1.Insult Battle
            \n2.bagels
            \n3.cannon
            \n4.bounce
            \n5.connect
            \n6.flappy
            \n7.simonsays
            \n8.tron

        OR type "quit" to exit gamemanager.

             ''')
    
    uinp=input("Enter the number in front of the game you'll like to play\n>>")
    
    if '1' in uinp :
        from games import insultbattle
    

    elif '2' in uinp:
        from games import bagels
    
    elif '3' in uinp:
        from games import cannon

    elif '4' in uinp:
        from games import bounce

    elif '5' in uinp:
        from games import connect

    elif '6' in uinp:
        from games import flappy
    
    elif '7' in uinp:
        from games import simonsays
    
    elif '8' in uinp:
        from games import tron

    elif uinp>8:
        print('this slot is empty... Pay Dev to Add More Games XD')

    elif uinp=="quit":
        quit()

    else:
        print('you need to choose a number from the list above NOOB! ')
        return playgame
    time.sleep(3)



playgame()
#after running this contine use krna,