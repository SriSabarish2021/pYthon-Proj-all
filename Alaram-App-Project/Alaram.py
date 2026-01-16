import datetime
import pygame
import time
print("Welcome to Alarm App".center(50,'-'))
print('')
get_set_time=input("Enter the time for Alarm(HH:MM:SS): ")

def alarm_func(get_time):
    count=True
    while count:
        timer=str(datetime.datetime.now().time()).split('.')[0]
        
        if timer==get_set_time:
            pygame.mixer.init()
            pygame.mixer.music.load('Alarm-Fast-High-Pitch-A1-www.fesliyanstudios.com.mp3')
            pygame.mixer.music.play()
            
        else:
            print(timer)
        time.sleep(1)
        


    
    

    



alarm_func(get_set_time)