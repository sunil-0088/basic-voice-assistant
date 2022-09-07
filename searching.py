import speech_recognition as sr
# import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time




class searching:
    def __init__(self, statement, speak):

        if "time" in statement:
            tm = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {tm}")
            print(tm)

        elif "date" in statement:
            dt = time.strftime("%d %b %y")
            speak(f"the date is {dt}")
            print(dt)

        elif "wikipedia" in statement or "tell me about" in statement or "who is" in statement:
            speak('Searching Wikipedia...')

            if 'wikipedia' in statement:
                statement = statement.replace("wikipedia", "")
            elif 'tell me about ' in statement:
                statement = statement.replace("tell me about", "")
            elif "who is " in statement:
                statement = statement.replace("who is", "")
            try:
                results = wikipedia.summary(statement.capitalize(), sentences=3)
                
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception:
                try:
                    from googlesearch import search
                except ImportError:
                    print("No module named 'google' found")

                # to search
                query = statement

                for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                    print(j.description)


