import pygame
import time
import datetime

def alaram_play(time_of_user):
    print(time_of_user)
    timer=True

    while timer:
        time_setting=f"{datetime.datetime.now().time().hour:02}:{datetime.datetime.now().time().minute:02}:{datetime.datetime.now().time().second:02}"
        if str(time_of_user)==str(time_setting):
            pygame.mixer.init()
            pygame.mixer.music.load('Alarm-Fast-High-Pitch-A1-www.fesliyanstudios.com.mp3')
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            break
        else:
            print(time_setting)
        time.sleep(1)
        

get_alram_time=input("Enter time to Alarm (HH:MM:SS): ")

alaram_play(get_alram_time)

