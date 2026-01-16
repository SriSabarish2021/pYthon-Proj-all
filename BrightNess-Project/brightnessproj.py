
import screen_brightness_control as sbc
import psutil
print("Brightness-Controller-APP")

sbc.set_brightness(100,display=0)

process=psutil.process_iter(attrs=['pid','name','status'])


for all in process:

    print(all.info['pid'])
