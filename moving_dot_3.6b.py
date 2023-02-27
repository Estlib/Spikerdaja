from tkinter import *
import time
import keyboard
# from pynput.keyboard import Key, Listener
raam = Tk()
raam.title("Spikerdaja")
tahvel = Canvas(raam, width=320, height = 240)
playerX = 0 #muutuja mis lisatakse iga tsükkel mängija X telje asukohale.
playerY = 0 #muutuja mis lisatakse iga tsükkel mängija Y telje asukohale
startX=104 #mängija algusasukoht X teljel, todo: muutujat muudetakse iga leveli alguses
startY=188 #mängija algusasukoht Y teljel, todo: muutujat muudetakse iga leveli alguses
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
Sdesk1 = None
Sdesk2 = None
Sdesk3 = None
Sdesk4 = None
Sdesk5 = None
Sdesk6 = None
Sdesk7 = None
Sdesk8 = None
Sdesk9 = None
AOECHECK = None
Wcollision = 0
Acollision = 0
Scollision = 0
Dcollision = 0

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
    global Sdesk1
    Sdesk1 = tahvel.create_rectangle(16, 64, 72, 88, fill=a, outline=b)
    global Sdesk2
    Sdesk2 = tahvel.create_rectangle(16, 112, 72, 136, fill=a, outline=b)
    global Sdesk3
    Sdesk3 = tahvel.create_rectangle(16, 160, 72, 184, fill=a, outline=b)
    global Sdesk4
    Sdesk4 = tahvel.create_rectangle(96, 64, 152, 88, fill=a, outline=b)
    global Sdesk5
    Sdesk5 = tahvel.create_rectangle(96, 112, 152, 136, fill=a, outline=b)
    global Sdesk6
    Sdesk6 = tahvel.create_rectangle(96, 160, 152, 184, fill=a, outline=b)
    global Sdesk7
    Sdesk7 = tahvel.create_rectangle(176, 64, 232, 88, fill=a, outline=b)
    global Sdesk8
    Sdesk8 = tahvel.create_rectangle(176, 112, 232, 136, fill=a, outline=b)
    global Sdesk9
    Sdesk9 = tahvel.create_rectangle(176, 160, 232, 184, fill=a, outline=b)
    # all these need to be solid, take them into account for collision map
    
def graphics_studentlayout_2person(a, b):
    tahvel.create_oval(24, 80, 40, 96, fill=a, outline=b)
    tahvel.create_oval(48, 84, 64, 100, fill=a, outline=b)
    tahvel.create_oval(24, 130, 40, 146, fill=a, outline=b)
    tahvel.create_oval(48, 128, 64, 144, fill=a, outline=b)
    tahvel.create_oval(24, 180, 40, 196, fill=a, outline=b)
    tahvel.create_oval(50, 180, 66, 196, fill=a, outline=b)
    
    tahvel.create_oval(104, 80, 120, 96, fill=a, outline=b)
    tahvel.create_oval(128, 84, 144, 100, fill=a, outline=b)
    tahvel.create_oval(104, 130, 120, 146, fill=a, outline=b)
    tahvel.create_oval(128, 128, 144, 144, fill=a, outline=b) 
#     tahvel.create_oval(104, 180, 120, 196, fill=a, outline=b) Player
#    tahvel.create_oval(130, 180, 146, 196, fill=a, outline=b) Nerd

    tahvel.create_rectangle(176, 64, 232, 88, fill=a, outline=b)
    tahvel.create_rectangle(176, 112, 232, 136, fill=a, outline=b)
    tahvel.create_rectangle(176, 160, 232, 184, fill=a, outline=b)
    # no collision for any of these students. except for the AOE check for the nerd / items
    
def graphics_studentlayout_2person_nerd(a, b):
    tahvel.create_oval(130, 180, 146, 196, fill=a, outline=b)
    # nerd, selle NPC pealt mängija spikerdab
    
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
    # muudab hudil oleva ruudu punasest roheliseks

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
    
def collisionstop(a,b,c,d):
    global Wcollision
    Wcollision = a
    global Acollision
    Acollision = b
    global Scollision
    Scollision = c
    global Dcollision
    Dcollision = d
    # märgib kus suunas mängija liikuda enam ei saa
    
def f_coll(a, b, c, d, e, f):
    if a-16 < b < c-8 and d-8 < e < f-8:
        hudtest(PAL6)
        collisionstop(Wcollision, Acollision, Scollision, 1)
    elif a-16 < b < c-2 and d < e < f:
        hudtest(PAL6)
        collisionstop(1, Acollision, Scollision, Dcollision)
    elif a-16 < b < c-8 and d-16 < e < f:
        hudtest(PAL6)
        collisionstop(Wcollision, Acollision, 1, Dcollision)
    elif a-8 < b < c and d-16 < e < f:
        hudtest(PAL6)
        collisionstop(Wcollision, 1, Scollision, Dcollision) #Eva
    else:
        collisionstop(0, 0, 0, 0)
        hudtest(PAL4)
    # töötleb läbi collisionid mis sellele funktsioonile antakse, ning kutsutakse märkija.
    # näitab ära hudil ka kas collision on toimunud

