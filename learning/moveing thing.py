from tkinter import *
import time
import keyboard

class character():
    x = 10
    y = 10
    color = "red"
    canvas.create_oval(x, y, x + 40, y + 40, fill=color)


def moveup():
    character.y -= 10
def moveright():
    character.x += 10
def movedown():
    character.y += 10
def moveleft():
    character.x -= 10


def choose():
    choosen_move = randint(0, 4)

    if choosen_move == 0:
        moveup()
    elif choosen_move == 1:
        moveright()
    elif choosen_move == 2:
        movedown()
    elif choosen_move == 3:
        moveleft()

    print "%s | %s" % (character.x, character.y)
    canvas.update()
    sleep(1)


while True:
    choose()
root.mainloop()