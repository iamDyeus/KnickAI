from speech import speak
import datetime
import wikipedia
import webbrowser
import time
import subprocess
import requests
import wolframalpha
import randomstuff
import os
import playsound
import winshell
import speech_recognition as sr
import pywhatkit
import keyboard
from inputmode import mode_select

def takeCommand():     
		print("Listening....")
		r = sr.Recognizer()
		r.dynamic_energy_threshold=False
		r.energy_threshold=4000
		r.pause_threshold = 1
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
			said=""
		try:
			print("Recognizing....")
			said = r.recognize_google(audio,language='en')
			print(f"You Said : {said}\n")
		except sr.UnknownValueError :
			print("could not understand audio \n~Trying Again~")
			return takeCommand()
		except sr.RequestError as e:
			print("Could not request results, check your internet connection; {0}".format(e))
			return "None"    
		return said.lower()

def takecommand_text():
    query=input(">> ")
    return query.lower()

def take_input(variable):
        if variable==0:
            return takecommand_text()
        elif variable==1:
            return takeCommand()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        playsound._playsoundWin(os.path.join('soundeffects\sfx',"gm.mp3"))
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        playsound._playsoundWin(os.path.join('soundeffects\sfx',"ga.mp3"))
        print("Hello,Good Afternoon")
    else:
        playsound._playsoundWin(os.path.join('soundeffects\sfx',"ge.mp3"))
        print("Hello,Good Evening")
    time.sleep(2)


def chat(conversation_mode):      #here conversation mode is referenced to either text or speech input
    with randomstuff.Client(api_key='YOUR-API-KEY-HERE') as client:  #API KEY REQUIRED HERE
        while True: 
            chat_message=take_input(conversation_mode)
            response = client.get_ai_response(chat_message,bot="Knick", master="Arsh")
            print(response.message)
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"notification.mp3"))
            if 'bye' in chat_message :
              break        
    time.sleep(1)

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])




