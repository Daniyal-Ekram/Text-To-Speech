import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volume', 0.8)
engine.setProperty('voice', 'en-us')

text = input("Enter the text to convert to speech: ")

engine.say(text)
engine.runAndWait()