from getch import getch as getc
import termios, fcntl, sys
from saveload import encrypt, decrypt
from saveload import userencrypt as encryptt
from saveload import userdecrypt as decryptt
from Sequences import bar1, bar2
from errors import RaiseShutDown, ShutDown
fd = sys.stdin.fileno()
flags_save = fcntl.fcntl(fd, fcntl.F_GETFL)
attrs_save = termios.tcgetattr(fd)
timeforshutdown = 0
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
  global timeforshutdown
  update = 0
  x=0
  import sys,os,re,random
  drive = random.choice(["A","B","D","E","F","G"])
  userdrive = ""
  l = re.compile('load_')
  bar1()
  os.system('clear')
  my_secret = "Firepup650"
  import time
  Color(255)
  print(f"Welcome to Yw-BCMDP! (ver. 0.30.OCT.21)")
  print(f"Type 'help' to see avalible commands")
  while x==0:
    Color(0, 255, 255)
    BCMDP = input(f"~/Yehaw{bcolors.RESET}$ ").lower()
    if BCMDP == "help":
      print(f"{bcolors.BROWN}Commands:\n{bcolors.RESET}help\nroms\nload_(rom name)\nencode\ndecode\nclear\nquit\nexit\nshutdown\n[Command Deleted]")
    elif BCMDP == "roms":
      print(f"{bcolors.BROWN}Roms:\n{bcolors.RESET}Yeehaw!)\nWood Cutter (Coming soon...)")
    elif BCMDP == "...":
      print(random.choice(["...","What do you want?","I'm not gonna tell you anything.","I mean it! I'm not telling you anything!","Fine, I'll tell you one thing...","There is more than one deleted command...","This command isn't on the command list...","Why are you here?","You got something to prove?","Just load the game!",f"{bcolors.WARNING}Invalid command!",f"{bcolors.WARNING}Invalid command!"]))
    elif BCMDP == "load_yeehaw!":
      if powercatch == 1:
        x=2
      else:
        if update != 0:
          print(f"{bcolors.WARNING}A restart is required.")
          if timeforshutdown == 0:
            timeforshutdown = 1
        else:
          while 1:
            os.system("clear")
            print(f"Please insert the 'Rom Update Drive' into floppy disk drive {drive}.")
            if userdrive != "":
              print(f"I said 'floppy disk drive {drive}'!!!")
            userdrive = get()
            if drive.lower() == userdrive:
              break
          print("Updating Rom...")
          time.sleep(5)
          print("Rom Update complete")
          update = 1
    elif BCMDP == "i":
      if powercatch == 1:
        x=1
      else:
        if update != 0:
          print(f"{bcolors.WARNING}A restart is required.")
          if timeforshutdown == 0:
            timeforshutdown = 1
        else:
          while 1:
            os.system("clear")
            print(f"Please insert the 'Rom Update Drive' into floppy disk drive {drive}.")
            if userdrive != "":
              print(f"I said 'floppy disk drive {drive}'!!!")
            userdrive = get()
            if drive.lower() == userdrive:
              break
          print("Updating Rom...")
          time.sleep(5)
          print("Rom Update complete")
          update = 1
    elif l.match(BCMDP):
      print(f"{bcolors.WARNING}Invalid rom or no rom name!{bcolors.RESET}")
    elif BCMDP == "quit":
        sys.exit(0)
    elif BCMDP == "exit":
        print("exit")
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
      coded = encryptt(input(f"{bcolors.OK}Message?:{bcolors.RESET} "))
      print(f"{bcolors.OK}encoded: {bcolors.RESET}{coded}")
    elif BCMDP == "decode":
      try:
        coded = decryptt(input(f"{bcolors.OK}Message?:{bcolors.RESET} "))
      except:
        coded = "Bad message"
      print(f"{bcolors.OK}decoded: {bcolors.RESET}{coded}")
    elif BCMDP == "system":
     print(hash("o"))
    elif BCMDP == "shutdown":
      RaiseShutDown()
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
                  time.sleep(0.7)
                  sys.stdout.write(char)
                  sys.stdout.flush()
  def speed(words):
    words
    for char in words:
      sys.stdout.write(char)
      sys.stdout.flush()
  import wordart as wa
  speed(f"{bcolors.WOOD}")
  wa.intro()
  print()
  x=2
  c = 0
  direction = 0
  while 1:
    if x != 1:
      speed(f"{bcolors.WOOD}")
      wa.town()
      speed(f"{bcolors.RESET}")
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
          speed("\nTermination cancled")
        else:
          konamicode = 0
          speed("\nTermination cancled")
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
import os, sys
power = 0
timeforshutdown = 0
def shutdown():
  global power
  global timeforshutdown
  if timeforshutdown == 1:
    power += 1
  try:
    reset = ""
    while 1:
      Color(255,255,255)
      os.system("clear")
      print("You turned off your computer...\nPress 'r' to turn it back on...")
      reset = get()
      if reset == "r":
        raise KeyboardInterrupt
      elif reset == "0":
        raise EOFError
  except EOFError:
      print("\nProgram Terminated...")
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
    except ShutDown:
      shutdown()
runner()
