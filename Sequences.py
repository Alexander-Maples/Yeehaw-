from alive_progress import alive_bar, config_handler
from time import sleep
from random import randint, choice
from color import Color
import os
def clear():
  os.system('clear')
def terminated():
  Color(r = 255,bar=True)
  print ('PROGRAM CRASHED\nPLEASE RESTART PROGRAM\nSESSION TERMINATED')
  exit()
def chance():
  Color()
  r = randint(1, 1000)
  if r == 392:
    terminated()
    exit()
  else:
    Color(256,bar=True)
    clear()
    print('The console ran into an error... Please Wait')
    sleep(choice([0.5,1,1.5,2,2.5,3]))
    clear()
    print('Error Fixed.')
    sleep(1.5)
    clear()
def chance2():
  Color()
  r = randint(1, 1000)
  if r == 392:
    terminated()
    exit()
  else:
    Color(r=256,bar=True)
    clear()
    print("'Yeehaw!' ran into an error... Please Wait")
    sleep(choice([0.5,1,1.5,2,2.5,3]))
    clear()
    print('Error Fixed.')
    sleep(1.5)
    clear()
def bar1(amount = 1000, starting_string = 'Getting ready to start Yw-BCMP...', bar = 'bubbles', spinner = 'dots'):
  clear()
  Color(g=256,bar=True)
  '''
  ```
  amount: the amount needed to end the progress bar\n
  starting_string: the string that is going to be printed out on 0\n
  bar: the type of bar that will used in the progress bar\n
  spinner: the tpye of spinner that will be used in the progress bar
  ```
  '''
  config_handler.set_global(bar = bar, spinner = spinner)
  count = 0
  with alive_bar(amount) as Bar:
    for i in range(amount):
      if count == 0:
        print(starting_string)
        sleep(1)
        clear()
        count += 1
        clear()
        Color(g=256,bar=True)
        clear()
      elif i % randint(100, 700) == count - 1 and count != 0:
        chance()
        clear()
        Color(g=256,bar=True)
        clear()
      sleep(0.01)
      Bar()
    print('\033[38;2;255;255;0mStarting up Yw-BCMDP')
  sleep(1.5)
def bar2(amount = 2000, starting_string = "Loading 'Yeehaw!'...", bar = 'bubbles', spinner = 'dots'):
  clear()
  Color(g=256,bar=True)
  '''
  ```
  amount: the amount needed to end the progress bar\n
  starting_string: the string that is going to be printed out on 0\n
  bar: the type of bar that will used in the progress bar\n
  spinner: the tpye of spinner that will be used in the progress bar
  ```
  '''
  config_handler.set_global(bar = bar, spinner = spinner)
  count = 0
  with alive_bar(amount) as Bar:
    for i in range(amount):
      if count == 0:
        print(starting_string)
        sleep(1)
        clear()
        count += 1
        clear()
        Color(g=255,bar=True)
        clear()
      elif i % randint(100, 700) == count - 1 and count != 0:
        chance2()
        clear()
        Color(g=255,bar=True)
        clear()
        Color(g=255,bar=True)
        clear()
      sleep(0.01)
      Bar()
    print("\033[38;2;255;255;0mStarting up 'Yeehaw!'...")
  sleep(1.5)