import pyttsx3                                    # converts text to speech
import datetime                                   # required to resolve any query regarding date and time
import speech_recognition as sr                   # required to return a string output by taking microphone input from the user
import wikipedia                                  # required to resolve any query regarding wikipedia
import webbrowser                                 # required to open the prompted application in web browser
import os.path                                    # required to fetch the contents from the specified folder/directory
import smtplib                                    # required to work with queries regarding e-mail


engine = pyttsx3.init('sapi5')                    # sapi5 is an API and the technology for voice recognition and synthesis provided by Microsoft
voices = engine.getProperty('voices')             # gets you the details of the current voices
engine.setProperty('voice',voices[1].id)          # 0-male voice , 1-female voice



def speak(audio):                                # function for assistant to speak
    engine.say(audio)
    print("murali")
    engine.runAndWait()                          # without this command, the assistant won't be audible to us



def wishme():                                    # function to wish the user according to the daytime
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')

    elif hour>12 and hour<18:
        speak('Good Afternoon')

    else:
        speak('Good Evening')

    speak('Hello Sir, I am Daisy, your Artificial intelligence assistant. Please tell me how may I help you')


def takecommand():                               # function to take an audio input from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 2
        audio = r.listen(source)


    try:                                            # error handling
        print('Recognizing...')
        query = r.recognize_google(audio,language = 'en-in')  # using google for voice recognition
        print(f'User said: {query}\n')

    except Exception as e :
        print('Say that again please...')        # 'say that again' will be printed in case of improper voice
        return 'None'  
    return query

def sendemail(to,content):                       # function to send email
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('muraliprakashk2430@gmail.com','lesmukpkelrzamsy')
    server.sendmail('muraliprakashk2430@gmail.com',to,content)
    server.close()


if __name__ == '__main__' :                      # execution control
    wishme()
    while True:
        query = takecommand().lower()  # converts user asked query into lower case

        # The whole logic for execution of tasks based on user asked query

        if 'wikipedia' in query :
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences = 5)
            print(results)
            speak(results)

        elif 'open youtube' in query :
            webbrowser.open('youtube.com')

        elif 'open google' in query :
            webbrowser.open('google.com')

        elif 'play music' in query :
            speak('okay boss')
            music_dir = 'music_dir_of_the_user'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))


        elif 'time' in query :
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir the time is {strtime}')


        elif 'open stack overflow' in query :
            webbrowser.open('stackoverflow.com')

        elif 'open free code camp' in query :
            webbrowser.open('freecodecamp.org')

        elif 'open notepad' in query :
            codepath = 'C:\Windows\System32/notepad.exe'
            os.startfile(codepath)

        elif 'email' in query :
            try:
                speak('what should i write in the email?')
                content = takecommand()
                speak('Enter your mail id please!!!')
                to = input("What is your email address? ")
               
                # to = 'reciever_email@gmail.com'
                sendemail(to, content)
                speak('email has been sent')
            except Exception as e:
                print(e)
                speak('Sorry, I am not able to send this email')

        elif 'exit' in query:
            speak('okay boss, please call me when you need me')
            quit()



################################################
#system lock function#

import subprocess
cmd='rundll32.exe user32.dll, LockWorkStation'
subprocess.call(cmd)

################################################

##### New unlock windows assistent code ###########

import pyttsx3                                    # converts text to speech
import datetime                                   # required to resolve any query regarding date and time
import speech_recognition as sr                   # required to return a string output by taking microphone input from the user
import wikipedia                                  # required to resolve any query regarding wikipedia
import webbrowser                                 # required to open the prompted application in web browser
import os.path                                    # required to fetch the contents from the specified folder/directory
import smtplib 
import subprocess
from ctypes import *

engine = pyttsx3.init('sapi5')                    # sapi5 is an API and the technology for voice recognition and synthesis provided by Microsoft
voices = engine.getProperty('voices')             # gets you the details of the current voices
engine.setProperty('voice',voices[1].id)  
windll.user32.BlockInput(True)        # 0-male voice , 1-female voice



def speak(audio):                                # function for assistant to speak
    engine.say(audio)
    engine.runAndWait()                          # without this command, the assistant won't be audible to us



def wishme():                                    # function to wish the user according to the daytime
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')

    elif hour>12 and hour<18:
        speak('Good Afternoon')

    else:
        speak('Good Evening')

    speak('Hello Sir, I am Alexsa, your Artificial intelligence assistant. Please tell me how may I help you')


def takecommand():                               # function to take an audio input from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 2
        audio = r.listen(source)


    try:                                            # error handling
        print('Recognizing...')
        query = r.recognize_google(audio,language = 'en-in')  # using google for voice recognition
        print(f'User said: {query}\n')

    except Exception as e :
        print('Say that again please...')        # 'say that again' will be printed in case of improper voice
        return 'None'  
    return query

if __name__ == '__main__' :                      # execution control
    wishme()
    while True:
        query = takecommand().lower()  # converts user asked query into lower case
        
        if 'login' in query :
            try:
                # speak('Whos this????')
                # content = takecommand()
                speak('Tell me your good name????')
                who = takecommand()
                user = "admin"
                user1= "Admin"

                if ((who == user)or (who == user1)):
                    speak('Welcome Boss')
                    quit()
                else:
                    cmd='rundll32.exe user32.dll, LockWorkStation'
                    subprocess.call(cmd)
                    speak('Worng User')
                    quit()

                    
            except Exception as e:
                print(e)
                speak('Sorry, I am not able to send this email')

        elif 'exit' in query:
            speak('okay boss, please call me when you need me')
            quit()
            
