#installed PYTTSX module which is just text-to-speech using python
import pyttsx3
engine = pyttsx3.init()
engine.say('''Hello I am Aayush Gorle
This is my code
Twinkle Twinkle, Little Stars
How i wonder what you are?''')
engine.runAndWait()