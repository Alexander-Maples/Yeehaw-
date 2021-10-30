import os
import sys
for p in sys.path:
    print(p)
def Cmd(command="help"):
  os.system(command)
Cmd("rm /home/runner/Yeehaw/__pycache__/*")
Cmd("rmdir /home/runner/Yeehaw/__pycache__")