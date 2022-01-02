#this file uses a .pyw extension to run in the background

import os
import speech_recognition as sr

def background_listening():
		print("Listening in background....")
		r = sr.Recognizer()
		r.dynamic_energy_threshold=False
		r.energy_threshold=4000
		r.pause_threshold = 0.5
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
			said=""
		try:
			print("Recognizing in background....")
			said = r.recognize_google(audio,language='en')
			print(f"You Said : {said}\n")
		except sr.UnknownValueError :
			print("\n~Trying Again~")
			return background_listening()
		except sr.RequestError as e:
			print("Could not request results, check your internet connection; {0}".format(e))
			return "None"    
		return said.lower()

def desktop_notification(text_for_notification,duration_of_notification):
    # import win10toast
    from win10toast import ToastNotifier
    # create an object to ToastNotifier class
    n = ToastNotifier()
    n.show_toast("KnickAI",text_for_notification, duration = duration_of_notification)

hotword="assistant activate"
hotword2="wake up assistant"

def work_in_background():
	desktop_notification("Assistant running in background",5)
	while True:
		Listening=background_listening()
		if hotword in Listening or hotword2 in Listening:
			desktop_notification("Assistant is now running in foreground",4)
			os.system("python scripts/Hotword/assistant_direct.py")
			break
		else:
			continue  


if __name__ == '__main__':
	work_in_background()


#Note : if you run this file individually, then you may receive an error because of the directory structure.
# 	 To fix this, run this file from the main directory of the project. i.e run knickassistant.py 
#  or
#    change the line 44 ( i.e scripts/Hotword/assistant_direct.py) to ("python Hotword/assistant_direct.py") 