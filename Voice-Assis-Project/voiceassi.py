import speech_recognition as recog_speech

print("Welcome to Voice Assiteant App".center(50,'-'))
print("")

def speech():
    print("Speak Now....")
    brain_speech=recog_speech.Recognizer()
    
    with recog_speech.Microphone() as speech_receiver:
        voice=brain_speech.listen(speech_receiver)
    try:
        get_txt=brain_speech.recognize_google(voice,language='en-in')
        print(f"Your Text:{get_txt}")
        with open("./text.txt",'a') as file:
            cont=get_txt
            file.writelines(f"{cont}\n")
    except:
        print("Sorry For The error occuring")

speech()