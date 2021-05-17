from sense_hat import SenseHat
import time
import os

# While loop that prints the current time (local)
while True:
  t = time.localtime()
  print(str(t.tm_hour)+":"+str(t.tm_min)+":"+str(t.tm_sec))
  time.sleep(.1)
  os.system('cls')
