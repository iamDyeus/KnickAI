import requests
import playsound
import time
from speech import speak


while True:
    evil=requests.get(url='https://evilinsult.com/generate_insult.php?lang=en&type=json')
    data=evil.json()
    insult=data['insult']
    print("knick :",insult)
    playsound._playsoundWin("ooh.mp3")
    speak(insult)
    time.sleep(1)
    print("Enter Your INSULT :")
    your_inp=input(">> ")
    if your_inp=="quit" or your_inp=="bye":
        print("thanks for playing this game!")
        break
