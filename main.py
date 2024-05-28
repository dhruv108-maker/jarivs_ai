import os
import speech_recognition as sr
import webbrowser
import random
# using data.py for storing and using variables in it.
from data import sites, exit_greetings, welcome_greetings, welcome_responses, applications,modules
import cv2
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
            print("Google Speech Recognition could not understand audio")
            return None

def use_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return
    try:
        while True:
            ret, frame = cap.read()
            
            cv2.imshow('Camera', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

def exit_program():
    exit_greeting = random.choice(exit_greetings)
    return exit_greeting
    sys.exit() 

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
    strtime=(f"{h}:{m}")
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
    query = user_input()
    if query is not None:
        print("Processing...")
        if "exit" in query.lower():
            say(f"{exit_program()}, sir")
            exit()
        found = False
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                print(f"Opening {site[0]}, sir")
                say(f"Opening {site[0]}, sir")
                webbrowser.open(site[1])
                found = True
                break
                if not found:
                    print("Website not found sir.")
                    say("Website not found sir.")
        if f"Jravis" is query:
            print("Yes sir")
            say("Yes sir")

        if f"Open camera".lower() in query:
            print("Opening camera, sir")
            say("Opening camera,sir")
            use_camera()

        if f"time".lower() in query:
            print(f"Current time is {current_time()}")
            say(f"Current time is {current_time()}")

        if f"Thank You Jarvis".lower() in query:
            print(welcome_responses())
            say(welcome_responses())

        for module in modules:
            if f"install {module}".lower() in query.lower():
                print(f"Installing {module}, sir")
                say(f"Installing {module}, sir")
                install_module(module)
                found = True
                break
        if not found:
            print("Module not found, sir.")
            say("Module not found, sir.")
            pass

        for application in applications:
            if f"open {application[0]} app".lower() in query.lower():
                print(f"Opening {application[0]}, sir")
                say(f"Opening {application[0]}, sir")
                try:
                    subprocess.run(["open", application[1]], check=True)
                    found = True
                    break
                except subprocess.CalledProcessError as e:
                    print(f"Failed to open {application[0]}: {e}")
                    say(f"Failed to open {application[0]}, sir.")
                    found = True
                    break
        if not found:
            print("Application not found, sir.")
            say("Application not found, sir.")
            pass

    else:
        print("No input received. Please try again.")