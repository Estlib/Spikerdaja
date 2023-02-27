from tkinter import *
import time
import keyboard
# from pynput.keyboard import Key, Listener
raam = Tk()
raam.title("Spikerdaja")
tahvel = Canvas(raam, width=320, height = 240)
playerX = 0 #muutuja mis lisatakse iga tsükkel mängija X telje asukohale.
playerY = 0 #muutuja mis lisatakse iga tsükkel mängija Y telje asukohale
startX=120 #mängija algusasukoht X teljel, todo: muutujat muudetakse iga leveli alguses
startY=120 #mängija algusasukoht Y teljel, todo: muutujat muudetakse iga leveli alguses
PAL1 = "black" #paletti 1. värv - must. paletti muudetakse vajaduselt ekraanil olevale graafikale.
PAL2 = "blue" #paletti 2. värv - tumesinine. paletti muudetakse vajaduselt ekraanil olevale graafikale.
PAL3 = "cyan" #paletti 3. värv - helesinine. paletti muudetakse vajaduselt ekraanil olevale graafikale.
PAL4 = "red" #paletti 4. värv - punane. paletti muudetakse vajaduselt ekraanil olevale graafikale.
PAL5 = "orange" #paletti 5. värv - oranz. paletti muudetakse vajaduselt ekraanil olevale graafikale.
PAL6 = "green" #paletti 6. värv - roheline. paletti muudetakse vajaduselt ekraanil olevale graafikale.
PAL7 = "yellow" #paletti 7. värv - kollane. paletti muudetakse vajaduselt ekraanil olevale graafikale.
PAL8 = "white" #paletti 8. värv - valge. paletti muudetakse vajaduselt ekraanil olevale graafikale.
SPAL9 = "red" #paletti erivärv - punane. mittemuutuv värv. muud funktsioonid mis ei sisalda mängugraafikat
gameExitvalue = 0 #väärtus mis praegu võrreldakse sellega kas mängu on tahetud kinni panna
# tulevikus aga jälgib teine väärtus progressi läbi mängu, mida salvestusfunktsioon kasutab
# savefaili tegemiseks. Hetkel 0 - mäng jookseb, 1 - exit game. funktsiooni mis seda väärtust kasutab
# hetkel veel pole.
Testprogress = 0 # todo: hakkab lugema progressi läbi mängu. antud juhul kahekohalise arvuna.
# arv tähistab viimast läbitud taset. funktsioon hetkel puudub
Levelsave = 0 # todo: salvestusfunktsioon level editorile. funktsioon hetkel puudub
ccm = None
playergraphic = None
Tdesk = None
AOECHECK = None

def graphics_bgcolor(a, b):
    tahvel.create_rectangle(0, 0, 320, 240, fill=a, outline=b)
    # joonistab taustavärvi, ei kasuta bgcolor meetodit, on ühtlasi seinavärv

def graphics_carpet(a, b):
    tahvel.create_rectangle(8, 8, 232, 232, fill=a, outline=b)
    # joonistab toa sisemuse põrandavärvi, ehk ruumi mille piires mängija liigelda saab
    
def graphics_leftwall_windows(a, b):
    tahvel.create_rectangle(0, 32, 8, 64, fill=a, outline=b)
    tahvel.create_rectangle(0, 96, 8, 128, fill=a, outline=b)
    tahvel.create_rectangle(0, 160, 8, 196, fill=a, outline=b)
    # joonistab vasaku seina aknad
    
def graphics_teacherdesk_leftwall(a, b):
    global Tdesk
    Tdesk = tahvel.create_rectangle(16, 32, 80, 56, fill=a, outline=b)
    # joonistab õpetaja laua vasakusse seina
    
    
def graphics_studentdesklayout_2person(a, b):
    tahvel.create_rectangle(16, 64, 72, 88, fill=a, outline=b)
    tahvel.create_rectangle(16, 112, 72, 136, fill=a, outline=b)
    tahvel.create_rectangle(16, 160, 72, 184, fill=a, outline=b)
    tahvel.create_rectangle(96, 64, 152, 88, fill=a, outline=b)
    tahvel.create_rectangle(96, 112, 152, 136, fill=a, outline=b)
    tahvel.create_rectangle(96, 160, 152, 184, fill=a, outline=b)
    tahvel.create_rectangle(176, 64, 232, 88, fill=a, outline=b)
    tahvel.create_rectangle(176, 112, 232, 136, fill=a, outline=b)
    tahvel.create_rectangle(176, 160, 232, 184, fill=a, outline=b)
    # all these need to be solid, take them into account for collision map
    