#here is the exceution functions i made it, so that the main code looks a bit clean XD
def showmagic():
    knick_input_mode= mode_select()
    while True:
        playsound.playsound(os.path.join('soundeffects\sfx',"howcanihelpyounow.mp3"))
        print("\nTell Me How Can I Help you Now ?")
        statement=take_input(knick_input_mode)
        
        if statement==None:
            print("No Input Detected!\n")
            continue
        
        elif "good bye" in statement or "ok bye" in statement or "stop" in statement or "bye" in statement or "quit" in statement:

            playsound._playsoundWin(os.path.join('soundeffects\sfx',"shuttingdown.mp3"))
            print("\n")
            print('    Your Personal Assistant Knick is Shutting Down,Good bye.     ')
            playsound._playsoundWin(os.path.join('soundeffects\sfx','powerdown.mp3'))
            print("~   The BOT went Offline    ~")
            time.sleep(4)
            quit()
 
        elif "sleep" in statement:
            speak("Assistant Paused.")
            print("ok i am sleeping\nPress 'W' whenever You Want Me to Resume")
            print("   ")
            from console import assistant_pause,assistant_resumed
            print(assistant_pause)
            print("  ")
            while True :
                if keyboard.is_pressed('w'):
                    speak("Assistant Resumed.")
                    print(assistant_resumed)
                    print("  ")
                    break

        elif "hi" in statement or "hello" in statement :
            print("I am very seroius about my work,\nso if you wanna have chat with me. just use the 'Lets Chat' command ")
            #playsound._playsoundWin(os.path.join('soundeffects\sfx','replytohello.mp3'))
            time.sleep(1)

        elif "open youtube and search for" in statement or "open youtube and search" in statement:
                query=statement.split('open youtube and search for')
                srch=query
                print("Searching for : ",srch," on youtube")
                print("opening youtube...")
                sss=(f"https://www.youtube.com/results?search_query="+
                        "+".join(srch))
                pywhatkit.playonyt(sss)
                playsound._playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
                time.sleep(1)

        elif 'open youtube' in statement:
                print('Opening Youtube...')
                webbrowser.open_new_tab("https://www.youtube.com")
                time.sleep(3)
                print("youtube is open now.")
                playsound._playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
                time.sleep(5)
        
        elif 'open github' in statement:
            print('Opening GitHub...')
            webbrowser.open_new_tab("https://github.com/")
            print('GitHub is now Open.')
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            print("Google chrome is open now.")
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(5)

        elif "snipping tool" in statement:
            print("Opening Snipping Tool")
            os.system("start snippingtool")
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(5)

        elif "screenshot" in statement:
            import random
            time.sleep(1.5)
            import pyscreenshot
            image = pyscreenshot.grab()
            r = random.randint(1,20000000)
            file_name=("knickscreenshot"+ str(r) +".png")
            image.save(file_name)
            print("Screenshot saved as : ",file_name)
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(2)

        elif "handwriting" in statement:
            speak("Enter the text you want to Convert ?")
            vars=input("Enter the Text which you want to convert into Your Handwriting. \n>>")
            pywhatkit.text_to_handwriting(string=vars,save_to="handwriting.png")
            print("Your Text to HandWriting Conversion is Done!\nTIP: To check your Result, Check for handwriting.png File")
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(3)

        elif "image conversion" in statement :
            ima=input("Enter the Path of Image :")
            pywhatkit.image_to_ascii_art(imgpath=ima,output_file="knick_asciiart.txt")
            print("i have Made Your ASCII art and also saved it.")
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(3)

        elif "edge" in statement:
            print("Opening Microsoft Edge")
            os.system("start msedge")
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3")) 
            time.sleep(5)

        elif 'open whatsapp' in statement or 'whatsapp' in statement:
            webbrowser.open_new_tab('https://web.whatsapp.com/')
            print('opening WhatsApp Web')
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(6)

        elif 'open instagram' in statement or 'instagram' in statement:
            webbrowser.open_new_tab('https://www.instagram.com/')
            print('opening Instagram')
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(6)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            print("Google Mail is open now.")
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(5)

        elif 'open discord' in statement or 'discord' in statement:
            webbrowser.open_new_tab("https://discord.com/channels/@me")
            print("discord is open now.")
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(5)

        elif 'open facebook' in statement:
            print('opening facebook...')
            webbrowser.open_new_tab("https://www.facebook.com/")
            print('facebook is open now.')
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(5)

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            print("Here is stackoverflow")
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(3)

        elif 'clear cache' in statement or 'clear system cache' in statement or 'boost system' in statement:
            speak("Clearing system Cache....")
            speak("please do not touch anything for a while, the automated process is starting.")
            keyboard.press_and_release('win+R')
            keyboard.write("%temp%")
            time.sleep(0.4)
            keyboard.press_and_release("enter")
            print("clearing cache in process....")
            time.sleep(2)
            keyboard.press_and_release("ctrl+a")
            keyboard.press_and_release("del")
            time.sleep(0.7)
            keyboard.press_and_release("enter")
            print ('Starting the removal of the file !')
            print("If you see any Error, just select Do this for all and click Skip")
            speak("If you see any Error, just select Do this for all and click Skip")
            time.sleep(3)

        elif "open my inbox" in statement:
            webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(3)

        elif "open my sent mails" in statement or "open my sent mail" in statement:
            webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#sent")
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(3)

        elif 'open terminal' in statement or 'cmd' in statement:
            os.startfile ("cmd")
            print("Command Prompt is Open Now")
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(3)

        elif 'log off' in statement or 'sign out' in statement:
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"logoff.mp3"))
            subprocess.call(["shutdown", "/l"])
        
        elif "shutdown" in statement or "shut down" in statement:
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"logoff.mp3"))
            time.sleep(3)
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"shutdown.mp3"))
            time.sleep(3)
            os.system('shutdown/s')

        elif "restart my pc" in statement:
            speak("okay, restarting your pc")
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"logoff.mp3"))
            os.system('shutdown/r')
        
        elif 'date today' in statement or 'today date' in statement:
            from datetoday import today_date
            print(today_date())
            speak(today_date())
            time.sleep(3)
        
        elif "empty recycle bin" in statement:
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )
                speak("you should press enter if the dialog box appears.")
                time.sleep(1.3)
                speak("Recycle Bin Emptied")
                
        elif "note" in statement or "remember this" in  statement:
                print("What would you like me to write down?")
                note_text = take_input(knick_input_mode)
                note(note_text)
                speak("I have made a note of that.")

        elif "weather" in statement:
            api_key="YOUR-API-KEY-HERE"  #API KEY REQUIRED HERE
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"cityname.mp3"))
            print("\nwhats the city?")
            city_name= take_input(knick_input_mode)
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                
                print(" Temperature in kelvin unit = " +
                    str(current_temperature) +
                    "\nhumidity (in percentage) = " +
                    str(current_humidiy) +
                    "\ndescription = " +
                    str(weather_description))
                speak("Temperature in kelvin unit is " +
                    str(current_temperature) +
                    "\nhumidity in percentage is " +
                    str(current_humidiy) +
                    "\ndescription  " +
                    str(weather_description))

            else:
                speak(" City Not Found. ")
                print(" City Not Found ")

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            playsound._playsoundWin(os.path.join('soundeffects\sfx',"news.mp3"))
            time.sleep(6)

        elif "search on google" in statement:
                statement = statement.split("search on google")
                search = statement
                webbrowser.open("https://www.google.com/search?q=" + "+".join(search))
                speak("Searching " + str(search) + " on google")
                playsound._playsoundWin(os.path.join('soundeffects\sfx','taskcompleted.mp3'))
                time.sleep(3)

        elif 'ask' in statement:
            speak("I can answer to computational and geographical questions and what question do you want to ask now")
            query=take_input(knick_input_mode)
            client = wolframalpha.Client('YOUR-API-KEY-HERE') #API KEY REQUIRED HERE
            res = client.query(query)
            answer = next(res.results).text
            print(answer)

        elif 'wikipedia' in statement:
            speak("Searching Wikipedia about it...")
            statement =statement.replace("search on wikipedia about", "")
            try:
                results = wikipedia.summary(statement, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                speak("Unknown Error Occured, say your question again.")
                continue
        
        elif 'who is' in statement:
            try:
                speak("getting information from Wikipedia..")
                statement =statement.replace("who is","")
                results = wikipedia.summary(statement, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                speak("Enable to Fetch Data,try again.")
                continue

        elif "where is" in  statement:
                ind = statement.split().index("is")
                location = statement[ind + 8:]
                url = "https://www.google.com/maps/place/" + "".join(location)
                speak("This is where i found, " + str(location))
                webbrowser.open(url)    
                playsound._playsoundWin(os.path.join('soundeffects\sfx','taskcompleted.mp3'))
                time.sleep(3)

        elif 'yt studio' in statement or 'open yt studio' in statement:
            webbrowser.open_new_tab("https://studio.youtube.com/")
            speak("opening youtube creator studio")
            playsound._playsoundWin(os.path.join('soundeffects\sfx','taskcompleted.mp3'))
            time.sleep(5)

        elif 'live studio' in statement or 'livestream dashboard' in statement or 'live control room' in statement:
            webbrowser.open_new_tab('https://studio.youtube.com/channel/UCWe1CSEpVq_u6WDk3F7E2Mg/livestreaming/manage')
            speak("opening youtube livestream dashboard")
            playsound._playsoundWin(os.path.join('soundeffects\sfx','taskcompleted.mp3'))
            time.sleep(5)

        elif 'keyword' in statement or 'google trends' in statement or 'keyword research' in statement:
            speak("do you want me to open google trends for keyword research.")
            print('type yes or no for Opening Google Trends')
            gtask=input('>> ')
            if (gtask=='yes'):
                webbrowser.open_new_tab('https://trends.google.com/')
            elif(gtask=='no'):
                speak("ok, i will not open Google Trends.")
                print("OPENING GOOGLE TRENDS : Cancelled By User")
            playsound._playsoundWin(os.path.join('soundeffects\sfx','taskcompleted.mp3'))
            time.sleep(5)

        elif 'viewbot' in statement or 'livebot' in statement or 'view bot' in statement:
            playsound._playsoundWin(os.path.join('soundeffects\sfx','startingviewbot.mp3'))
            print("if you get any error in the viewbot or it doesn't work try updating the Assistant or \n vist the official website of knick assistant & check the ViewBot Page.")
            subprocess.call('viewbot\livebot.exe')
            time.sleep(3)
                
        elif 'how were you born' in statement  or 'why were you born' in statement:
            print('''
            I was born on june 2021 by A Boy Who Had an Ambition To Change This World with the
            Help Of Artificial Intelligence, Although i am still just a small step towards this
            new ERA of A.I . But I am still Happy to be Born and serve you right now''')
            playsound._playsoundWin(os.path.join('soundeffects\sfx','born.mp3'))
            time.sleep(3)
        
        elif 'who are you' in statement or 'what can you do' in statement:
            print('I am Knick your Persoanl AI assistant. I am programmed for managing normal tasks in your Life')
            speak("I am Knick your Persoanl AI assistant. I am programmed for managing normal tasks in your Life")
            time.sleep(3)

        elif 'your name' in statement or 'what is your name' in statement :
            speak("my name is knick, how could you forget me :-(")
            print('my name is knick your A.I assistant')
            time.sleep(3)

        elif 'what is your slogan' in statement or 'what is your motive' in statement:
            playsound._playsoundWin(os.path.join('soundeffects\sfx','slogan.mp3'))
            print('Leading Towards A Efficient Life.')
            time.sleep(3)
        
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by my great all mighty master, Arsh")
            print("I was built by Arsh")
            time.sleep(2)

        elif 'update knick' in statement or 'knick website' in statement:
            speak("opening The Official Website For Knick Assistant.")
            webbrowser.open_new_tab("https://knickassistant.wordpress.com/")
            speak("please manually check for any new Available verson.")
            time.sleep(4)

        elif 'tell commands' in statement or 'your commands' in statement  or 'command' in statement:
            speak("Telling you the list of my commands :")
            speak("below is the list of all commands respectively.")
            print('\n\nbelow is the list of all commands respectively')
            from console import command_list
            print(command_list)
            time.sleep(3)
        
        elif 'chat' in statement: 
            print('\nChat Feature is Still in ALPHA vesion,\nso please have patience while using it.')
            chat(knick_input_mode)
            time.sleep(3)
    
        elif 'play game' in statement:
            speak('opening mini games manager') 
            from minigames import minigamesmanager
            minigamesmanager.playgame()
            time.sleep(3)

        elif 'insult me' in statement:
            try:
                evil=requests.get(url='https://evilinsult.com/generate_insult.php?lang=en&type=json')
                data=evil.json()
                insult=data['insult']
                print(insult)
                speak(insult)
                time.sleep(2)
            except:
                speak("the insult generation server is down,you may try again later.")

        elif 'say' in statement or 'pronounce' in statement:
            speak("okay, type the text.")
            say=input('What you Want Me To Say : ')
            print('user entered :',say)
            speak(say)
            time.sleep(2)

        elif "change input mode" in statement:
            speak("ok, select the input mode again.")
            showmagic()

        elif "thanks" in statement:
            print("NP :)")
            speak("no problem, always there to help you.")

        elif "support assistance" in statement:
            speak("you can join the official discord server of knick, if you have any problem while using the assistant.")
            query=input("do you want to join the Discord Server for Assistance? (y/n)\n>> ")
            if query=="y":
                webbrowser.open_new_tab("https://discord.gg/2X4WThB64b")
                continue
            elif query=="n":
                print("ok : action cancelled by user")
                continue
            else:
                print("you need to select from 'y' or 'n' only, IDOT!")
                continue
        
        else:
            print('Unable to Read Your Command \nError: Unknown Command')
            playsound._playsoundWin(os.path.join('soundeffects\sfx','systemdown.mp3'))
            speak("i am sorry, my Responses are limited, you must ask the right question.")