def collisioncheck_teacherdesk_leftwall():
    playerbox = tahvel.bbox(playergraphic)
    colliderbox = tahvel.bbox(Tdesk)
    f_coll(colliderbox[0],playerbox[0],colliderbox[2],colliderbox[1],playerbox[1],colliderbox[3])
    # võrdleb mängija asukohta laua asukohaga ja muudab hudil oleva ruudu roheliseks kui collision on saavutatud
    # puudu on playerstop funktsioon mis peatab mängija ning lukustab liikumissuuna.
    # TLDR; collision ei tunne ära kustsuunast mängija tuleb. hetkel on tegu in-AOE collisioniga.
    
def cc_sdl_2p_Sdesk1():
    playerbox = tahvel.bbox(playergraphic)
    colliderbox = tahvel.bbox(Sdesk1)
    f_coll(colliderbox[0],playerbox[0],colliderbox[2],colliderbox[1],playerbox[1],colliderbox[3])
def cc_sdl_2p_Sdesk2():
    playerbox = tahvel.bbox(playergraphic)
    colliderbox = tahvel.bbox(Sdesk2)
    f_coll(colliderbox[0],playerbox[0],colliderbox[2],colliderbox[1],playerbox[1],colliderbox[3])
def cc_sdl_2p_Sdesk3():
    playerbox = tahvel.bbox(playergraphic)
    colliderbox = tahvel.bbox(Sdesk3)
    f_coll(colliderbox[0],playerbox[0],colliderbox[2],colliderbox[1],playerbox[1],colliderbox[3])
def cc_sdl_2p_Sdesk4():
    playerbox = tahvel.bbox(playergraphic)
    colliderbox = tahvel.bbox(Sdesk4)
    f_coll(colliderbox[0],playerbox[0],colliderbox[2],colliderbox[1],playerbox[1],colliderbox[3])
def cc_sdl_2p_Sdesk5():
    playerbox = tahvel.bbox(playergraphic)
    colliderbox = tahvel.bbox(Sdesk5)
    f_coll(colliderbox[0],playerbox[0],colliderbox[2],colliderbox[1],playerbox[1],colliderbox[3])
def cc_sdl_2p_Sdesk6():
    playerbox = tahvel.bbox(playergraphic)
    colliderbox = tahvel.bbox(Sdesk6)
    f_coll(colliderbox[0],playerbox[0],colliderbox[2],colliderbox[1],playerbox[1],colliderbox[3])
def cc_sdl_2p_Sdesk7():
    playerbox = tahvel.bbox(playergraphic)
    colliderbox = tahvel.bbox(Sdesk7)
    f_coll(colliderbox[0],playerbox[0],colliderbox[2],colliderbox[1],playerbox[1],colliderbox[3])
def cc_sdl_2p_Sdesk8():
    playerbox = tahvel.bbox(playergraphic)
    colliderbox = tahvel.bbox(Sdesk8)
    f_coll(colliderbox[0],playerbox[0],colliderbox[2],colliderbox[1],playerbox[1],colliderbox[3])
def cc_sdl_2p_Sdesk9():
    playerbox = tahvel.bbox(playergraphic)
    colliderbox = tahvel.bbox(Sdesk9)
    f_coll(colliderbox[0],playerbox[0],colliderbox[2],colliderbox[1],playerbox[1],colliderbox[3])
    
def collisioncheck_studentdesklayout_2person():
    cc_sdl_2p_Sdesk1()
    cc_sdl_2p_Sdesk2()
    cc_sdl_2p_Sdesk3()
    cc_sdl_2p_Sdesk4()
    cc_sdl_2p_Sdesk5()
    cc_sdl_2p_Sdesk6()
    cc_sdl_2p_Sdesk7()
    cc_sdl_2p_Sdesk8()
    cc_sdl_2p_Sdesk9()
    # lauad mida kontrollitakse
    
def drawroom_peterson():
    graphics_bgcolor(PAL2, PAL2)
    graphics_carpet(PAL6, PAL1)
    graphics_leftwall_windows(PAL3, PAL3)
    graphics_teacherdesk_leftwall(PAL5, PAL7)
    graphics_studentdesklayout_2person(PAL5, PAL4)
    graphics_studentlayout_2person(PAL2, PAL3)
    graphics_studentlayout_2person_nerd(PAL7, PAL1)
    # spetsiifilise klassiruumi leveli kujundus kasutades eelnevaid joonistusfunktsioone
    # sellel põhimõttel tuleb ka level editor.
    # siit puudu: õpetaja pattern / room event / interactible map
    
