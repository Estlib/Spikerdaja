from tkinter import *
import time
import keyboard
# from pynput.keyboard import Key, Listener
raam = Tk()
raam.title("Spikerdaja")
tahvel = Canvas(raam, width=320, height = 240)
playerX = 120
playerY = 120
PAL1 = "black"
PAL2 = "blue"
PAL3 = "cyan"
PAL4 = "red"
PAL5 = "orange"
PAL6 = "green"
PAL7 = "yellow"
PAL8 = "white"
SPAL9 = "red"
gameExitvalue = 0
Testprogress = 0
Levelsave = 0
playergraphic = tahvel.create_oval(0+playerX, 0+playerY, 16+playerX, 16+playerY, fill=PAL5, outline=PAL1)

def graphics_bgcolor(a, b):
    tahvel.create_rectangle(0, 0, 320, 240, fill=a, outline=b)

def graphics_carpet(a, b):
    tahvel.create_rectangle(8, 8, 232, 232, fill=a, outline=b)
    
def graphics_leftwall_windows(a, b):
    tahvel.create_rectangle(0, 32, 8, 64, fill=a, outline=b)
    tahvel.create_rectangle(0, 96, 8, 128, fill=a, outline=b)
    tahvel.create_rectangle(0, 160, 8, 196, fill=a, outline=b)
    
def graphics_teacherdesk_leftwall(a, b):
    tahvel.create_rectangle(16, 32, 80, 56, fill=a, outline=b)
    
def screenupdate():
    tahvel.pack()
    raam.update()

def drawroom_peterson():
    graphics_bgcolor(PAL2, PAL2)
    graphics_carpet(PAL6, PAL1)
    graphics_leftwall_windows(PAL3, PAL3)
    graphics_teacherdesk_leftwall(PAL5, PAL7)
    
def drawhud():
    tahvel.create_rectangle(240, 0, 320, 240, fill=PAL7, outline=PAL7)

def drawplayer():
    global playergraphic
    playergraphic = tahvel.create_oval(0+playerX, 0+playerY, 16+playerX, 16+playerY, fill=PAL5, outline=PAL1)
    
def initialiseroom1():
    drawroom_peterson()
    drawhud()
    drawplayer()
    
def moveplayer():
    tahvel.position(playergraphic, playerX, playerY)

initialiseroom1()

while gameExitvalue < 1:    
    if keyboard.is_pressed("w") and keyboard.is_pressed("d"):
        playerY -= 1
        playerX += 1
    elif keyboard.is_pressed("w") and keyboard.is_pressed("a"):
        playerY -= 1
        playerX -= 1
    elif keyboard.is_pressed("w") and keyboard.is_pressed("s"):
        playerY -= 0
        playerY += 0
    elif keyboard.is_pressed("a") and keyboard.is_pressed("s"):
        playerX -= 1
        playerY += 1
    elif keyboard.is_pressed("a") and keyboard.is_pressed("d"):
        playerX -= 0
        playerY += 0
    elif keyboard.is_pressed("s") and keyboard.is_pressed("d"):
        playerY += 1
        playerX += 1
    elif keyboard.is_pressed("w"):
        playerY -= 1
    elif keyboard.is_pressed("a"):
        playerX -= 1
    elif keyboard.is_pressed("s"):
        playerY += 1
    elif keyboard.is_pressed("d"):
        playerX += 1
    drawplayer()
    screenupdate()
    time.sleep(0.000001) # 50 fps setting is 0.005. if it is anything other than this, speed is affected
raam.mainloop()