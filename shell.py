import os
def install(package=""):
  pip = f"pip install --upgrade {package}"
  os.system(pip)
def pwd():
  pwd = os.system("pwd")
  return pwd
install("pip")
install("cryptography")
install("alive-progress")
install("cffi")
os.system("clear")
print("You are good to start the 'main.py' file now!")