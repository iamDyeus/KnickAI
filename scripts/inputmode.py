import time
import keyboard
from speech import speak
import speech_recognition as sr
from rich import print


def mode_select():
	speak("please select an input Mode.")
	print("Please Select in wich input Mode you want to Use the Assistant :  ")
	print("1.Press 't' for Text Input Mode\n2.Press 's' for Speech Input Mode ")

	while True : 
		if keyboard.is_pressed('t'):
			print('You have successfully Selected : Text Input Mode')
			speak("text input Mode Selected.")
			mode_var= 0
			time.sleep(0.6)
			break
		elif keyboard.is_pressed('s'):
			print('You have successfully Selected : Speech Input Mode')
			speak("speech input Mode Selected.")
			mode_var= 1
			time.sleep(0.6)
			break		    
	return mode_var

#sample how it will be used for selecting modes : 
'''
a=mode_select()
if a==0:
	#takecommandti()
	print("things related to text input happen in main script :)")
elif a==1:
	#takecommandsi()	
	print("things related to speech_input happen in main script :)")
'''








