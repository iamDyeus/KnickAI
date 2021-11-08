#typewriter printing Animations For Knick Assistant
#btw not used this anywhere.
import time, sys

def tprint(str):

    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)









