import subprocess
import os
from guizero import App, PushButton

def lsscan():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/lsscan.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )

def lsflash():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/lsflash.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
    
def close_window():
    app.destroy()

app = App(title="Identify and Wipe Chips")
button1 = PushButton(app, command=lsscan, text="Scan Chip")
button2 = PushButton(app, command=lsflash, text="Write Chips")
button10 = PushButton(app, command=close_window, text="Close")


app.display()
