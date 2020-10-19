import subprocess
import os
from guizero import App, PushButton

def dpread_wipe():
    process = subprocess.Popen("./dpread_wipe.sh")

def dpflash():
    process = subprocess.Popen("./dpflash.sh")

def close_window():
    app.destroy()

app = App(title="Dediprog")
button1 = PushButton(app, command=dpread_wipe, text="Read and Wipe Chips")
button2 = PushButton(app, command=dpflash, text="Write Chips")
button3 = PushButton(app, command=close_window, text="Close")

app.display()