def test_checkall():
    playerbox = tahvel.bbox(playergraphic)
    colliderbox1 = tahvel.bbox(Tdesk)
    f_coll(colliderbox1[0],playerbox[0],colliderbox1[2],colliderbox1[1],playerbox[1],colliderbox1[3])
    colliderbox2 = tahvel.bbox(Sdesk1)
    f_coll(colliderbox2[0],playerbox[0],colliderbox2[2],colliderbox2[1],playerbox[1],colliderbox2[3])
    colliderbox3 = tahvel.bbox(Sdesk2)
    f_coll(colliderbox3[0],playerbox[0],colliderbox3[2],colliderbox3[1],playerbox[1],colliderbox3[3])
    colliderbox4 = tahvel.bbox(Sdesk3)
    f_coll(colliderbox4[0],playerbox[0],colliderbox4[2],colliderbox4[1],playerbox[1],colliderbox4[3])
    colliderbox5 = tahvel.bbox(Sdesk4)
    f_coll(colliderbox5[0],playerbox[0],colliderbox5[2],colliderbox5[1],playerbox[1],colliderbox5[3])
    colliderbox6 = tahvel.bbox(Sdesk5)
    f_coll(colliderbox6[0],playerbox[0],colliderbox6[2],colliderbox6[1],playerbox[1],colliderbox6[3])
    colliderbox7 = tahvel.bbox(Sdesk6)
    f_coll(colliderbox7[0],playerbox[0],colliderbox7[2],colliderbox7[1],playerbox[1],colliderbox7[3])
    colliderbox8 = tahvel.bbox(Sdesk7)
    f_coll(colliderbox8[0],playerbox[0],colliderbox8[2],colliderbox8[1],playerbox[1],colliderbox8[3])
    colliderbox9 = tahvel.bbox(Sdesk8)
    f_coll(colliderbox9[0],playerbox[0],colliderbox9[2],colliderbox9[1],playerbox[1],colliderbox9[3])
    colliderbox10 = tahvel.bbox(Sdesk9)
    f_coll(colliderbox10[0],playerbox[0],colliderbox10[2],colliderbox10[1],playerbox[1],colliderbox10[3])

def collisionmap_peterson():
#     collisioncheck_teacherdesk_leftwall()
#     hudtest(PAL8)
#     collisioncheck_studentdesklayout_2person()
#     hudtest(PAL1)
    test_checkall()
    # leveli collisionmap, ehk kõik kõvad objectid.
    
def moveplayer():
    global playerX
    global playerY
    tahvel.move(playergraphic, playerX, playerY)    
#     playerX == 0
#     playerY == 0
    # liigutab mängijat    

initialiseroom1() # level initsialiseeritakse.