def graphics_studentlayout_2person(a, b):
    tahvel.create_oval(24, 80, 40, 96, fill=a, outline=b)
    tahvel.create_oval(48, 84, 64, 100, fill=a, outline=b)
    tahvel.create_rectangle(16, 112, 72, 136, fill=a, outline=b)
    tahvel.create_rectangle(16, 160, 72, 184, fill=a, outline=b)
    tahvel.create_rectangle(96, 64, 152, 88, fill=a, outline=b)
    tahvel.create_rectangle(96, 112, 152, 136, fill=a, outline=b)
    tahvel.create_rectangle(96, 160, 152, 184, fill=a, outline=b)
    tahvel.create_rectangle(176, 64, 232, 88, fill=a, outline=b)
    tahvel.create_rectangle(176, 112, 232, 136, fill=a, outline=b)
    tahvel.create_rectangle(176, 160, 232, 184, fill=a, outline=b)
    # no collision for any of these students. except for the AOE check for the nerd / items
    
def screenupdate():
    tahvel.pack()
    raam.update()
    # pakib akna graafika kokku, funktsioon kutsutakse iga tsükkel
        
def drawhud():
    tahvel.create_rectangle(240, 0, 320, 240, fill=PAL7, outline=PAL7)
    global AOECHECK
    AOECHECK = tahvel.create_rectangle(248, 8, 256, 16, fill=PAL4, outline=PAL1)
    # joonistab ekraanile leveliga seotud info.
    # siit puudu: soorituse läbivuse protsent / inventory? / periphery proximity indicator
    # / passgrade / time / excuses
    
def hudtest(a):
    tahvel.itemconfig(AOECHECK, fill=a)

def drawplayer():
    global playergraphic
    playergraphic = tahvel.create_oval(startX+playerX, startY+playerY, startX+16+playerX, startY+16+playerY, fill=PAL5, outline=PAL1)
    # joonistab ekraanile mängija, kasutatakse leveli initsialiseerimisel.
    # vana mängija liigutamismeetod kasutas seda ka mängija iga tsükkel uuestijoonistamiseks
    
def initialiseroom1():
    drawroom_peterson()
    drawhud()
    drawplayer()
    #initisialiseerib leveli, joonistades leveli, infotabeli (hud) ja mängija.
    #siit puudu: add progress counter +1 /
    
def Ycheck(int):
    global playerY
    if playerY != int:
        playerY = int
    # kontrollib et mängija liigutusväärtused Y teljel ei oleks suurem kui sisseantav väärtus, 
    # antud juhul eespool on selleks väärtuseks ainult kas 1 või -1
    # hoiab ära "libiseva" liikumise

def Xcheck(int):
    global playerX
    if playerX != int:
        playerX = int
    # kontrollib et mängija liigutusväärtused X teljel ei oleks suurem kui sisseantav väärtus, 
    # antud juhul eespool on selleks väärtuseks ainult kas 1 või -1
    # hoiab ära "libiseva" liikumise
    
def collisioncheck_teacherdesk_leftwall():
    playerbox = tahvel.bbox(playergraphic)
    deskbox = tahvel.bbox(Tdesk)
    if deskbox[0] < playerbox[2] < deskbox[2] and deskbox[1] < playerbox[3] < deskbox[3]:
        hudtest(PAL6)
        Xcheck(0)
        Ycheck(0)
    else:
        hudtest(PAL4)
    
def drawroom_peterson():
    graphics_bgcolor(PAL2, PAL2)
    graphics_carpet(PAL6, PAL1)
    graphics_leftwall_windows(PAL3, PAL3)
    graphics_teacherdesk_leftwall(PAL5, PAL7)
    graphics_studentdesklayout_2person(PAL5, PAL4)
    graphics_studentlayout_2person(PAL2, PAL3)
    # spetsiifilise klassiruumi leveli kujundus kasutades eelnevaid joonistusfunktsioone
    # sellel põhimõttel tuleb ka level editor.
    # siit puudu: õpetaja pattern / room event / collision map / interactible map

def collisionmap_peterson():
    collisioncheck_teacherdesk_leftwall()
    
def moveplayer():
    global playerX
    global playerY
    tahvel.move(playergraphic, playerX, playerY)    
    playerX == 0
    playerY == 0
    # liigutab mängijat

initialiseroom1() # level initsialiseeritakse.


