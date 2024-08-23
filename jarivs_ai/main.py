import os
import speech_recognition as sr
import webbrowser
import random
# using data.py for storing and using variables in it.
from data import sites, exit_greetings, welcome_greetings, responses, applications,modules,num,questions
from camera import use_camera;
from security import recognize_face
import sys
import subprocess
import datetime
# using config.py for storing and using variables in it.
from config import google_search, install_module
import requests
from googlesearch import search
import re

def google_search(query):
    """
    Open a web browser with Google search page populated with the provided query.

    Args:
        query (str): The search query string.
    """
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)



def say(text, rate=180):
    os.system(f'say -r {rate} {text}')

def user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except Exception as e:
            print("Error capturing audio:", e)
            return None
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service")
            return None
        except sr.UnknownValueError:
            print("I couldn,t able to understand audio")
            return None

def exit_program():
    exit_greeting = random.choice(exit_greetings)
    return exit_greeting

def welcom_program():
    welcome_greeting = random.choice(welcome_greetings)
    return welcome_greeting

def welcome_responses():
    return random.choice(responses)

def current_time():
    h=datetime.datetime.now().strftime("%H")
    if (int(h)==00):
        h=12
    if(int(h)>12):
        h=int(h)-12
    else:
        pass
    m=datetime.datetime.now().strftime("%M")
    strtime=(f"Current time is: {h}:{m}")
    return strtime

say(welcom_program())
n1 = None
n2 = None
security = recognize_face()
while True:
    if security == True:
        query=user_input()
        if query is not None:
            if f"exit".lower() in query.lower():
                say(f"{exit_program()}...")
                exit()
                
            elif f"time".lower() in query.lower():
                print(current_time())
                say(current_time())

            elif f"camera".lower() in query.lower():
                say(f"Opening Camera sir.")
                use_camera()
            
            elif f"thank".lower() in query.lower():
                say(f"{welcome_responses()}")
            
            for n in num:
                if f" {str(n)}" in query.lower():
                    numbers = re.findall(r'\d+', query)
                    num1 = int(numbers[0])
                    num2 = int(numbers[1])
                    result = num1 + num2
                    print(result)
                    say(result)

            for site in sites:
                if f"open {site[0]}".lower() in query.lower():
                    say(f"Opening {site[0]} sir.")
                    webbrowser.open(site[1])
                    break

            for module in modules:
                if f"install {module}".lower() in query.lower():
                    say(f"installing {module} in your mac sir")
                    install_module(module)
                    break 
            
            for question in questions:
                if question.lower() in query.lower():
                    results = google_search(query)
                    say(f"Finding on google..")
                    break
        
