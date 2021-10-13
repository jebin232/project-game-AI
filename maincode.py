import os
import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import time

#this line is for datetime
now = datetime.now()
tim = now.strftime("%H:%M:%S")
print("Current Time =", tim)
#this line is for voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speech(so):
    engine.say(so)
    engine.runAndWait()
    engine.stop()
speech("welcome boss how can i help you")
speech("Current time")
speech(tim)
def bb():
    r = sr.Recognizer()
    r.energy_threshold = 300
    with sr.Microphone() as source:
        print("say anything:")
        audio = r.listen(source)
        time.sleep(3)
        print("listing.....")

    try:
        speech("wait for a moment")
        text = r.recognize_google(audio, language='en-in')
        print("you said:", text)
        speech("you said",text)
    except Exception as e:
        print(e)
        print("can you say it again ")
        speech("can you say it again please")
    return text

while True:
    text=bb()
    if "game" in text:
        speech("""you have two games 1==rps and 2==plants vs zombies
        say number one for rps ,say number 2 for plants vs zombies""")
    elif "open whatsapp" in text:
        os.startfile("C:\\Users\\LENOVO\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    elif "open google" in text:
        webbrowser.open('http://google.com', new=2)
    elif "open youtube" in text:
        webbrowser.open("https://www.youtube.com",new=2)
    elif "play songs" in text:
        import jj1
    elif "exit" in text:
        quit()
    elif "1" in text:
        import jack
    elif "2" in text:
        os.startfile("F:\\Plants vs Zombies\\plants vs zombies.exe")
    elif "___" in text:
        pass