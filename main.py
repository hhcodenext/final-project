from sense_hat import SenseHat
import time
import os
import pygame

# i is so that the noise only runs once
i = 0
# Initializing & loading alarm clock noise.
pygame.mixer.init()
pygame.mixer.music.load('noise.wav')

sense = SenseHat()

sense.clear()

# Function called when alarm clock is turned off
# Referenced in the while loop
def turn_off_alarm():
    global i
    sense.show_letter("!", text_colour=(255,0,0))
    pygame.mixer.music.stop()
    i = 0
    time.sleep(1)
    alarm_time = input("Please enter a new time: ")
    sense.clear()

# Function called when alarm clock is set off
# Referenced in the while loop
def set_off_alarm():
    global i
    sense.clear((255,255,255))
    # Really bad way to play audio with python.
    # See pygame.org/docs/ref/music.html
    i += 1
    if i == 1:
        pygame.mixer.music.play()

# Input from the user for the alarm time
alarm_time = input("Please print what time you would like the alarm to go off (Format: hh:mm): ")

# While loop to check alarm.
while True:
    t = time.localtime()
    # print(str(t.tm_hour)+":"+str(t.tm_min)+":"+str(t.tm_sec))
    # ^^FOR TESTING^^
    time.sleep(.1)
    
    # Formatting the localtime & checking the alarm
    time_formatted = str(t.tm_hour)+":"+str(t.tm_min)
    alarm_on = time_formatted == alarm_time    
    
    if alarm_on:
        set_off_alarm()
    
    # Some stuff to detect movement
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x=abs(x)
    y=abs(y)
    z=abs(z)
  
    # Logic for all the stuff above
    if x > 1 or y > 1 or z > 1:
        turn_off_alarm()
        continue
    if alarm_on:
        continue
    else:
        sense.clear()

