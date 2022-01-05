import time
import playsound
import os
from rich.progress import Progress
from speech import speak
from api_keys import *
from rich import print

#actually this has no use and is just a showpiece for now.
# + it probably wastes time on startup too. xD


def check_for_api_keys(): #if you wa to run without api keys, just comment this function call below.
    if weather_api_key == "YOUR-API-KEY-HERE" or wolfram_api_key == "YOUR-API-KEY-HERE": 
        speak("Found Missing A P I keys.")
        print("\n\n[red]You have not yet set your API keys. Please add them to the api_keys.py file First.")
        time.sleep(3)
    else:
        pass

def enginestart():
    playsound._playsoundWin('soundeffects\sfx\startingengine.mp3')
    time.sleep(0.5)
    with Progress() as progress:
        task1 = progress.add_task("[red]Starting Engine...", total=200)
        task2 = progress.add_task("[green]Initialising Modules...", total=300)
        task3 = progress.add_task("[cyan]Importing all Prefrences...", total=100)
        while not progress.finished:
            progress.update(task1, advance=0.9)
            progress.update(task2, advance=0.9)
            progress.update(task3, advance=0.9)
            time.sleep(0.02)
    check_for_api_keys()
    speak("engine successfully started.")
    time.sleep(0.6)
    os.system('cls' if os.name == 'nt' else 'clear')







