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

def lsflash9480m():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/ls9480m_W25Q128BV.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def lsflash840g2():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/ls840g2_W25Q128BV.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def lsflash8570p():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/ls8570p_MX25L12805D.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def lsflash8570p2():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/ls8570p_W25Q128BV.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def lsflash850g2():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/ls850g2_N25Q128A13.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
def lsflash6570b():
    process = subprocess.Popen(
        "sudo gnome-terminal -x /home/administrator/BiosUnlocking/gui/ls6570b_W25Q128BV.sh", 
        stdout=subprocess.PIPE,
        stderr=None,
        shell=True
    )
    
def close_window():
    app.destroy()

app = App(title="Write(Flash) Chips")
button1 = PushButton(app, command=lsscan, text="Scan Chip")
button2 = PushButton(app, command=lsflash, text="Write Chips")
button10 = PushButton(app, command=close_window, text="Close")


app.display()
