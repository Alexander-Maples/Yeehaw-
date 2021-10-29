from getch import getch as getc
import termios, fcntl, sys
from saveload import encrypt, decrypt
from Sequences import bar1, bar2
fd = sys.stdin.fileno()
flags_save = fcntl.fcntl(fd, fcntl.F_GETFL)
attrs_save = termios.tcgetattr(fd)
def geth():
    termios.tcsetattr(fd, termios.TCSAFLUSH, attrs_save)
    fcntl.fcntl(fd, fcntl.F_SETFL, flags_save)
def get():
  getc()
  key = sys.stdin.read(1)
  geth()
  return key
from color import bcolors, Color
def run(powercatch):
  x=0
  import sys,os,re
  l = re.compile('load_')
  bar1()
  os.system('clear')
  my_secret = "Firepup650"
  import time
  Color(255)
  print(f"Welcome to Yw-BCMDP! (ver. 0.29.OCT.21)")
  print(f"Type 'help' to see avalible commands")
  while x==0:
    Color(0, 255, 255)
    BCMDP = input(f"~/Yehaw{bcolors.RESET}$ ").lower()
    if BCMDP == "help":
      print(f"{bcolors.BROWN}Commands:\n{bcolors.RESET}help\nroms\nload_(rom name)\nencode\ndecode\nreset\nclear\nquit\nexit\n[Command Deleted]")
    elif BCMDP == "roms":
      print(f"{bcolors.BROWN}Roms:\n{bcolors.RESET}Yeehaw!")
    elif BCMDP == "load_yeehaw!":
      x=2
    elif BCMDP == "i":
      x=1
    elif l.match(BCMDP):
      print(f"{bcolors.WARNING}Invalid rom or no rom name!{bcolors.RESET}")
    elif BCMDP == "quit":
        sys.exit(0)
    elif BCMDP == "exit":
        sys.exit(0)
    elif BCMDP == "clear":
        os.system('clear')
    elif BCMDP == "dev":
      dev_try = input("Dev code: ")
      if dev_try == my_secret:
        print("Congratulations!\nYou get nothing!")
      else:
        print(f"{bcolors.FAIL}INVALID CODE... GOODBYE")
        sys.exit(65)
    elif BCMDP == "encode":
      coded = encrypt(input(f"{bcolors.OK}Message?:{bcolors.RESET} "))
      print(f"{bcolors.OK}encoded: {bcolors.RESET}{coded}")
    elif BCMDP == "decode":
      try:
        coded = decrypt(input(f"{bcolors.OK}Message?:{bcolors.RESET} "))
      except:
        coded = "Bad message"
      print(f"{bcolors.OK}decoded: {bcolors.RESET}{coded}")
    elif BCMDP == "reset":
      raise(KeyboardInterrupt)
    elif BCMDP == "crash":
      raise(EnvironmentError)
    else:
      print(f"{bcolors.WARNING}Invalid command!")
  if x != 1:
    print("Starting Rom...")
    time.sleep(2)
  os.system("clear")
  if x != 1:
    print(f"{bcolors.FAIL}Importing content")
  import random
  konamicode = 0
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
    Color(0, 256, 0)
    print("Town initialized successfully")
    time.sleep(1)
    print("")
    print(f"{bcolors.FAIL}Defining custom commands")
    print("")
  def clear():
    os.system("clear")
  def slep():
    time.sleep(1)
  def slleep():
    time.sleep(2)
  if x != 1:
    print(f"{bcolors.OK}Definintions complete")
    slep()
    print("")
    bar2()
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
  typing(f"{bcolors.WOOD}")
  wa.intro()
  print()
  x=2
  c = 0
  direction = 0
  while 1:
    if x != 1:
      typing(f"{bcolors.WOOD}")
      wa.town()
      typing(f"{bcolors.RESET}")
    else:
      wa.town2()
    key = get()
    clear()
    if key.lower() == "a":
      direction = 3
      konamicode = 0
      c = 0
    elif key == '4':
      direction = 3
      if konamicode == 4:
        konamicode = 5
      elif konamicode == 6:
        konamicode = 7
      else:
        konamicode = 0
      c = 0
    elif key.lower() == "w":
      direction = 1
      konamicode = 0
      c = 0
    elif key == "8":
      direction = 1
      if konamicode == 0:
        konamicode = 1
      elif konamicode == 1:
        konamicode = 2
      else:
        konamicode = 0
      c = 0
    elif key == "[":
      konamicode = 0
      if c == 2:
        key = get()
        c = 0
        if key == "A":
          direction = 1
        elif key == "B":
          direction = 2
        elif key == "D":
          direction = 3
        elif key == "C":
          direction = 4
    elif key.lower() == "s":
      direction = 2
      konamicode = 0
      c = 0
    elif key == "2":
      direction = 2
      if konamicode == 2:
        konamicode = 3
      elif konamicode == 3:
        konamicode = 4
      else:
        konamicode = 0
      c = 0
    elif key.lower() == "d":
      direction = 4
      konamicode = 0
      c = 0
    elif key == "6":
      direction = 4
      if konamicode == 5:
        konamicode = 6
      elif konamicode == 7:
        konamicode = 8
      else:
        konamicode = 0
      c = 0
    elif key == "\n":
      direction = 0
      c = 2
      if konamicode == 10:
        konamicode = 11
      else:
        konamicode = 0
      c = 0
    elif key == "\r":
      direction = 0
      if konamicode == 10:
        konamicode = 11
      else:
        konamicode = 0
      c = 0
    elif key == "b":
      direction = 0
      if konamicode == 8:
        konamicode = 9
      else:
        konamicode = 0
      speed('WARNING: THIS WILL TERMINATE THE PROGRAM, PRESS "t" TO CONTINUE')
      speed("\n")
      key = get()
      if key == "t":
        raise(EOFError)
      elif key == "a":
        if konamicode == 9:
          konamicode = 10
        else:
          konamicode = 0
      else:
        speed("\nTermination cancled")
      c=0
    else:
      direction = 0
      konamicode = 0
      c = 2
    if konamicode == 11:
      clear()
      speed("Congrats... you know the Konami Code... so what?")
      konamicode = 0
    elif direction == 1:
      speed("up")
    elif direction == 2:
      speed("down")
    elif direction == 3:
      speed("left")
    elif direction == 4:
      speed("right")
    x = 1
import os, time, sys
power = 0
def shutdown():
  global power
  power += 1
  try:
    while 1:
      os.system("clear")
      print("You turned off your computer...\nPress 'crtl + c' or 'r' to turn it back on...")
      reset = get()
      if reset == "r":
        raise KeyboardInterrupt
  except KeyboardInterrupt:
    runner()
def runner():
    global power
    try:
      run(power)
    except EOFError:
      print("\nProgram Terminated...")
    except KeyboardInterrupt:
      shutdown()
runner()