import subprocess
import os
from guizero import App, PushButton
def do_nothing1():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/exe1.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def do_nothing2():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/exe2.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def do_nothing3():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/exe3.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def do_nothing4():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/exe4.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def do_nothing5():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/exe5.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def do_nothing6():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/exe22.sh",
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def do_nothing7():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/exe33.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def do_nothing8():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/exe44.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def do_nothing9():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/exe55.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
app = App(title="Dell E6440 Computrace Removal")
button1 = PushButton(app, command=do_nothing1, text="Scan Chip")
button2 = PushButton(app, command=do_nothing2, text="W25Q32 Wipe 4MB")
button3 = PushButton(app, command=do_nothing3, text="W25Q32 Write 4MB")
button4 = PushButton(app, command=do_nothing4, text="W25Q64BV Wipe 8MB")
button5 = PushButton(app, command=do_nothing5, text="W25Q64BV Write 8MB")
button6 = PushButton(app, command=do_nothing2, text="EN25QH32 Wipe 4MB")
button7 = PushButton(app, command=do_nothing3, text="EN25QH32 Write 4MB")
button8 = PushButton(app, command=do_nothing4, text="EN25QH64 Wipe 8MB")
button9 = PushButton(app, command=do_nothing5, text="EN25QH64 Write 8MB")
button1.bg = "white"
button2.bg = "red"
button3.bg = "green"
button4.bg = "red"
button5.bg = "green"
button6.bg = "red"
button7.bg = "green"
button8.bg = "red"
button9.bg = "green"

app.display()

