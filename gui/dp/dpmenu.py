import subprocess
import os
from guizero import App, PushButton

def read_wipe():
    process = subprocess.Popen("/home/administrator/BiosUnlocking/gui/read_wipe.sh")

def flash():
    process = subprocess.Popen("/home/administrator/BiosUnlocking/gui/flash.sh")

def close_window():
    app.destroy()

app = App(title="Dediprog")
button1 = PushButton(app, command=read_wipe, text="Read and Wipe Chips")
button2 = PushButton(app, command=flash, text="Write Chips")
button3 = PushButton(app, command=close_window, text="Close")

app.display()
