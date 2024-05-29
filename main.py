import os
import speech_recognition as sr
import webbrowser
import random
# using data.py for storing and using variables in it.
from data import sites, exit_greetings, welcome_greetings, welcome_responses, applications,modules
from camera import use_camera;
import sys
import subprocess
import datetime
# using config.py for storing and using variables in it.
from config import api_key

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
    response=random.choice(welcome_responses)
    return(response)

def current_time():
    h=datetime.datetime.now().strftime("%H")
    if(int(h)>12):
        h=int(h)-12
    else:
        pass
    m=datetime.datetime.now().strftime("%M")
    strtime=(f"Current time is: {h}:{m}")
    return strtime

def install_module(module_name):
    """
    Install a Python module using pip.
    
    :param module_name: The name of the module to install.
    """
    try:
        subprocess.run(["pip", "install", module_name], check=True)
        print(f"Module {module_name} installed successfully.")
        say(f"Module {module_name} installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install module {module_name}: {e}")
        say(f"Failed to install module {module_name}.")

say(welcom_program())

while True:

    query=user_input()
    found=False
    m=False
    if query is not None:
        if f"exit".lower() in query.lower():
            say(exit_program())
            exit()
            
        elif f"time".lower() in query.lower():
            print(current_time())
            say(current_time())

        elif f"camera".lower() in query.lower():
            say(f"Opening Camera sir.")
            use_camera()

        elif f"thank".lower() in query.lower():
            print(welcome_responses())
            say(welcome_responses())

        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir.")
                webbrowser.open(site[1])
                found=True
                break

        for module in modules:
            if f"install {module[0]}".lower() in query.lower():
                say(f"installing {module[0]} in your mac sir")
                install_module(module[0])
                m=True
                break        

