import subprocess
import os
from guizero import App, PushButton

def chread():
    process = subprocess.Popen("./chread.sh")

def chflash():
    process = subprocess.Popen("./chflash.sh")

def cherase():
    process = subprocess.Popen("./cherase.sh")
    
def close_window():
    app.destroy()

app = App(title="Dediprog")
button1 = PushButton(app, command=chread, text="Read Chips")
button2 = PushButton(app, command=chflash, text="Write Chips")
button3 = PushButton(app, command=cherase, text="Erase Chips")
button4 = PushButton(app, command=close_window, text="Close")

app.display()
 
