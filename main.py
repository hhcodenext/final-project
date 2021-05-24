from sense_hat import SenseHat
import time
import os

sense = SenseHat()

# While loop that prints the current time (local)
while True:
    t = time.localtime()
    print(str(t.tm_hour)+":"+str(t.tm_min)+":"+str(t.tm_sec))
    time.sleep(.1)
    # os.system('clear') # replace with 'cls' if not on sense-hat
  
    # Some stuff to detect movement
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

  x=abs(x)
  y=abs(y)
  z=abs(z)
  
  if x > 1 or y > 1 or z > 1:
    sense.show_letter("!")
    break
  else:
    sense.clear()
