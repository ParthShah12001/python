import speech_recognition as sr
from time import ctime
import time
import playsound
import os
import random
from gtts import gTTS
import webbrowser
r = sr.Recognizer()


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data=''
        try:
            voice_data = r.recognize_google(audio)
            print("-->" + voice_data)
        except sr.UnknownValueError:
           speak("Sorry, I did not get that")
        except sr.RequestError:
            speak("Sorry, my speech service is down")
        return voice_data

def respond(voice_data):
    if "what is your name" in voice_data:
        speak("My name is Friday")
    if "what time is it" in voice_data:
        speak(ctime())
    if "search" in voice_data:
        search = record_audio("What do you want me to search")
        url = "https://google.com/search?q="+search
        webbrowser.get().open(url)
        speak("Here's what I found about" + voice_data)
    if "find location" in voice_data:
        location = record_audio("what is the location")
        url = "https://google.nl/maps/place/"+location+'/&amp;'
        webbrowser.get().open(url)
        print("Here is the location of" + voice_data)
    if "bye" in voice_data:
        speak("ok bye")
        exit()

def speak(audio_string):
    tts = gTTS(text=audio_string,lang='en')
    r=random.randint(1,1000000)
    audio_file = 'audio--'+ str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


time.sleep(1)
speak("How can I help you?")
while(1):
    voice_data = record_audio()
    respond(voice_data)