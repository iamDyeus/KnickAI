import time


def playgame():
    print('Which Game Would you like to play Today :\n')
    print(''' 
    List of Available Games:
    \n1.Venge.io
    \n2.Smashkarts.io
    \n3.Skribbl.io
    \n4.Chess
    \n5.Drift Hunters
    \n6.Ninja.io

        OR type "quit" to exit gamemanager.
        or type "help" to get help on how to use gamemanager.

             ''')
    
    uinp=input("Enter the number in front of the game you'll like to play\n>>")
    
    if '1' in uinp or 'Venge' in uinp or 'venge' in uinp or 'Venge.io' in uinp or 'venge.io' in uinp:
        from games import venge
    
    elif '2' in uinp or 'Smashkarts' in uinp or 'smashkarts' in uinp or 'Smashkarts.io' in uinp or 'smashkarts.io' in uinp:
        from games import smashkarts
    
    elif '3' in uinp or 'Skribbl' in uinp or 'skribbl' in uinp or 'Skribbl.io' in uinp or 'skribbl.io' in uinp:
        from games import skribbl

    elif '4' in uinp or 'Chess' in uinp or 'chess' in uinp:
        from games import chess

    elif '5' in uinp or 'Drift' in uinp or 'drift' in uinp or 'Drift Hunters' in uinp or 'drift hunters' in uinp:
        from games import drifthunters

    elif '6' in uinp or 'ninja' in uinp or 'ninja.io' in uinp:
        from games import ninja
    
    elif 'help' in uinp or 'Help' in uinp or 'HELP' in uinp:
        print("its so easy already, just type the number in front of the game you want to play")
        print("your such an amazing person, you can't even type the number of the game you want to play")
        print("so just type the name of the game you want to play and it will work")

    elif uinp=="quit" or uinp=="Quit":
        quit()

    else:
        print('You need to choose a Number/Name from the list above, You NOOB! ')
        print('\n')
        return playgame()
    time.sleep(3)


if __name__ == "__main__":
    playgame()