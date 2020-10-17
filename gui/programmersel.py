import subprocess
import os
from guizero import App, Window, PushButton

def open_window1():
    window1.show()

def close_window1():
    window1.hide()

def open_window2():
    window2.show()

def close_window2():
    window2.hide()

def open_window3():
    window3.show()

def close_window3():
    window3.hide()

def dpmenu():
    process = subprocess.Popen("/home/administrator/BiosUnlocking/gui/dpmenu.sh")

def chmenu():
    process = subprocess.Popen("/home/administrator/BiosUnlocking/gui/chmenu.sh")

def lsmenu():
    process = subprocess.Popen("/home/administrator/BiosUnlocking/gui/lsmenu.sh")

def close_window():
    app.destroy()
    
app = App(title="Programmer Selection")
window1 = Window(app, title="Dediprog")
window1.hide()
window2 = Window(app, title="CH341A_SPI")
window2.hide()
window3 = Window(app, title="LinuxSPI(rpi etc)")
window3.hide()

open_button = PushButton(app, command=dpmenu, text="Dediprog")
close_button = PushButton(window1, text="Close", command=close_window1)
open_button = PushButton(app, command=chmenu, text="CH341A_SPI")
close_button = PushButton(window2, text="Close", command=close_window2)
open_button = PushButton(app, command=lsmenu, text="LinuxSPI(rpi etc)")
close_button = PushButton(window3, text="Close", command=close_window3)
button1 = PushButton(app, command=close_window, text="Close")
app.display()