#alljärgnev loop on hetkel mängu main loop. Iga tsükkel kontrollitakse WASD klahve. Liikumissuundi on 8
#hierarhia mille järjekorras klahvikombinatsioone kontrollitakse on sihilik. Kui monokombinatsioone
#kontrollida enne mitmeklahvikombinatsioone, siis ei saa diagonaale mida see kombinatsioon tekitab
#kunagi kontrollida ning mängija ei saa liikuda diagonaalselt.
while gameExitvalue < 1:
    collisionmap_peterson() # enne iga WASD tsüklit kontrollitakse selle leveli collisionmappi.
    if keyboard.is_pressed("w") and keyboard.is_pressed("d"):
        if Wcollision == 1 or Dcollision == 1:
            Ycheck(0) #annab Y telje liikumisväärtuse
            Xcheck(0) #annab X telje liikumisvärtuse
        else:
            Ycheck(-1) #annab Y telje liikumisväärtuse
            Xcheck(1) #annab X telje liikumisvärtuse
        moveplayer() #liigutab mängijat
        # kontrollitav suund on üles-paremale
    elif keyboard.is_pressed("w") and keyboard.is_pressed("a"):
        if Wcollision == 1 or Acollision == 1:
            Ycheck(0)
            Xcheck(0)        
        else:
            Ycheck(-1)
            Xcheck(-1)
        moveplayer()
        # kontrollitav suund on üles-vasakule
    elif keyboard.is_pressed("w") and keyboard.is_pressed("s"):
        if Wcollision == 1 or Scollision == 1:
            Xcheck(0)
            Ycheck(0)           
        else:
            Xcheck(0)
            Ycheck(0)
        moveplayer()
        # kontrollitakse vastastikku liigutavate klahvide kombinatsiooni, mis paneb mängija seisma
    elif keyboard.is_pressed("a") and keyboard.is_pressed("s"):
        if Acollision == 1 or Scollision == 1:
            Xcheck(0)
            Ycheck(0)
        else:
            Xcheck(-1)
            Ycheck(1)
        moveplayer()
        # kontrollitav suund on vasakule-alla
    elif keyboard.is_pressed("a") and keyboard.is_pressed("d"):
        if Acollision == 1 or Dcollision == 1:
            Xcheck(0)
            Ycheck(0)         
        else:
            Xcheck(0)
            Ycheck(0)
        moveplayer()
        # kontrollitakse vastastikku liigutavate klahvide kombinatsiooni, mis paneb mängija seisma
    elif keyboard.is_pressed("s") and keyboard.is_pressed("d"):
        if Scollision == 1 or Dcollision == 1:
            Ycheck(0)
            Xcheck(0)         
        else:
            Ycheck(1)
            Xcheck(1)
        moveplayer()
        # kontrollitav suund on alla-paremale
    elif keyboard.is_pressed("w"):
        if Wcollision == 1:
            Ycheck(0)
            Xcheck(0)
        else:
            Ycheck(-1)
            Xcheck(0)
        moveplayer()
        # kontrollitav suund on üles
    elif keyboard.is_pressed("a"):
        if Acollision == 1:
            Xcheck(0)
            Ycheck(0)
        else:
            Xcheck(-1)
            Ycheck(0)
        moveplayer()
        # kontrollitav suund on vasakule
    elif keyboard.is_pressed("s"):
        if Scollision == 1:
            Ycheck(0)
            Xcheck(0)
        else:
            Ycheck(1)
            Xcheck(0)
        moveplayer()
        # kontrollitav suund on alla
    elif keyboard.is_pressed("d"):
        if Dcollision == 1:
            Xcheck(0)
            Ycheck(0)
        else:
            Xcheck(1)
            Ycheck(0)
        moveplayer()
        # kontrollitav suund on paremale
    # TODO: vii kontroll tsükli algusesse, ning moodusta suunalukk 
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
# - check collision = in progress
# - split collision types into solid and AOE (also implement student & desk/chair graphics)
# - more robust gameloop allowing for multiple levels (järjend)
# - teachers & moving the teachers around on predetermined paths. this includes the AOE FOV COLLISION
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
# - shift to run with stamina meter of 1 second.
#
# Scrapped code:
#
# incomplete collision checking:
# #     if colliderbox[0] < playerbox[2] < colliderbox[2] and colliderbox[1] < playerbox[3] < colliderbox[3]:
# #         hudtest(PAL6)
# #         collisionstop()
#     if colliderbox[0]-16 < playerbox[0] < colliderbox[2]-16 and colliderbox[1] < playerbox[1] < colliderbox[3]:
# #         hudtest(PAL6)
#         collisionstop(1, Acollision, Scollision, Dcollision)
#     # kontrollitav suund on üles
#     elif colliderbox[0]-16 < playerbox[0] < colliderbox[2]-16 and colliderbox[1]-16 < playerbox[1] < colliderbox[3]-16:
# #         hudtest(PAL6)
#         collisionstop(Wcollision, Acollision, 1, Dcollision)
#     elif colliderbox[0]-16 < playerbox[0] < colliderbox[2] and colliderbox[1]-16 < playerbox[1] < colliderbox[3]-16:
# #         hudtest(PAL6)
#         collisionstop(Wcollision, 1, Scollision, Dcollision)
#     elif colliderbox[0]-16 < playerbox[0] < colliderbox[2]-16 and colliderbox[1] < playerbox[1] < colliderbox[3]:
#         hudtest(PAL6)
#         collisionstop(Wcollision, Acollision, 1, Dcollision)
# #     elif:
# #     elif:
#
# completed collision checking prior to making it a function:
#     if colliderbox[0]-16 < playerbox[0] < colliderbox[2]-8 and colliderbox[1]-8 < playerbox[1] < colliderbox[3]-8:
#         hudtest(PAL6)
#         collisionstop(Wcollision, Acollision, Scollision, 1)
#     elif colliderbox[0]-16 < playerbox[0] < colliderbox[2]-2 and colliderbox[1]< playerbox[1] < colliderbox[3]:
#         hudtest(PAL6)
#         collisionstop(1, Acollision, Scollision, Dcollision)
#     elif colliderbox[0]-16 < playerbox[0] < colliderbox[2]-8 and colliderbox[1]-16 < playerbox[1] < colliderbox[3]:
#         hudtest(PAL6)
#         collisionstop(Wcollision, Acollision, 1, Dcollision)
#     elif colliderbox[0]-8 < playerbox[0] < colliderbox[2] and colliderbox[1]-16 < playerbox[1] < colliderbox[3]:
#         hudtest(PAL6)
#         collisionstop(Wcollision, 1, Scollision, Dcollision) #Eva
#     else:
#         collisionstop(0, 0, 0, 0)
#         hudtest(PAL4)