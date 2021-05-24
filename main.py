from sense_hat import SenseHat
import time
import os

# Really bad way to play audio with python.
# See pygame.org/docs/ref/music.html
import pygame
pygame.mixer.init()
pygame.mixer.music.load('noise.wav')
pygame.mixer.music.play()

sense = SenseHat()

sense.clear()

def turn_off_alarm():
    sense.show_letter("!", text_colour=(255,0,0))
    time.sleep(1)
    alarm_time = input("Please enter a new time: ")
    sense.clear()
        
def set_off_alarm():
    sense.clear((255,255,255))

alarm_time = input("Please print what time you would like the alarm to go off (Format: hh:mm): ")

# While loop to check time.
while True:
    t = time.localtime()
    # print(str(t.tm_hour)+":"+str(t.tm_min)+":"+str(t.tm_sec))
    # ^^FOR TESTING^^
    time.sleep(.1)
    
    time_formatted = str(t.tm_hour)+":"+str(t.tm_min)
    alarm_off = time_formatted == alarm_time    
    
    if alarm_off:
        set_off_alarm()
    
    # Some stuff to detect movement
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x=abs(x)
    y=abs(y)
    z=abs(z)
  
    if x > 1 or y > 1 or z > 1:
        turn_off_alarm()
        continue
    if alarm_off:
        continue
    else:
        sense.clear()
