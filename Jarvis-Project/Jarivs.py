import pyttsx3 as pytotxt
import speech_recognition as speechrecog
import pyaudio
import datetime
import wikipedia
import webbrowser
engine=pytotxt.init()
voices=engine.getProperty('voices')
male_voice=engine.setProperty('voice',voices[0].id)
spped=engine.setProperty("rate",175)


def say_engine(text):
    engine.say(text)
    engine.runAndWait()

def greetings():
    hour=int(datetime.datetime.now().hour)

    if hour<12:
        say_engine("Hello Good Morning ")
    elif hour>=12 and hour<=16:
        say_engine("Hello Good Afternoon ")
    else:
        say_engine("Hello Good Evening ")

    say_engine("Im Jarvis How can i help you Today..")
    print("hello")


def user_speak():

    brain_speech=speechrecog.Recognizer()

    with speechrecog.Microphone() as get_sppech:
        print("Speak Now...")
        audio=brain_speech.listen(get_sppech)
    
    try:
        text=brain_speech.recognize_google(audio,language='en-in')
        print(f"You Speak: {text}")
    except:
        print("Please Speak..")
        return user_speak()
    
    return text

     


def speech_worker():
    greetings()
    while True:
        get_user_speaks=user_speak()
        print(type(get_user_speaks))
        if "wikipedia" in str(get_user_speaks).lower():
            say_engine("Searching Wikipedia....")
            get_user_speaks=get_user_speaks.replace("wikipedia","")
            result=wikipedia.summary(get_user_speaks,sentence=2)
            say_engine("According to Wikipedia...")
            print(result)
            say_engine(result)
        elif "open youtube" in str(get_user_speaks).lower():
            webbrowser.open("youtube.com")
        elif "open google" in str(get_user_speaks).lower():
            webbrowser.open("google.com")
        elif "time" in str(get_user_speaks).lower():
            get_time=datetime.datetime.now().strftime("%H:%M:%S")
            print(type(get_time))
            say_engine(get_time)
        elif "exit" in get_user_speaks or "quit" in get_user_speaks:
            say_engine("Goodbye")
            break
    
speech_worker()