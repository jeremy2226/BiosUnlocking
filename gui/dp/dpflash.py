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
def dpflash9480m():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/dp9480m_W25Q128BV.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def dpflash840g2():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/dp840g2_W25Q128BV.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def dpflash8570p():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/dp8570p_MX25L12805D.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def dpflash8570p2():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/dp8570p_W25Q128BV.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def dpflash850g2():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/dp850g2_N25Q128A13.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def dpflash6570b():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/dp6570b_W25Q128BV.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )

def close_window():
    app.destroy()

app = App(title="Flash Chips")
button1 = PushButton(app, command=scan, text="Scan Chip")
button2 = PushButton(app, command=dpflash9480m, text="9480m FLASH Winbond")
button3 = PushButton(app, command=dpflash9480m, text="840G2 FLASH Winbond")
button4 = PushButton(app, command=dpflash8570p, text="8570p FLASH Macronix")
button5 = PushButton(app, command=dpflash8570p2, text="8570p FLASH Winbond")
button6 = PushButton(app, command=dpflash850g2, text="850g2 FLASH Micron(N)")
button5 = PushButton(app, command=dpflash6570b, text="6570b FLASH Winbond")
button6 = PushButton(app, command=close_window, text="Close")

app.display()

