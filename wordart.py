import time,random,sys
from color import bcolors
def typing(words):
				words
				for char in words:
								time.sleep(random.choice([0.04, 0.04, 0.05, 0.05, 0.04, 0.038, 0.05]))
								sys.stdout.write(char)
								sys.stdout.flush()
def intro():
  typing("\\   /   =====   =====   |   |   |===|   | | |    ||| \n \\ /    |       |       |   |   |   |   | | |    ||| \n  |     =====   =====   |===|   |===|   | | |    ||| \n  |     |       |       |   |   |   |   | | |        \n  |     =====   =====   |   |   |   |    | |     ||| \n")
def town():
	typing("=================================\n| =====   |===|   | | |   |   | |\n|   |     |   |   | | |   |\\  | |\n|   |     |   |   | | |   | \\ | |\n|   |     |   |   | | |   |  \\| |\n|   |     |===|    | |    |   | |\n=================================\nPress any key to continue\n")
def town2():
  print(f"{bcolors.OK}\n=================================\n|{bcolors.RESET}| | | | | | | | | | | | | | | |{bcolors.OK}|\n|{bcolors.RESET}    |                          {bcolors.OK}|\n|{bcolors.RESET}    |                          {bcolors.OK}|\n|{bcolors.RESET}    |                          {bcolors.OK}|\n|{bcolors.RESET}    |                          {bcolors.OK}|\n=================================\n{bcolors.RESET}Type movement (wasd or arrow keys)\n")