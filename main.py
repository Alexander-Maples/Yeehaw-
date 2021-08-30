class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    CYAN = '\033[36m' #CYAN
    BROWN = '\033[33m' #BROWN
from Reader import *
def run():
  x=0
  import sys
  import os
  import re
  l = re.compile('load')
  os.system('clear')
  my_secret = "Firepup650"
  import time
  print(f"{bcolors.FAIL}Welcome to Yw-BCMDP! (ver. 0.30.AUG.21)")
  print(f"Type 'help' to see avalible commands{bcolors.RESET}")
  while x==0:
    BCMDP = input(f"{bcolors.CYAN}~/Yehaw{bcolors.RESET}$ ").lower()
    if BCMDP == "help":
      print(f"{bcolors.BROWN}Commands:\n{bcolors.RESET}Help\nRoms\nLoad (rom name)\nQuit\n[Command Deleted]")
    elif BCMDP == "roms":
      print(f"{bcolors.BROWN}Roms:\n{bcolors.RESET}Yeehaw!")
    elif BCMDP == "load yeehaw!":
      x=2
    elif BCMDP == "i":
      x=1
    elif l.match(BCMDP):
      print(f"{bcolors.WARNING}Invalid rom or no rom name!{bcolors.RESET}")
    elif BCMDP == "quit":
        sys.exit(0)
    elif BCMDP == "dev":
      dev_try = input("Dev code: ")
      if dev_try == my_secret:
        print("Congratulations!\nYou get nothing!")
      else:
        print(f"{bcolors.FAIL}INVALID CODE... GOODBYE")
        sys.exit(65)
    else:
      print(f"{bcolors.WARNING}Invalid command!")
  if x != 1:
    print("Starting Rom...")
    time.sleep(2)
  os.system("clear")
  if x != 1:
    print(f"{bcolors.FAIL}Importing content")
  import random, termios, fcntl 
  fd = sys.stdin.fileno()
  # save old state
  flags_save = fcntl.fcntl(fd, fcntl.F_GETFL)
  attrs_save = termios.tcgetattr(fd)
  if x !=1:
    print("")
    print(f"{bcolors.OK}Import successful")
    time.sleep(1)
    print("")
    print(f"{bcolors.FAIL}Initializing town")
  store = "Kroger"
  sherf = "Sheriff's office"
  lot = "Texas Lottery"
  jail = "Jail"
  ticbot = "Racing tickets"
  house = "Your house"
  if x != 1:
    print("")
    print(f"{bcolors.OK}Town initialized successfully")
    time.sleep(1)
    print("")
    print(f"{bcolors.FAIL}Defining custom commands")
    print("")
  def clear():
    os.system("clear")
  def read2():
    #old state restore
    termios.tcsetattr(fd, termios.TCSAFLUSH, attrs_save)
    fcntl.fcntl(fd, fcntl.F_SETFL, flags_save)
  def slep():
    time.sleep(1)
  def slleep():
    time.sleep(2)
  def convert(tup):
    '''Converts a tuple to a string'''
    key2 = ''
    for item in tup:
          key2 = key2 + item
    return key2
  if x != 1:
    print(f"{bcolors.OK}Definintions complete")
    slep()
    print("")
    print(f"{bcolors.RESET}Starting Game 'Yeehaw'...")
    slleep()
    slleep()
    clear()
  def typing(words):
         words
         for char in words:
                  time.sleep(random.choice([0.04, 0.04, 0.05, 0.05, 0.04, 0.038, 0.05]))
                  sys.stdout.write(char)
                  sys.stdout.flush()
  def speed(words):
    words
    for char in words:
      sys.stdout.write(char)
      sys.stdout.flush()
  import wordart as wa
  typing(f"{bcolors.BROWN}")
  if x != 1:
    wa.intro()
  print()
  x=2
  while 1:
    if x != 1:
      typing(f"{bcolors.BROWN}")
      wa.town()
      typing(f"{bcolors.RESET}")
    else:
      wa.town2()
    read1()
    key = sys.stdin.read(1)
    read2()
    clear()
    speed(key)
    if key == "a":
      speed("\nleft")
    elif key == "w":
      speed("\nup")
    elif key == "[":
      key = sys.stdin.read(1)
      speed(key)
      if key == "A":
        speed("\nup")
      elif key == "B":
        speed("\ndown")
      elif key == "D":
        speed("\nleft")
      elif key == "C":
        speed("\nright")
      else:
        speed("\nbad")
    elif key == "s":
      speed("\ndown")
    elif key == "d":
      speed("\nright")
    elif key == "\n":
      pass
    elif key == "\r":
      pass
    else:
      speed("\n'")
      speed(key)
      speed("' is not a command!")
    x = 1
def runner():
  try:
    run()
  except KeyboardInterrupt:
    print("rash!")
    runner()
runner()