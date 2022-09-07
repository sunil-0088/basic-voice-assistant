import speech_recognition as sr
# import pyttsx3
import datetime
# import wikipedia
# import webbrowser
# import os
# import time
# import subprocess
# from capture import capture as ec
# import wolframalpha
# import json
# import requests
import searching as search
import voice_properties as vp

vp.voice_rate(165)  # 0 to between 200
vp.voice_type(1)  # 0 for male 1:for female


def speak(text):
    vp.engine.say(text)
    vp.engine.runAndWait()


def wish():
    hr = datetime.datetime.now().hour

    if 0 <= hr < 12:
        print("Hello, Good Morning Sir")
        speak("Hello, Good Morning Sir")
    elif 12 <= hr < 18:
        print("Hello, good afternoon sir ")
        speak("Hello, good afternoon sir ")
    else:
        print("hello, good night sir")
        speak("hello, good night sir")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception:
            speak("sorry, please say that again")
            return "None"
        return statement


if __name__ == '__main__':
    print("Loading your AI personal assistant veronika")
    speak("Loading your AI personal assistant veronika")

    wish()

    speak("how can I help you ")

    while True:
        statement = takeCommand().lower()
        speak(statement)

        if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
            print("Your AI personal assistant is shutting down")
            speak("Your AI personal assistant is shutting down")
            break
        else:
            search.searching(statement,speak)

        if statement == 0:
            continue
