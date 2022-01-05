import sys
sys.path.append('scripts/')


from console import intro_header
import time
#assistant directly works without giving introduction or any other shit.
def start_from_hibernation():
    print(intro_header)
    from standardfunctions import wishMe
    wishMe()
    time.sleep(1)
    from FeatureExecution import showmagic
    showmagic()

if __name__ == '__main__':
    start_from_hibernation()