#alljärgnev loop on hetkel mängu main loop. Iga tsükkel kontrollitakse WASD klahve. Liikumissuundi on 8
#hierarhia mille järjekorras klahvikombinatsioone kontrollitakse on sihilik. Kui monokombinatsioone
#kontrollida enne mitmeklahvikombinatsioone, siis ei saa diagonaale mida see kombinatsioon tekitab
#kunagi kontrollida ning mängija ei saa liikuda diagonaalselt.
while gameExitvalue < 1:    
    if keyboard.is_pressed("w") and keyboard.is_pressed("d"):
        Ycheck(-1) #annab Y telje liikumisväärtuse
        Xcheck(1) #annab X telje liikumisvärtuse
        moveplayer() #liigutab mängijat
        # kontrollitav suund on üles-paremale
    elif keyboard.is_pressed("w") and keyboard.is_pressed("a"):
        Ycheck(-1)
        Xcheck(-1)
        moveplayer()
        # kontrollitav suund on üles-vasakule
    elif keyboard.is_pressed("w") and keyboard.is_pressed("s"):
        Xcheck(0)
        Ycheck(0)
        moveplayer()
        # kontrollitakse vastastikku liigutavate klahvide kombinatsiooni, mis paneb mängija seisma
    elif keyboard.is_pressed("a") and keyboard.is_pressed("s"):
        Xcheck(-1)
        Ycheck(1)
        moveplayer()
        # kontrollitav suund on vasakule-alla
    elif keyboard.is_pressed("a") and keyboard.is_pressed("d"):
        Xcheck(0)
        Ycheck(0)
        moveplayer()
        # kontrollitakse vastastikku liigutavate klahvide kombinatsiooni, mis paneb mängija seisma
    elif keyboard.is_pressed("s") and keyboard.is_pressed("d"):
        Ycheck(1)
        Xcheck(1)
        moveplayer()
        # kontrollitav suund on alla-paremale
    elif keyboard.is_pressed("w"):
        Ycheck(-1)
        Xcheck(0)
        moveplayer()
        # kontrollitav suund on üles
    elif keyboard.is_pressed("a"):
        Xcheck(-1)
        Ycheck(0)
        moveplayer()
        # kontrollitav suund on vasakule
    elif keyboard.is_pressed("s"):
        Ycheck(1)
        Xcheck(0)
        moveplayer()
        # kontrollitav suund on alla
    elif keyboard.is_pressed("d"):
        Xcheck(1)
        Ycheck(0)
        moveplayer()
        # kontrollitav suund on paremale
    collisionmap_peterson()
    screenupdate() #uuendab tahvlit liigutatud mängijaga
    time.sleep(0.005) # 50 fps setting is 0.005. if it is anything other than this, speed is affected
raam.mainloop()

# Autorid: Jüri Vaitmaa & Eva-Kristina Vesiallik
#
# ülesandesihilised eesmärgid
#    Programmeerimiskeel peab olema Python.
#    Lahendus peab olema enda tehtud ja uus.
#    Lahenduse failis peab kommentaarina sisalduma ka püstitatud ülesande tekst ja autorite nimed.
#    Lahendus ise peab olema mõistlikult kommenteeritud.
#    Ülesande lahendus peab sisaldama vähemalt ühte endakirjutatud funktsiooni ja selle rakendamist.
#    Ülesande lahenduses peab olema vähemalt üks tingimuslause.
#    Ülesande lahenduses peab olema vähemalt üks tsükkel.
#    Ülesande lahenduses tuleb failist lugeda või/ja kasutajalt andmeid küsida.
#    Ülesande lahenduses tuleb faili või/ja ekraanile väljastada.
#    Ülesande lahendus peab sisaldama vähemalt ühte järjendit.
#
# eesmärgid:
#
# - draw level = done (still need desk and student gfx, see collision below)
# - move player = done
# - check collision 
# - split collision types into solid and AOE (also implement student & desk/chair graphics)
# - more robust gameloop allowing for multiple levels (järjend)
# - teachers & moving the teachers around on predetermined paths. this includes the AOE FOV
# - pause menu & title screen (involves modifying the gameloop more)
# - save game & load game systems basing on text files
# - ending & failstate
#
# nendest esmärkidest peaks piisama projektiülesande sooritusest, kuid polish on puudu:
# - story with cutscenes
# - implement fadein & fadeout via palette modification
# - bomb ass music and sfx (sound implementation in general)
# - use images instead of tkinter generated graphics
# - fullscreen graphics scaling
# - items and objects to sabotage the class with
# - alternate paths and extra missions based on shoplifting & hardest game ever
