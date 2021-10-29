import sys
def speed(words):
    words
    for char in words:
      sys.stdout.write(char)
      sys.stdout.flush()
bcakupdes = "Syntax | Description\n--------- | ---------\n`\\033[0m` | Resets all color and formats\n`\\033[1m` | Creates bold text\n`\\033[2m` | Creates dim text\n`\\033[3m` | Creates italic text\n`\\033[4m` | Creates underlined text\n`\\033[7m` | Swaps foreground and background colors\n`\\033[8m` | Hides text\n`\\033[38;2;{RED};{GREEN};{BLUE}m` | Create custom colors using RGB color codes"
def Color(r=0,g=0,b=0,bar=False,bcolor=False):
  '''"r"  is red, "g" is green, "b" is blue.'''
  if r < 0:
    r = 0
  if r > 255:
    r=255
  if g < 0:
    g = 0
  if g > 255:
    g = 255
  if b < 0:
    b = 0
  if b > 255:
    b = 255
  speed("\033[0m")
  speed(f'\033[38;2;{r};{g};{b}m')
  if bar == True:
    print("\003[0m")
    print(f"\033[38;2;{r};{g};{b}m")
  if bcolor == True:
    return f"\033[38;2;{r};{g};{b}m"
class bcolors:
  RESET = "\033[0m"
  BROWN = f"{Color(205,127,50,bcolor=True)}"
  WARNING = f"{Color(236,232,26,bcolor=True)}"
  FAIL = f"{Color(255,bcolor=True)}"
  OK = f"{Color(g=255,bcolor=True)}"
  WOOD = f"{Color(120,81,45,bcolor=True)}\033[46m\033[7m"