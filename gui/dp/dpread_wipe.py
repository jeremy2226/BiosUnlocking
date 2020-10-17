import subprocess
import os
from guizero import App, PushButton
def scan():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/dpscan.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def dpwipeW25Q32():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/dpwipeW25Q32.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def dpwipeW25Q64BV():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/dpwipeW25Q64BV.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def dpwipeW25Q128BV():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/dpwipeW25Q128BV.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def dpwipeEN25QH32():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/dpwipeEN25QH32.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def dpwipeEN25QH64():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/dpwipeEN25QH64.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def dpwipeEN25QH128():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/dpwipeEN25QH128.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def dpwipeMX25L12805D():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/dpwipeMX25L12805D.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def dpwipeN25Q128A13():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/dpwipeN25Q128A13.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )

def close_window():
    app.destroy()

app = App(title="Identify and wipe Chips")
button1 = PushButton(app, command=scan, text="Scan Chip")
button2 = PushButton(app, command=dpwipeW25Q32, text="W25Q32 wipe 4MB")
button3 = PushButton(app, command=dpwipeEN25QH32, text="EN25QH32 wipe 4MB")
button4 = PushButton(app, command=dpwipeW25Q64BV, text="W25Q64BV wipe 8MB")
button5 = PushButton(app, command=dpwipeEN25QH64, text="EN25QH64 wipe 8MB")
button6 = PushButton(app, command=dpwipeW25Q128BV, text="W25Q128BV wipe 16MB")
button7 = PushButton(app, command=dpwipeEN25QH128, text="EN25QH128 wipe 16MB")
button8 = PushButton(app, command=dpwipeMX25L12805D, text="MX25L12805D wipe 16MB")
button9 = PushButton(app, command=dpwipeN25Q128A13, text="N25Q128A13 wipe 16MB")
button10 = PushButton(app, command=close_window, text="Close")


app.display()

