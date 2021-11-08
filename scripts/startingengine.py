import time
import playsound
import os
from rich.progress import Progress
from speech import speak


def enginestart():
    playsound._playsoundWin('soundeffects\sfx\startingengine.mp3')
    time.sleep(0.5)
    with Progress() as progress:

        task1 = progress.add_task("[red]Starting Engine...", total=200)
        task2 = progress.add_task("[green]Initialising Modules...", total=345)
        task3 = progress.add_task("[cyan]Importing all Prefrences...", total=100)
        while not progress.finished:
            progress.update(task1, advance=0.9)
            progress.update(task2, advance=0.9)
            progress.update(task3, advance=0.9)
            time.sleep(0.02)
    speak("engine successfully started.")
    time.sleep(0.6)
    os.system('cls' if os.name == 'nt' else 'clear')







