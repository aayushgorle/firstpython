#installed PYTTSX module which is just text-to-speech using python
# make sure to install pyttsx3 module from terminal to make the code work
import pyttsx3
engine = pyttsx3.init()
engine.say('''Hello I am Aayush Gorle
This is my code
Twinkle Twinkle, Little Stars
How i wonder what you are?''')
engine.runAndWait()
