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
teacherX = 0#teachers X value
teacherY = 0#teachers Y value
TstartX = 81
TstartY = 53
saveprogress = 1 # todo: hakkab lugema progressi läbi mängu. antud juhul kahekohalise arvuna.
# arv tähistab viimast läbitud taset. funktsioon hetkel puudub
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
# tulevikus a9
playergraphic = None
teachergraphic = None
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
TESTGRAPHIC = None
Wcollision = 0
Acollision = 0
Scollision = 0
Dcollision = 0
nerdbox = None
testcompletion = 0
currentlevelcompleted = 0
hudtestcompletionlines = [264,264,264,264,264]
nerdregion = None
startpause = True
enumerativeline1 = None
enumerativeline2 = None
enumerativeline3 = None
enumerativeline4 = None
enumerativeline5 = None
getkeytriggerspeed = 0
nooption = 0
turnintest = 0
pausegraphic = None
pausetext = None
enterlock = 0
playercontainer = None
pcontainerW = None
pcontainerA = None
pcontainerS = None
pcontainerD = None
saverequested = 0
loadrequested = 0
leveltext = None
leveltextcomplete = None
currentlvteacher = None
direction = 0
stepcount = 0
element = 0
teachermove1 = [0,58,0,80, 0,115,80,0, 68,0,0,80, 107,0,68,0]
teachermove2 = [0,0,0,110 ,0,0,110,0]
# teachermove3 = []
# teachermove4 = []
# teachermove5 = []
# teachermove6 = []
# teachermove7 = []
# teachermove8 = []
# teachermove9 = []
# teachermove10 = []
#up,down,left,right

def splashscreen():
    tahvel.create_rectangle(0, 0, 320, 240, fill=PAL8, outline=PAL8)
    img = PhotoImage(file="TTHK-logo.ppm")
    tahvel.create_image(8,50, anchor=NW, image=img)
    screenupdate()
    time.sleep(3.000)

def roomcollision():
    global pcontainerW
    pcontainerW = tahvel.create_rectangle(0, 0, -8, 240, fill=PAL8, outline=PAL8)
    global pcontainerA
    pcontainerA = tahvel.create_rectangle(0, -8, 320, 0, fill=PAL8, outline=PAL8)
    global pcontainerS
    pcontainerS = tahvel.create_rectangle(240, 0, 320, 240, fill=PAL8, outline=PAL8)
    global pcontainerD
    pcontainerD = tahvel.create_rectangle(0, 240, 320, 248, fill=PAL8, outline=PAL8)
    
def worksheet():
    tahvel.create_rectangle(0, 0, 320, 240, fill=PAL8, outline=PAL8)
    tahvel.create_line(0,0,0,240,fill=PAL3,width=1)
    tahvel.create_line(16,0,16,240,fill=PAL3,width=1)
    tahvel.create_line(32,0,32,240,fill=PAL3,width=1)
    tahvel.create_line(48,0,48,240,fill=PAL3,width=1)
    tahvel.create_line(64,0,64,240,fill=PAL3,width=1)
    tahvel.create_line(80,0,80,240,fill=PAL3,width=1)
    tahvel.create_line(96,0,96,240,fill=PAL3,width=1)
    tahvel.create_line(112,0,112,240,fill=PAL3,width=1)
    tahvel.create_line(128,0,128,240,fill=PAL3,width=1)
    tahvel.create_line(144,0,144,240,fill=PAL3,width=1)
    tahvel.create_line(160,0,160,240,fill=PAL3,width=1)
    tahvel.create_line(176,0,176,240,fill=PAL3,width=1)
    tahvel.create_line(192,0,192,240,fill=PAL3,width=1)
    tahvel.create_line(208,0,208,240,fill=PAL3,width=1)
    tahvel.create_line(224,0,224,240,fill=PAL3,width=1)
    tahvel.create_line(240,0,240,240,fill=PAL3,width=1)
    tahvel.create_line(256,0,256,240,fill=PAL3,width=1)
    tahvel.create_line(272,0,272,240,fill=PAL3,width=1)
    tahvel.create_line(288,0,288,240,fill=PAL3,width=1)
    tahvel.create_line(304,0,304,240,fill=PAL3,width=1)    
    tahvel.create_line(320,0,320,240,fill=PAL3,width=1)
    tahvel.create_line(0,0,320,0,fill=PAL3,width=1)
    tahvel.create_line(0,16,320,16,fill=PAL3,width=1)
    tahvel.create_line(0,32,320,32,fill=PAL3,width=1)
    tahvel.create_line(0,48,320,48,fill=PAL3,width=1)
    tahvel.create_line(0,64,320,64,fill=PAL3,width=1)
    tahvel.create_line(0,80,320,80,fill=PAL3,width=1)
    tahvel.create_line(0,96,320,96,fill=PAL3,width=1)
    tahvel.create_line(0,112,320,112,fill=PAL3,width=1)
    tahvel.create_line(0,128,320,128,fill=PAL3,width=1)
    tahvel.create_line(0,144,320,144,fill=PAL3,width=1)
    tahvel.create_line(0,160,320,160,fill=PAL3,width=1)
    tahvel.create_line(0,176,320,176,fill=PAL3,width=1)
    tahvel.create_line(0,192,320,192,fill=PAL3,width=1)
    tahvel.create_line(0,208,320,208,fill=PAL3,width=1)
    tahvel.create_line(0,224,320,224,fill=PAL3,width=1)
    tahvel.create_line(0,240,320,240,fill=PAL3,width=1)
    
def story1():
    worksheet()
    tahvel.create_text(160, 24, text="Esimene kontrolltöö.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 56, text="Nohik ütles et aitab mind, kuigi", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 72, text="ma teda väga ei usu. Istun klassis", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 88, text="ta kõrvale, vaatan kas peab oma", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 104, text="sõnast kinni. Kui ei pea, siis...", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 120, text="siis on nii minu, kui tema lips läbi", fill=PAL1, font=("terminal", 10))
    global nooption
    nooption = 0
    time.sleep(0.200)
    while nooption < 1:
        if keyboard.is_pressed("enter"): #continue to next level
            nooption = 1
            return
        else:
            screenupdate()
            nooption = 0
            
def story2():
    worksheet()
    tahvel.create_text(160, 24, text="Teine kontrolltöö - Õpetaja aisting.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 56, text="Olen oma hinnetega nii kraavis, et", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 72, text="ühest spikerdamisest ei piisa. Ta", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 88, text="lubas ka edaspidigi aidata, ainult", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 104, text="et õpetaja on haisu ninna saanud.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 120, text="Ta ei lase mul enam koos nohikuga", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 136, text="istuda, paneb minu alati kuskile", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 152, text="mujale istuma. :C", fill=PAL1, font=("terminal", 10))
    global nooption
    nooption = 0
    time.sleep(0.200)
    while nooption < 1:
        if keyboard.is_pressed("enter"): #continue to next level
            nooption = 1
            return
        else:
            screenupdate()
            nooption = 0
            
def story3():
    worksheet()
    tahvel.create_text(160, 24, text="Kolmas kontrolltöö - Spikerduskunst", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 56, text="Meid on pandud algklassi kunstiklassi.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 72, text="Tundub et õpetajale see väga ei istu, ", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 88, text="käib ringi ja pidevalt jälgib nagu kull.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 104, text="Nohik on õpetaja eriti põletava pilgu", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 120, text="all, isegi maaler ei vahi värvi kui-", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 136, text="vamist pingsamalt.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 152, text="", fill=PAL1, font=("terminal", 10))
    global nooption
    nooption = 0
    time.sleep(0.200)
    while nooption < 1:
        if keyboard.is_pressed("enter"): #continue to next level
            nooption = 1
            return
        else:
            screenupdate()
            nooption = 0
            
def story4():
    worksheet()
    tahvel.create_text(160, 24, text="Neljas kontrolltöö - Kommari punker.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 56, text="Tundub et tund liigutati õpetaja", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 72, text="Pavlovitsi klassi - vanale kommarile", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 88, text="meeldib punane värv üle kõige, seega", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 104, text="värvis ta üks aasta oma klassi üleni", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 120, text="punaseks. Õpetajat on selles klassis", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 136, text="halb näha kuna tallegi meeldib punane", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 152, text="ent mitte ümbruses, vaid seljas kanda.", fill=PAL1, font=("terminal", 10))
    global nooption
    nooption = 0
    time.sleep(0.200)
    while nooption < 1:
        if keyboard.is_pressed("enter"): #continue to next level
            nooption = 1
            return
        else:
            screenupdate()
            nooption = 0
            
def story5():
    worksheet()
    tahvel.create_text(160, 24, text="Viies kontrolltöö - Tagasi algklassi.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 56, text="Nohik, truu sõber, aitab alati, kuid", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 72, text="täna on meil asendusõpetaja, spiker-", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 88, text="dajate hirm ise: Stallone.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 104, text="See pole ta päris nimi, ta tõmbas", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 120, text="üks aasta kooli lõpuballil korralikult", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 136, text="nina täis ja hakkas karated keset saali", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 152, text="viskama - nii saigi nime Stallone.", fill=PAL1, font=("terminal", 10))
    global nooption
    nooption = 0
    time.sleep(0.200)
    while nooption < 1:
        if keyboard.is_pressed("enter"): #continue to next level
            nooption = 1
            return
        else:
            screenupdate()
            nooption = 0
            
def story6():
    worksheet()
    tahvel.create_text(160, 24, text="Kuues kontrolltöö - Härmatunud digivõlur", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 56, text="Täna annab kontrolltööd üks habemik", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 72, text="keda tuntakse koolipeal mitme nimega.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 88, text="Könndalf, kaabelhabe... levinuim", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 104, text="neist on digivõlur. Kuna tema tunnis", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 120, text="peaaegu mitte keegi läbi ei kuku.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 136, text="Tundub et ta spikerdamistest ei tea", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 152, text="sest seekord olen nohikule üsna lähedal.", fill=PAL1, font=("terminal", 10))
    global nooption
    nooption = 0
    time.sleep(0.200)
    while nooption < 1:
        if keyboard.is_pressed("enter"): #continue to next level
            nooption = 1
            return
        else:
            screenupdate()
            nooption = 0
            
def story7():
    worksheet()
    tahvel.create_text(160, 24, text="Seitsmes kontrolltöö - Taevas või põrgu?", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 56, text="Kes kurat selle klassi kallale kommari", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 72, text="lasi? taevasinine põrand ja kärtspunased", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 88, text="lauad ei sobi kokku, valus on midagi muud", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 104, text="peale töö vaadatagi. Vähemalt nohikule on", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 120, text="juurdepääs suhteliselt vaba.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 136, text="", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 152, text="", fill=PAL1, font=("terminal", 10))
    global nooption
    nooption = 0
    time.sleep(0.200)
    while nooption < 1:
        if keyboard.is_pressed("enter"): #continue to next level
            nooption = 1
            return
        else:
            screenupdate()
            nooption = 0
            
def story8():
    worksheet()
    tahvel.create_text(160, 24, text="Kaheksas kontrolltöö - Lan party.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 56, text="Oleme tagasi arvutiklassis, halb on see", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 72, text="et meile annab tunde jälle meie tavaline", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 88, text="õpetaja, kullipilk on naasnud ja ase-", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 104, text="ndusõpetajate käe all lihtsalt spiker-", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 120, text="damine on läbi. Vähemalt nüüd oleme", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 136, text="kogenumad, ning mulle tundub, et", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 152, text="kooliaasta lõppeb positiivselt.", fill=PAL1, font=("terminal", 10))
    global nooption
    nooption = 0
    time.sleep(0.200)
    while nooption < 1:
        if keyboard.is_pressed("enter"): #continue to next level
            nooption = 1
            return
        else:
            screenupdate()
            nooption = 0
            
def story9():
    worksheet()
    tahvel.create_text(160, 24, text="Üheksas kontrolltöö - Kommar strikes back", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 56, text="Keegi elutark (vist kommar ise) otsustas", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 72, text="et üks arvutiklassidest ka kommari meele", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 88, text="järgi kärtspunaseks värvida. Mida see", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 104, text="meile tähendab, et ma pean jälle", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 120, text="rohkem vahtima et vahele ei jääks.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 136, text="Nohik vast nõustub minuga siinkohal.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 152, text="", fill=PAL1, font=("terminal", 10))
    global nooption
    nooption = 0
    time.sleep(0.200)
    while nooption < 1:
        if keyboard.is_pressed("enter"): #continue to next level
            nooption = 1
            return
        else:
            screenupdate()
            nooption = 0
            
def story10():
    worksheet()
    tahvel.create_text(160, 24, text="Lõpueksam - Vastused nutitahvlil", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 56, text="Ainult mina ja nohik pääsesime", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 72, text="eelmise kontrolltöö tuumapommist.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 88, text="Uskumatu. Poleks arvanud, et", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 104, text="õpetaja nii laastava töö teeb.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 120, text="Aga samas siin ongi viimane töö.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 136, text="Nohik mind seekord ei aita.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 152, text="tundub, et tegu on lõksuga...", fill=PAL1, font=("terminal", 10))
    global nooption
    nooption = 0
    time.sleep(0.200)
    while nooption < 1:
        if keyboard.is_pressed("enter"): #continue to next level
            nooption = 1
            return
        else:
            screenupdate()
            nooption = 0
            
def graphics_failstate():
    tahvel.create_text(162, 62, text="TABATUD", fill=PAL8, font=("terminal", 32))
    tahvel.create_text(158, 66, text="TABATUD", fill=PAL8, font=("terminal", 32))
    tahvel.create_text(162, 66, text="TABATUD", fill=PAL8, font=("terminal", 32))
    tahvel.create_text(158, 62, text="TABATUD", fill=PAL8, font=("terminal", 32))
    tahvel.create_text(160, 64, text="TABATUD", fill=SPAL9, font=("terminal", 32))
    tahvel.create_text(160, 120, text="ENTER alustab esimeselt levelilt uuesti", fill=SPAL9, font=("terminal", 10))
    tahvel.create_text(160, 136, text="X laeb salvestatud mängu", fill=SPAL9, font=("terminal", 10))
    
def failstate_caughtscreen():
    worksheet()
    graphics_failstate()
    screenupdate()
    global nooption
    nooption = 0
    while nooption < 1:
        if keyboard.is_pressed("enter"): #continue to next level
            if saveprogress == 0:
                nooption = 1
                return
        #         errorscreen(1101) as level 0 isnt suppose to be playable.
            elif saveprogress == 1:
        #         errorscreen() needed as level 1 is already autoinitialised and never called again.
#                 tahvel.delete("all")
                story1()
                initialiseroom1()
                screenupdate()
                nooption = 1
                return
            return
        elif keyboard.is_pressed("z"): #save. currently does nothing. used to save a text file with current progress.
            instructions()
        elif keyboard.is_pressed("x"): #save. currently does nothing. used to save a text file with current progress.
            loadrequested = 1
            gameload()
#         elif keyboard.is_pressed("x"): #load. currently does nothing. used to load a save from a text file.            
        elif keyboard.is_pressed("esc"): #exit game
            quit() #this quits, in later version, this needs to go back to title screen instead
     #uuendab tahvlit liigutatud mängijaga
    time.sleep(0.001)

def titlescreen():
    global loadrequested
    worksheet()
    tahvel.create_text(163, 67, text="Spikerdaja", fill=PAL1, font=("terminal", 32))
    tahvel.create_text(162, 66, text="Spikerdaja", fill=PAL1, font=("terminal", 32))
    tahvel.create_text(161, 65, text="Spikerdaja", fill=PAL1, font=("terminal", 32))
    tahvel.create_text(160, 64, text="Spikerdaja", fill=PAL4, font=("terminal", 32))
    tahvel.create_text(161, 121, text="ENTER alustab mängu", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 120, text="ENTER alustab mängu", fill=PAL2, font=("terminal", 10))
    tahvel.create_text(161, 137, text="Z näitab juhiseid", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 136, text="Z näitab juhiseid", fill=PAL2, font=("terminal", 10))
    tahvel.create_text(161, 153, text="X laeb salvestatud mängu", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 152, text="X laeb salvestatud mängu", fill=PAL2, font=("terminal", 10))
    tahvel.create_text(160, 184, text="Juhendaja: Kristjan Kivikangur", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 200, text="Autorid: Jüri Vaitmaa ning", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 216, text="Eva-Kristina Vesiallik", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 232, text="TTHK TARge21 - 2021 v3.1x", fill=PAL1, font=("terminal", 10))
    screenupdate()
    global nooption
    nooption = 0
    while nooption < 1:
        if keyboard.is_pressed("enter"): #continue to next level
            if saveprogress == 0:
                nooption = 1
                return
        #         errorscreen(1101) as level 0 isnt suppose to be playable.
            elif saveprogress == 1:
        #         errorscreen() needed as level 1 is already autoinitialised and never called again.
#                 tahvel.delete("all")
                story1()
                initialiseroom1()
                screenupdate()
                nooption = 1
                return
            return
        elif keyboard.is_pressed("z"): #save. currently does nothing. used to save a text file with current progress.
            instructions()
        elif keyboard.is_pressed("x"): #save. currently does nothing. used to save a text file with current progress.
            loadrequested = 1
            gameload()
#         elif keyboard.is_pressed("x"): #load. currently does nothing. used to load a save from a text file.            
        elif keyboard.is_pressed("esc"): #exit game
            quit() #this quits, in later version, this needs to go back to title screen instead
     #uuendab tahvlit liigutatud mängijaga
    time.sleep(0.001)
    
def instructions():
    worksheet()
    tahvel.create_text(160, 10, text="Juhised: ", fill=PAL4, font=("terminal", 10))
    tahvel.create_text(160, 30, text="Oled lohakas õpilane ning oled jätnud", fill=PAL4, font=("terminal", 10))
    tahvel.create_text(160, 40, text="oma kodutöö tegemata. Käes on kontroll-", fill=PAL4, font=("terminal", 10))
    tahvel.create_text(160, 50, text="töö päev, ning sul pole mitte midagi ", fill=PAL4, font=("terminal", 10))
    tahvel.create_text(160, 60, text="õpitud kontrolltööks. Su sõber, klassi", fill=PAL4, font=("terminal", 10))
    tahvel.create_text(160, 70, text="nohik on nõustunud sind aitama. Spikerda", fill=PAL4, font=("terminal", 10))
    tahvel.create_text(160, 80, text="nohiku pealt oma töö maha, ilma et ", fill=PAL4, font=("terminal", 10))
    tahvel.create_text(160, 90, text="õpetaja sind spikerdamas avastaks.", fill=PAL4, font=("terminal", 10))
    tahvel.create_text(160, 130, text="WASD liigutab mängijat", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 140, text="Space spikerdab", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 150, text="3 - esitab töö (olenemata asukohast)", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 160, text="ENTER - mäng pausil", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 170, text="ESC - Välju mängust", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 200, text="Vajuta ENTER et alustada", fill=PAL4, font=("terminal", 10))
    tahvel.create_text(160, 210, text="või X et salvestatud mängu jätkata", fill=PAL4, font=("terminal", 10))
    screenupdate()
    global nooption
    nooption = 0
    while nooption < 1:
        if keyboard.is_pressed("enter"): #continue to next level
            if saveprogress == 0:
                nooption = 1
                return
        #         errorscreen(1101) as level 0 isnt suppose to be playable.
            elif saveprogress == 1:
        #         errorscreen() needed as level 1 is already autoinitialised and never called again.
#                 tahvel.delete("all")
                initialiseroom1()
                screenupdate()
                nooption = 1
                return
            return
#         elif keyboard.is_pressed("z"): #save. currently does nothing. used to save a text file with current progress.             
#         elif keyboard.is_pressed("x"): #load. currently does nothing. used to load a save from a text file.            
        elif keyboard.is_pressed("esc"): #exit game
            quit() #this quits, in later version, this needs to go back to title screen instead
     #uuendab tahvlit liigutatud mängijaga
    time.sleep(0.001)
    
def graphics_bgcolor(a, b):
    tahvel.create_rectangle(0, 0, 320, 240, fill=a, outline=b)
    # joonistab taustavärvi, ei kasuta bgcolor meetodit, on ühtlasi seinavärv

def graphics_carpet(a, b):
    global playercontainer
    playercontainer = tahvel.create_rectangle(8, 8, 232, 232, fill=a, outline=b)
    # joonistab toa sisemuse põrandavärvi, ehk ruumi mille piires mängija liigelda saab
    
def graphics_leftwall_windows(a, b):
    tahvel.create_rectangle(0, 32, 8, 64, fill=a, outline=b)
    tahvel.create_rectangle(0, 96, 8, 128, fill=a, outline=b)
    tahvel.create_rectangle(0, 160, 8, 196, fill=a, outline=b)
    # joonistab vasaku seina aknad

def graphics_rightwall_exitdoor(a, b):
    tahvel.create_rectangle(232, 32, 240, 64, fill=a, outline=b)

def graphics_rightwall_exitdoorlow(a, b):
    tahvel.create_rectangle(232, 200, 240, 232, fill=a, outline=b)
    
def graphics_teacherdesk_leftwall(a, b):
    global Tdesk
    Tdesk = tahvel.create_rectangle(16, 32, 80, 56, fill=a, outline=b)
    # joonistab õpetaja laua vasakusse seina
def graphics_teacherdesk_centerroom(a, b):
    global Tdesk
    Tdesk = tahvel.create_rectangle(80, 32, 144, 56, fill=a, outline=b)
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
def graphics_studentdesklayout_3column(a, b):
    global Sdesk1
    Sdesk1 = tahvel.create_rectangle(16, 64, 44, 208, fill=a, outline=b)
    global Sdesk2
    Sdesk2 = tahvel.create_rectangle(96, 64, 152, 184, fill=a, outline=b)
    global Sdesk3
    Sdesk3 = tahvel.create_rectangle(204, 64, 232, 208, fill=a, outline=b)
    global Sdesk4
    Sdesk4 = tahvel.create_rectangle(-16, -16, -32, -32, fill=a, outline=b) #this xy coordinate writes them out of sight
    global Sdesk5
    Sdesk5 = tahvel.create_rectangle(-16, -16, -32, -32, fill=a, outline=b) #these objects arent needed, but they cannot remain
    global Sdesk6
    Sdesk6 = tahvel.create_rectangle(-16, -16, -32, -32, fill=a, outline=b) #unassigned due to how the program checks collision
    global Sdesk7
    Sdesk7 = tahvel.create_rectangle(-16, -16, -32, -32, fill=a, outline=b) #and erases previous room from the memory when a new
    global Sdesk8
    Sdesk8 = tahvel.create_rectangle(-16, -16, -32, -32, fill=a, outline=b) #level is loaded. as such, this is the engines preset
    global Sdesk9
    Sdesk9 = tahvel.create_rectangle(-16, -16, -32, -32, fill=a, outline=b) #limitation. 9 desks + teachersdesk + screencollisions
    # all these need to be solid, take them into account for collision map
    
def graphics_studentdesklayout_square(a, b):
    global Sdesk1
    Sdesk1 = tahvel.create_rectangle(16, 64, 72, 112, fill=a, outline=b)
    global Sdesk2
    Sdesk2 = tahvel.create_rectangle(96, 112, 152, 160, fill=a, outline=b)
    global Sdesk3
    Sdesk3 = tahvel.create_rectangle(176, 64, 232, 112, fill=a, outline=b)
    global Sdesk4
    Sdesk4 = tahvel.create_rectangle(16, 160, 72, 208, fill=a, outline=b) #this xy coordinate writes them out of sight
    global Sdesk5
    Sdesk5 = tahvel.create_rectangle(176, 160, 232, 208, fill=a, outline=b) #these objects arent needed, but they cannot remain
    global Sdesk6
    Sdesk6 = tahvel.create_rectangle(-16, -16, -32, -32, fill=a, outline=b) #unassigned due to how the program checks collision
    global Sdesk7
    Sdesk7 = tahvel.create_rectangle(-16, -16, -32, -32, fill=a, outline=b) #and erases previous room from the memory when a new
    global Sdesk8
    Sdesk8 = tahvel.create_rectangle(-16, -16, -32, -32, fill=a, outline=b) #level is loaded. as such, this is the engines preset
    global Sdesk9
    Sdesk9 = tahvel.create_rectangle(-16, -16, -32, -32, fill=a, outline=b) #limitation. 9 desks + teachersdesk + screencollisions
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
#     tahvel.create_oval(104, 180, 120, 196, fill=a, outline=b) #Player lvl1
    tahvel.create_oval(130, 180, 146, 196, fill=a, outline=b)  #Nerd lvl 1
    
    tahvel.create_oval(184, 80, 200, 96, fill=a, outline=b)
    tahvel.create_oval(208, 84, 224, 100, fill=a, outline=b)
    tahvel.create_oval(184, 130, 200, 146, fill=a, outline=b)
    tahvel.create_oval(208, 128, 224, 144, fill=a, outline=b)
    tahvel.create_oval(184, 180, 200, 196, fill=a, outline=b)
#     tahvel.create_oval(208, 180, 224, 196, fill=a, outline=b) #player lvl4
     # no collision for any of these students. except for the AOE check for the nerd / items
    
def graphics_studentlayout_3column(a, b):
    tahvel.create_oval(46, 64, 62, 80, fill=a, outline=b)
    tahvel.create_oval(48, 84, 64, 100, fill=a, outline=b)
    tahvel.create_oval(43, 104, 59, 120, fill=a, outline=b)
    tahvel.create_oval(44, 128, 60, 144, fill=a, outline=b)
    tahvel.create_oval(44, 180, 60, 196, fill=a, outline=b)
    
    tahvel.create_oval(74, 64, 90, 80, fill=a, outline=b)
    tahvel.create_oval(80, 86, 96, 102, fill=a, outline=b)
    tahvel.create_oval(78, 108, 94, 124, fill=a, outline=b)
    tahvel.create_oval(74, 128, 90, 144, fill=a, outline=b)
    tahvel.create_oval(80, 150, 96, 166, fill=a, outline=b)
    tahvel.create_oval(78, 172, 94, 188, fill=a, outline=b)
    
    tahvel.create_oval(106, 184, 122, 200, fill=a, outline=b)
    
    tahvel.create_oval(148, 70, 164, 86, fill=a, outline=b) #nerd
    tahvel.create_oval(150, 88, 166, 104, fill=a, outline=b)
    tahvel.create_oval(154, 108, 170, 124, fill=a, outline=b)
    tahvel.create_oval(148, 128, 164, 144, fill=a, outline=b)
    tahvel.create_oval(154, 150, 170, 166, fill=a, outline=b)
    tahvel.create_oval(152, 172, 168, 188, fill=a, outline=b)
    
    tahvel.create_oval(184, 80, 200, 96, fill=a, outline=b)
    tahvel.create_oval(188, 104, 204, 120, fill=a, outline=b)
    tahvel.create_oval(184, 130, 200, 146, fill=a, outline=b)
    tahvel.create_oval(192, 150, 208, 166, fill=a, outline=b)
    tahvel.create_oval(184, 180, 200, 196, fill=a, outline=b)
    # no collision for any of these students. except for the AOE check for the nerd / items
    
def graphics_studentlayout_square(a, b):
    tahvel.create_oval(24, 50, 40, 66, fill=a, outline=b)
    tahvel.create_oval(68, 84, 84, 100, fill=a, outline=b)
    tahvel.create_oval(24, 111, 40, 127, fill=a, outline=b)
    tahvel.create_oval(48, 109, 64, 125, fill=a, outline=b)
    
    tahvel.create_oval(24, 207, 40, 223, fill=a, outline=b)
    tahvel.create_oval(50, 143, 66, 159, fill=a, outline=b)
    
    tahvel.create_oval(104, 96, 120, 112, fill=a, outline=b)
    tahvel.create_oval(160, 100, 176, 116, fill=a, outline=b)
    tahvel.create_oval(104, 162, 120, 178, fill=a, outline=b)
    tahvel.create_oval(128, 160, 144, 176, fill=a, outline=b) 
#     tahvel.create_oval(104, 180, 120, 196, fill=a, outline=b) #Player lvl1
#     tahvel.create_oval(130, 180, 146, 196, fill=a, outline=b)  #Nerd lvl 1
    
    tahvel.create_oval(184, 45, 200, 61, fill=a, outline=b)
    tahvel.create_oval(208, 49, 224, 65, fill=a, outline=b)
    tahvel.create_oval(184, 146, 200, 162, fill=a, outline=b)
    tahvel.create_oval(208, 112, 224, 128, fill=a, outline=b)
    tahvel.create_oval(184, 207, 200, 223, fill=a, outline=b)
    tahvel.create_oval(208, 207, 224, 223, fill=a, outline=b)
    # no collision for any of these students. except for the AOE check for the nerd / items
    
def graphics_studentlayout_2person_nerd_pos1(a, b):
    global nerdbox
    nerdbox = tahvel.create_oval(130, 180, 146, 196, fill=a, outline=b) # level 1 position for the nerd
    
def graphics_studentlayout_3column_nerd_pos1(a, b):
    global nerdbox
    nerdbox = tahvel.create_oval(148, 70, 164, 86, fill=a, outline=b) # level 2 position for the nerd
    
def graphics_studentlayout_square_nerd_pos1(a, b):
    global nerdbox
    nerdbox = tahvel.create_oval(129, 97, 145, 113, fill=a, outline=b) # level 3 position for the nerd
    
def graphics_studentlayout_2person_nerd_pos2(a, b):
    global nerdbox
    nerdbox = tahvel.create_oval(24, 80, 40, 96, fill=a, outline=b) # level 4 position for the nerd
    
def graphics_studentlayout_square_nerd_pos2(a, b):
    global nerdbox
    nerdbox = tahvel.create_oval(208, 144, 224, 160, fill=a, outline=b) # level 5 position for the nerd

def graphics_studentlayout_3column_nerd_pos2(a, b):
    global nerdbox
    nerdbox = tahvel.create_oval(129, 186, 145, 202, fill=a, outline=b) # level 6 position for the nerd
    
def graphics_studentlayout_square_nerd_pos3(a, b):
    global nerdbox
    nerdbox = tahvel.create_oval(49, 210, 65, 226, fill=a, outline=b) # level 7 position for the nerd
    
def graphics_studentlayout_3column_nerd_pos3(a, b):
    global nerdbox
    nerdbox = tahvel.create_oval(80, 150, 96, 166, fill=a, outline=b) # level 8 position for the nerd
    
def graphics_studentlayout_2person_nerd_pos3(a, b):
    global nerdbox
    nerdbox = tahvel.create_oval(128, 132, 144, 148, fill=a, outline=b) # level 10 position for the nerd
    
def screenupdate():
    tahvel.pack()
    raam.update()
    # pakib akna graafika kokku, funktsioon kutsutakse iga tsükkel
        
def drawhud():
    tahvel.create_rectangle(240, 0, 320, 240, fill=PAL7, outline=PAL7)
    global AOECHECK
    AOECHECK = tahvel.create_rectangle(248, 8, 256, 16, fill=PAL4, outline=PAL1)
    global TESTGRAPHIC
    TESTGRAPHIC = tahvel.create_polygon(256, 64, 256, 128, 304, 128, 304, 72, 296, 64, 296, 72, 304, 72, 296, 64, fill=PAL8, outline=PAL1)
    global enumerativeline1
    enumerativeline1 = tahvel.create_line(264, 80, 264, 80, fill=PAL1, width=1)
    global enumerativeline2
    enumerativeline2 = tahvel.create_line(264, 88, 264, 88, fill=PAL1, width=1)
    global enumerativeline3
    enumerativeline3 = tahvel.create_line(264, 96, 264, 96, fill=PAL1, width=1)
    global enumerativeline4
    enumerativeline4 = tahvel.create_line(264, 104, 264, 104, fill=PAL1, width=1)
    global enumerativeline5
    enumerativeline5 = tahvel.create_line(264, 112, 264, 112, fill=PAL1, width=1)
    global pausegraphic
    global pausetext
    pausegraphic = tahvel.create_rectangle(248, 208, 312, 232, fill=PAL7, outline=PAL7)
    pausetext = tahvel.create_text(280, 220, text="Pause ", fill=PAL7, font=("terminal", 10))
    global leveltext
    global leveltextcomplete
    leveltext = tahvel.create_text(280, 140, text=str(saveprogress)+". Töö ", fill=PAL1, font=("terminal", 10))
    leveltextcomplete = tahvel.create_text(280, 152, text="Tehtud!", fill=PAL7, font=("terminal", 10))
    
# def drawhud_flair(a, b):
#     
    
#     global COLLWTEXT
#     COLLWTEXT = tahvel.create_text(raam, height=1, width=1)
#     COLLWTEXT.insert("W")
    # joonistab ekraanile leveliga seotud info.
    # siit puudu: soorituse läbivuse protsent / inventory? / periphery proximity indicator
    # / passgrade / time / excuses
    
def hudtest(a):
    tahvel.itemconfig(AOECHECK, fill=a)
    tahvel.itemconfig(TESTGRAPHIC, fill=a)
    global hudtestcompletionlines
    global leveltextcomplete
    if testcompletion < 33:
        hudtestcompletionlines[0] = 264+testcompletion
    elif testcompletion < 65:
        hudtestcompletionlines[1] = 264+(testcompletion - 32)
        hudtestcompletionlines[0] = 264+32
    elif testcompletion < 97:
        hudtestcompletionlines[2] = 264+(testcompletion - 64)
        hudtestcompletionlines[1] = 264+32
        hudtestcompletionlines[0] = 264+32
    elif testcompletion < 129:
        hudtestcompletionlines[3] = 264+(testcompletion - 96)
        hudtestcompletionlines[2] = 264+32
        hudtestcompletionlines[1] = 264+32
        hudtestcompletionlines[0] = 264+32
    elif testcompletion < 161:      
        hudtestcompletionlines[4] = 264+(testcompletion - 128)
        hudtestcompletionlines[3] = 264+32
        hudtestcompletionlines[2] = 264+32
        hudtestcompletionlines[1] = 264+32
        hudtestcompletionlines[0] = 264+32
    elif testcompletion == 160:
        leveltextcomplete = tahvel.create_text(280, 152, text="Tehtud!", fill=PAL6, font=("terminal", 10))
        hudtestcompletionlines[4] = 264+32
        hudtestcompletionlines[3] = 264+32
        hudtestcompletionlines[2] = 264+32
        hudtestcompletionlines[1] = 264+32
        hudtestcompletionlines[0] = 264+32
    tahvel.coords(enumerativeline1, 264, 80, hudtestcompletionlines[0], 80)
    tahvel.coords(enumerativeline2, 264, 88, hudtestcompletionlines[1], 88)
    tahvel.coords(enumerativeline3, 264, 96, hudtestcompletionlines[2], 96)
    tahvel.coords(enumerativeline4, 264, 104, hudtestcompletionlines[3], 104)
    tahvel.coords(enumerativeline5, 264, 112, hudtestcompletionlines[4], 112)
    # uuendab hudil olevaid objekte

def drawplayer():
    global playergraphic
    playergraphic = tahvel.create_oval(startX+playerX, startY+playerY, startX+16+playerX, startY+16+playerY, fill=PAL5, outline=PAL1)
    # joonistab ekraanile mängija, kasutatakse leveli initsialiseerimisel.
    # vana mängija liigutamismeetod kasutas seda ka mängija iga tsükkel uuestijoonistamiseks

def graphics_drawteacher(a, b):
    global teachergraphic
    teachergraphic = tahvel.create_oval(TstartX,TstartY,TstartX +16,TstartY +16, fill=a, outline=b)
    # draws the teacher, for level based patterns

def initialiseroom1():
    global currentlvteacher
    currentlvteacher = teachermove1
    global startX
    global startY
    global TstartX
    global TstartY
    startX = 104
    startY = 188
    TstartX = 81
    TstartY = 53
    drawroom_peterson()
    drawhud()
    drawplayer()
    #graphics_drawteacher(PAL4, PAL1) made it draw the teacher twice
    #initisialiseerib leveli, joonistades leveli, infotabeli (hud) ja mängija.
    #siit puudu: add progress counter +1 /
def initialiseroom2():
    global startX
    global startY
    startX = 47
    startY = 152
    drawroom_class2()
    drawhud()
    drawplayer()
def initialiseroom3():
    global startX
    global startY
    startX = 36
    startY = 208
    drawroom_class3()
    drawhud()
    drawplayer()
def initialiseroom4():
    global startX
    global startY
    startX = 208
    startY = 180
    drawroom_class4()
    drawhud()
    drawplayer()
def initialiseroom5():
    global startX
    global startY
    startX = 48
    startY = 48
    drawroom_class5()
    drawhud()
    drawplayer()
def initialiseroom6():
    global startX
    global startY
    startX = 47
    startY = 152
    drawroom_class6()
    drawhud()
    drawplayer()
def initialiseroom7():
    global startX
    global startY
    startX = 160
    startY = 69
    drawroom_class7()
    drawhud()
    drawplayer()
def initialiseroom8():
    global startX
    global startY
    startX = 186
    startY = 66
    drawroom_class8()
    drawhud()
    drawplayer()
def initialiseroom9():
    global startX
    global startY
    startX = 46
    startY = 63
    drawroom_class9()
    drawhud()
    drawplayer()
def initialiseroom10():
    global startX
    global startY
    startX = 103
    startY = 132
    drawroom_class10()
    drawhud()
    drawplayer()

def end1():
    worksheet()
    tahvel.create_text(160, 24, text="Ending TBD.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 56, text="Game Over", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 72, text="0", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 88, text="0", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 104, text="0", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 120, text="0", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 136, text="0", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 152, text="0", fill=PAL1, font=("terminal", 10))
    global nooption
    nooption = 0
    time.sleep(0.200)
    while nooption < 1:
        if keyboard.is_pressed("enter"): #continue to next level
            nooption = 1
            return
        else:
            screenupdate()
            nooption = 0
            
def end2():
    worksheet()
    tahvel.create_text(160, 24, text="Juhendaja: Kristjan Kivikangur", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 56, text="Mängu tegid:", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 72, text="Jüri Vaitmaa ning", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 88, text="Eva-Kristina Vesiallik", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 120, text="Kasutatud vahendid:", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 136, text="Tkinter, Time, Keyboard moodulid.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 152, text="Otsingumootor google.", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 184, text="Põhineb mängul:", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 200, text="The Classroom (2003, luksy of c404)", fill=PAL1, font=("terminal", 10))
    global nooption
    nooption = 0
    time.sleep(0.200)
    while nooption < 1:
        if keyboard.is_pressed("enter"): #continue to next level
            nooption = 1
            return
        else:
            screenupdate()
            nooption = 0
            
def end3():
    worksheet()
    tahvel.create_text(160, 24, text="Enter viib tagasi titlescreenile", fill=PAL1, font=("terminal", 10))
    tahvel.create_text(160, 56, text="X laeb viimase salvestatud mängu", fill=PAL1, font=("terminal", 10))
    global nooption
    nooption = 0
    while nooption < 1:
        if keyboard.is_pressed("enter"): #continue to next level
            nooption = 1
            return
        else:
            screenupdate()
            nooption = 0

def initialiseending():
    end1()
    end2()
    
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

def YcheckT(int):
    global teacherY
    if teacherY != int:
        teacherY = int
    # kontrollib et mängija liigutusväärtused Y teljel ei oleks suurem kui sisseantav väärtus, 
    # antud juhul eespool on selleks väärtuseks ainult kas 1 või -1
    # hoiab ära "libiseva" liikumise

def XcheckT(int):
    global teacherX
    if teacherX != int:
        teacherX = int
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
        
def f_coll(a, b, c, d, e, f):
    if a-16 < b < c-8 and d-8 < e < f-8:
        collisionstop(Wcollision, Acollision, Scollision, 1)
    elif a-16 < b < c-2 and d < e < f:
        collisionstop(1, Acollision, Scollision, Dcollision)
    elif a-16 < b < c-8 and d-16 < e < f:
        collisionstop(Wcollision, Acollision, 1, Dcollision)
    elif a-8 < b < c and d-16 < e < f:
        collisionstop(Wcollision, 1, Scollision, Dcollision) #Eva
    else:
        collisionstop(0, 0, 0, 0)
            
def f_coll_aoe():
    return #functionalising aoe collisionchecking, currently not used

def collisioncheck_teacherdesk_leftwall():
    playerbox = tahvel.bbox(playergraphic)
    colliderbox = tahvel.bbox(Tdesk)
    if Wcollision == 1 or Acollision == 1 or Scollision == 1 or Dcollision == 1:
        return
    else:
        f_coll(colliderbox[0],playerbox[0],colliderbox[2],colliderbox[1],playerbox[1],colliderbox[3])
#     f_coll2(colliderbox[0],playerbox[0],colliderbox[2],colliderbox[1],playerbox[1],colliderbox[3],TdeskWASD)
    # võrdleb mängija asukohta laua asukohaga ja muudab hudil oleva ruudu roheliseks kui collision on saavutatud
    
def collisioncheck_studentlayout_2person_nerd():
    global nerdregion
    playerbox = tahvel.bbox(playergraphic)
    colliderbox = tahvel.bbox(nerdbox)
    if colliderbox[0] < playerbox[2] < colliderbox[2]+16 and colliderbox[1] < playerbox[3] < colliderbox[3]+16:
        nerdregion = 1
        hudtest(PAL3)
    else:
        nerdregion = 0
        hudtest(PAL8) #checks for the nerd via the action of "why are you setting a value for yourself".
        
def p_coll_W():
    playerbox = tahvel.bbox(playergraphic)
    colliderbox = tahvel.bbox(pcontainerW)
    f_coll(colliderbox[0],playerbox[0],colliderbox[2],colliderbox[1],playerbox[1],colliderbox[3])
def p_coll_A():
    playerbox = tahvel.bbox(playergraphic)
    colliderbox = tahvel.bbox(pcontainerA)
    f_coll(colliderbox[0],playerbox[0],colliderbox[2],colliderbox[1],playerbox[1],colliderbox[3])
def p_coll_S():
    playerbox = tahvel.bbox(playergraphic)
    colliderbox = tahvel.bbox(pcontainerS)
    f_coll(colliderbox[0],playerbox[0],colliderbox[2],colliderbox[1],playerbox[1],colliderbox[3])
def p_coll_D():
    playerbox = tahvel.bbox(playergraphic)
    colliderbox = tahvel.bbox(pcontainerD)
    f_coll(colliderbox[0],playerbox[0],colliderbox[2],colliderbox[1],playerbox[1],colliderbox[3])
    
def collisioncheck_playercontainer():
    if Wcollision == 1 or Acollision == 1 or Scollision == 1 or Dcollision == 1:
        return
    else:
        p_coll_W()
    if Wcollision == 1 or Acollision == 1 or Scollision == 1 or Dcollision == 1:
        return
    else:
        p_coll_A()
    if Wcollision == 1 or Acollision == 1 or Scollision == 1 or Dcollision == 1:
        return
    else:
        p_coll_S()
    if Wcollision == 1 or Acollision == 1 or Scollision == 1 or Dcollision == 1:
        return
    else:
        p_coll_D()

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
    if Wcollision == 1 or Acollision == 1 or Scollision == 1 or Dcollision == 1:
        return
    else:
        cc_sdl_2p_Sdesk1()
    if Wcollision == 1 or Acollision == 1 or Scollision == 1 or Dcollision == 1:
        return
    else:
        cc_sdl_2p_Sdesk2()
    if Wcollision == 1 or Acollision == 1 or Scollision == 1 or Dcollision == 1:
        return
    else:
        cc_sdl_2p_Sdesk3()
    if Wcollision == 1 or Acollision == 1 or Scollision == 1 or Dcollision == 1:
        return
    else:
        cc_sdl_2p_Sdesk4()
    if Wcollision == 1 or Acollision == 1 or Scollision == 1 or Dcollision == 1:
        return
    else:
        cc_sdl_2p_Sdesk5()
    if Wcollision == 1 or Acollision == 1 or Scollision == 1 or Dcollision == 1:
        return
    else:
        cc_sdl_2p_Sdesk6()
    if Wcollision == 1 or Acollision == 1 or Scollision == 1 or Dcollision == 1:
        return
    else:
        cc_sdl_2p_Sdesk7()
    if Wcollision == 1 or Acollision == 1 or Scollision == 1 or Dcollision == 1:
        return
    else:
        cc_sdl_2p_Sdesk8()
    if Wcollision == 1 or Acollision == 1 or Scollision == 1 or Dcollision == 1:
        return
    else:
        cc_sdl_2p_Sdesk9()
    # lauad mida kontrollitakse
    
def hudfunc2(int):
    if int < 160:
        tahvel.itemconfig(leveltextcomplete, fill=PAL7)
    elif int == 160:
        tahvel.itemconfig(leveltextcomplete, fill=PAL6)

def drawroom_peterson():
    roomcollision()
    graphics_bgcolor(PAL2, PAL2)
    graphics_carpet(PAL6, PAL1)
    graphics_leftwall_windows(PAL3, PAL3)
    graphics_rightwall_exitdoor(PAL5, PAL1)
    graphics_teacherdesk_leftwall(PAL5, PAL7)
    graphics_studentdesklayout_2person(PAL5, PAL4)
    graphics_studentlayout_2person(PAL2, PAL3)
    graphics_studentlayout_2person_nerd_pos1(PAL7, PAL1)
    graphics_drawteacher(PAL4, PAL1)
    # spetsiifilise klassiruumi leveli kujundus kasutades eelnevaid joonistusfunktsioone
    # sellel põhimõttel tuleb ka level editor.
    # siit puudu: õpetaja pattern / room event / interactible map
    # LAYOUTS COMPLETED
    
def drawroom_class2():
    roomcollision()
    graphics_bgcolor(PAL3, PAL3)
    graphics_carpet(PAL7, PAL1)
    graphics_leftwall_windows(PAL8, PAL8)
    graphics_teacherdesk_centerroom(PAL5, PAL1)
    graphics_studentdesklayout_3column(PAL8, PAL1)
    graphics_studentlayout_3column(PAL2, PAL1)         
    graphics_studentlayout_3column_nerd_pos1(PAL7, PAL1)    
    graphics_rightwall_exitdoor(PAL5, PAL1)
    # LAYOUTS COMPLETED
    
def drawroom_class3():
    roomcollision()
    graphics_bgcolor(PAL6, PAL2)
    graphics_carpet(PAL7, PAL1)
    graphics_leftwall_windows(PAL3, PAL3)
    graphics_teacherdesk_centerroom(PAL8, PAL1)
    graphics_studentdesklayout_square(PAL5, PAL4)
    graphics_studentlayout_square(PAL2, PAL1)
    graphics_studentlayout_square_nerd_pos1(PAL7, PAL1)
    graphics_rightwall_exitdoor(PAL5, PAL1)
    # LAYOUT IN PROGRESS
    
def drawroom_class4():
    roomcollision()
    graphics_bgcolor(PAL1, PAL1)
    graphics_carpet(PAL4, PAL1)
    graphics_leftwall_windows(PAL3, PAL3)
    graphics_rightwall_exitdoor(PAL5, PAL1)
    graphics_teacherdesk_leftwall(PAL5, PAL7)
    graphics_studentdesklayout_2person(PAL5, PAL1)
    graphics_studentlayout_2person(PAL2, PAL3)
    graphics_studentlayout_2person_nerd_pos2(PAL7, PAL1)
    # spetsiifilise klassiruumi leveli kujundus kasutades eelnevaid joonistusfunktsioone
    # sellel põhimõttel tuleb ka level editor.
    # siit puudu: õpetaja pattern / room event / interactible map
    # LAYOUTS COMPLETED
    
def drawroom_class5():
    roomcollision()
    graphics_bgcolor(PAL5, PAL5)
    graphics_carpet(PAL6, PAL1)
    graphics_leftwall_windows(PAL3, PAL3)
    graphics_teacherdesk_centerroom(PAL8, PAL1)
    graphics_studentdesklayout_square(PAL5, PAL7)
    graphics_studentlayout_square(PAL2, PAL3)
    graphics_studentlayout_square_nerd_pos2(PAL7, PAL1)
    graphics_rightwall_exitdoorlow(PAL8, PAL1)
    # LAYOUTS COMPLETED
    
def drawroom_class6():
    roomcollision()
    graphics_bgcolor(PAL3, PAL3)
    graphics_carpet(PAL7, PAL1)
    graphics_leftwall_windows(PAL8, PAL8)
    graphics_teacherdesk_centerroom(PAL5, PAL1)
    graphics_studentdesklayout_3column(PAL8, PAL1)
    graphics_studentlayout_3column(PAL2, PAL1)         # no room-specific student layout exists yet.
    graphics_studentlayout_3column_nerd_pos2(PAL7, PAL1)    # no room-specific nerd layout exists yet.
    graphics_rightwall_exitdoor(PAL5, PAL1)
    #layouts completed
    
def drawroom_class7():
    roomcollision()
    graphics_bgcolor(PAL6, PAL6)
    graphics_carpet(PAL3, PAL1)
    graphics_leftwall_windows(PAL3, PAL3)
    graphics_teacherdesk_centerroom(PAL6, PAL1)
    graphics_studentdesklayout_square(PAL4, PAL1)
    graphics_studentlayout_square(PAL2, PAL1)
    graphics_studentlayout_square_nerd_pos3(PAL7, PAL1)
    graphics_rightwall_exitdoor(PAL8, PAL1)
    #layouts completed
    
    
def drawroom_class8():
    roomcollision()
    graphics_bgcolor(PAL2, PAL2)
    graphics_carpet(PAL8, PAL8)
    graphics_leftwall_windows(PAL3, PAL3)
    graphics_teacherdesk_centerroom(PAL5, PAL1)
    graphics_studentdesklayout_3column(PAL3, PAL1)
    graphics_studentlayout_3column(PAL2, PAL1)         
    graphics_studentlayout_3column_nerd_pos3(PAL7, PAL1)    
    graphics_rightwall_exitdoor(PAL5, PAL1)
    #layouts completed
    
def drawroom_class9():
    roomcollision()
    graphics_bgcolor(PAL6, PAL6)
    graphics_carpet(PAL4, PAL4)
    graphics_leftwall_windows(PAL8, PAL8)
    graphics_teacherdesk_leftwall(PAL5, PAL1)
    graphics_studentdesklayout_3column(PAL7, PAL1)
    graphics_studentlayout_3column(PAL2, PAL1)         
    graphics_studentlayout_3column_nerd_pos1(PAL7, PAL1)    
    graphics_rightwall_exitdoorlow(PAL5, PAL1)
    
def drawroom_class10():
    roomcollision()
    graphics_bgcolor(PAL2, PAL2)
    graphics_carpet(PAL6, PAL1)
    graphics_leftwall_windows(PAL3, PAL3)
    graphics_teacherdesk_leftwall(PAL5, PAL7)
    graphics_studentdesklayout_2person(PAL5, PAL4)
    graphics_studentlayout_2person_nerd_pos3(PAL7, PAL1)    
    graphics_rightwall_exitdoorlow(PAL5, PAL1)
    
# def drawroom_ending():
#     roomcollision()
#     graphics_bgcolor(PAL2, PAL2)
#     graphics_carpet(PAL6, PAL1)
#     graphics_leftwall_windows(PAL3, PAL3)
#     graphics_teacherdesk_leftwall(PAL5, PAL7)
#     graphics_studentdesklayout_2person(PAL5, PAL4)
#     graphics_studentlayout_2person(PAL2, PAL3)
#     graphics_studentlayout_2person_nerd_pos3(PAL7, PAL1)

def collisionmap_peterson():
    if Wcollision == 1 or Acollision == 1 or Scollision == 1 or Dcollision == 1:
        return
    else:
        collisioncheck_playercontainer()
    if Wcollision == 1 or Acollision == 1 or Scollision == 1 or Dcollision == 1:
        return
    else:
        collisioncheck_teacherdesk_leftwall()
    if Wcollision == 1 or Acollision == 1 or Scollision == 1 or Dcollision == 1:
        return
    else:
        collisioncheck_studentdesklayout_2person()
    if Wcollision == 1 or Acollision == 1 or Scollision == 1 or Dcollision == 1:
        return
    else:
        collisionstop(0,0,0,0)
    collisioncheck_studentlayout_2person_nerd() # nohiku collisioncheck, kasutatud spikerdamiseks
    collisioncheck_playercontainer()
    # leveli collisionmap, ehk kõik kõvad objectid.
    
def moveplayer():
    global playerX
    global playerY
    tahvel.move(playergraphic, playerX, playerY)    
#     playerX == 0
#     playerY == 0
    # liigutab mängijat



def moveteacher():
    global teacherX
    global teacherY
    tahvel.move(teachergraphic, teacherX, teacherY)

def teacherpath():
    global currentlvteacher
    global direction
    global stepcount
    global element
    sequence = currentlvteacher
    elementvalue = 0
    
    if element == len(sequence):
        element = 0
    
    if direction == 0: #up
        elementvalue = sequence[element]
        if stepcount < elementvalue:
            YcheckT(-1)
            XcheckT(0)
            moveteacher()
            stepcount += 1
        elif stepcount == elementvalue:
                element += 1
                stepcount = 0
                direction = 1
              
    if direction == 1: #down
        elementvalue = sequence[element]
        if stepcount < elementvalue:
            YcheckT(+1)
            XcheckT(0)
            moveteacher()
            stepcount += 1
        elif stepcount == elementvalue:
            direction = 2
            element += 1
            stepcount = 0
           
    if direction == 2: #left
        elementvalue = sequence[element]
        if stepcount < elementvalue:
            YcheckT(0)
            XcheckT(-1)
            moveteacher()
            stepcount += 1
        elif stepcount == elementvalue:
            direction = 3
            element += 1
            stepcount = 0
           
    if direction == 3: #right
        elementvalue = sequence[element]
        if stepcount < elementvalue:
            YcheckT(0)
            XcheckT(+1)
            moveteacher()
            stepcount += 1
        elif stepcount == elementvalue:
            direction = 0
            element += 1
            stepcount = 0
        
def pausegame():
    global enterlock
    global pausegraphic
    global pausetext
    global startpause
    enterlock = 0
    while startpause == True:
     #later replace with seize() function which also pauses automoving objects
        if keyboard.is_pressed("enter") and enterlock == 1:
            tahvel.itemconfig(pausegraphic, fill=PAL7, outline=PAL7)
            tahvel.itemconfig(pausetext, fill=PAL7,)
            startpause = False
            collisionstop(0,0,0,0)
            screenupdate()
            time.sleep(0.200)
        else:
            tahvel.itemconfig(pausegraphic, fill=PAL1, outline=PAL8)
            tahvel.itemconfig(pausetext, fill=PAL8,)
            screenupdate()
            if enterlock == 0:
                time.sleep(0.200)
            startpause = True
            collisionstop(1,1,1,1)
            enterlock = 1
    startpause = True
    enterlock = 0
    return

def gameload():
    global saveprogress
    global loadrequested
    f = open("savegame.txt", encoding="UTF-8")
    progress = f.readline()
    f.close
    saveprogress = int(progress)
    loadrequested = 1
    levelclear_gotonext()
    
def gamesave():
    global saveprogress
    f = open("savegame.txt", "w")
    writeintstr = str(saveprogress)
    f.write(writeintstr)
    f.close

def levelclear_gotonext():
    global loadrequested
    global hudtestcompletionlines
    global saveprogress
    global testcompletion
    global currentlevelcompleted
    if loadrequested == 1:
        tahvel.delete("all")        
        hudtestcompletionlines[0] = 264
        hudtestcompletionlines[1] = 264
        hudtestcompletionlines[2] = 264
        hudtestcompletionlines[3] = 264
        hudtestcompletionlines[4] = 264
        testcompletion = 0
        currentlevelcompleted = 0
        tahvel.create_rectangle(0, 0, 320, 240, fill=PAL1, outline=PAL1)
        tahvel.create_text(160, 24, text="savegame loaded", fill=PAL8, font=("terminal", 10))
        tahvel.create_text(160, 36, text="Press enter to continue", fill=PAL8, font=("terminal", 10))
        screenupdate()
        loadrequested = 0
    else:
        tahvel.delete("all")
        hudtestcompletionlines[0] = 264
        hudtestcompletionlines[1] = 264
        hudtestcompletionlines[2] = 264
        hudtestcompletionlines[3] = 264
        hudtestcompletionlines[4] = 264
        saveprogress += 1
        testcompletion = 0
        currentlevelcompleted = 0
        tahvel.create_rectangle(0, 0, 320, 240, fill=PAL1, outline=PAL1)
        tahvel.create_text(160, 24, text="level complete. ", fill=PAL8, font=("terminal", 10))
        tahvel.create_text(160, 36, text="esc to exit, enter to continue", fill=PAL8, font=("terminal", 10))
        tahvel.create_text(160, 48, text="z to save game", fill=PAL8, font=("terminal", 10))
        tahvel.create_text(160, 60, text="x to load game", fill=PAL8, font=("terminal", 10))
        screenupdate()
    #draw screen here
    #keycheck code for save, load, exit and continue in a while loop
    #screen needs to include: next level name and number, current savefile name
    #progress map, some hud data, like lives left.
    global nooption
    nooption = 0
    while nooption < 1:
        if keyboard.is_pressed("enter"): #continue to next level
            if saveprogress == 0:
                nooption = 1
                return
        #         errorscreen(1101) as level 0 isnt suppose to be playable.
            elif saveprogress == 1:
        #         errorscreen() needed as level 1 is already autoinitialised and never called again.
#                 tahvel.delete("all")
                initialiseroom1()
                screenupdate()
                nooption = 1
                return
            elif saveprogress == 2:
#                 tahvel.delete("all")
                story2()
                initialiseroom2()
                screenupdate()
                nooption = 1
                return
            elif saveprogress == 3:
                story3()
#                 tahvel.delete("all")
                initialiseroom3()
                screenupdate()
                nooption = 1
                return
            elif saveprogress == 4:
                story4()
                tahvel.delete("all")
                initialiseroom4()
                screenupdate()
                nooption = 1
                return
            elif saveprogress == 5:
                story5()
                tahvel.delete("all")
                initialiseroom5()
                screenupdate()
                nooption = 1
                return
            elif saveprogress == 6:
                story6()
                tahvel.delete("all")
                initialiseroom6()
                screenupdate()
                nooption = 1
                return
            elif saveprogress == 7:
                story7()
                tahvel.delete("all")
                initialiseroom7()
                screenupdate()
                nooption = 1
                return
            elif saveprogress == 8:
                story8()
                tahvel.delete("all")
                initialiseroom8()
                screenupdate()
                nooption = 1
                return
            elif saveprogress == 9:
                story9()
                tahvel.delete("all")
                initialiseroom9()
                screenupdate()
                nooption = 1
                return
            elif saveprogress == 10:
                story10()
                tahvel.delete("all")
                initialiseroom10()
                screenupdate()
                nooption = 1
                return
            elif saveprogress == 11:
                tahvel.delete("all")
                initialiseending()
                screenupdate()
                nooption = 1
            return
        elif keyboard.is_pressed("z"): #save. currently does nothing. used to save a text file with current progress.
            (0.200)
#             saverequested = 1
            gamesave()
        elif keyboard.is_pressed("x"): #load. currently does nothing. used to load a save from a text file.
            (0.200)
            gameload()
        elif keyboard.is_pressed("esc"): #exit game
            quit() #this quits, in later version, this needs to go back to title screen instead
     #uuendab tahvlit liigutatud mängijaga
    time.sleep(0.001) # 50 fps setting is 0.005. if it is anything other than this, speed is affected
    
splashscreen()
titlescreen() # mäng algab title screenist.
#alljärgnev loop on hetkel mängu main loop. Iga tsükkel kontrollitakse WASD klahve. Liikumissuundi on 8
#hierarhia mille järjekorras klahvikombinatsioone kontrollitakse on sihilik. Kui monokombinatsioone
#kontrollida enne mitmeklahvikombinatsioone, siis ei saa diagonaale mida see kombinatsioon tekitab
#kunagi kontrollida ning mängija ei saa liikuda diagonaalselt.    
while gameExitvalue < 1:
    enterlock = 0
    collisionmap_peterson() #iga WASD tsükkel kontrollitakse selle leveli collisionmappi.
    if keyboard.is_pressed("w") and keyboard.is_pressed("d"):
        if Wcollision == 1 or Dcollision == 1:
            Ycheck(0) #annab Y telje liikumisväärtuse
            Xcheck(0) #annab X telje liikumisvärtuse
        else:
            Ycheck(-1) #annab Y telje liikumisväärtuse
            Xcheck(1) #annab X telje liikumisvärtuse
        moveplayer() #liigutab mängijat
        # kontrollitav suund on üles-paremale
        collisionstop(0,0,0,0)
    elif keyboard.is_pressed("w") and keyboard.is_pressed("a"):
        if Wcollision == 1 or Acollision == 1:
            Ycheck(0)
            Xcheck(0)        
        else:
            Ycheck(-1)
            Xcheck(-1)
        moveplayer()
        collisionstop(0,0,0,0)
        # kontrollitav suund on üles-vasakule
    elif keyboard.is_pressed("w") and keyboard.is_pressed("s"):
        if Wcollision == 1 or Scollision == 1:
            Xcheck(0)
            Ycheck(0)           
        else:
            Xcheck(0)
            Ycheck(0)
        moveplayer()
        collisionstop(0,0,0,0)
        # kontrollitakse vastastikku liigutavate klahvide kombinatsiooni, mis paneb mängija seisma
    elif keyboard.is_pressed("a") and keyboard.is_pressed("s"):
        if Acollision == 1 or Scollision == 1:
            Xcheck(0)
            Ycheck(0)
        else:
            Xcheck(-1)
            Ycheck(1)
        moveplayer()
        collisionstop(0,0,0,0)
        # kontrollitav suund on vasakule-alla
    elif keyboard.is_pressed("a") and keyboard.is_pressed("d"):
        if Acollision == 1 or Dcollision == 1:
            Xcheck(0)
            Ycheck(0)         
        else:
            Xcheck(0)
            Ycheck(0)
        moveplayer()
        collisionstop(0,0,0,0)
        # kontrollitakse vastastikku liigutavate klahvide kombinatsiooni, mis paneb mängija seisma
    elif keyboard.is_pressed("s") and keyboard.is_pressed("d"):
        if Scollision == 1 or Dcollision == 1:
            Ycheck(0)
            Xcheck(0)         
        else:
            Ycheck(1)
            Xcheck(1)
        moveplayer()
        collisionstop(0,0,0,0)
        # kontrollitav suund on alla-paremale
    elif keyboard.is_pressed("w"):
        if Wcollision == 1:
            Ycheck(0)
            Xcheck(0)
        else:
            Ycheck(-1)
            Xcheck(0)
        moveplayer()
        collisionstop(0,0,0,0)
        # kontrollitav suund on üles
    elif keyboard.is_pressed("a"):
        if Acollision == 1:
            Xcheck(0)
            Ycheck(0)
        else:
            Xcheck(-1)
            Ycheck(0)
        moveplayer()
        collisionstop(0,0,0,0)
        # kontrollitav suund on vasakule
    elif keyboard.is_pressed("s"):
        if Scollision == 1:
            Ycheck(0)
            Xcheck(0)
        else:
            Ycheck(1)
            Xcheck(0)
        moveplayer()
        collisionstop(0,0,0,0)
        # kontrollitav suund on alla
    elif keyboard.is_pressed("d"):
        if Dcollision == 1:
            Xcheck(0)
            Ycheck(0)
        else:
            Xcheck(1)
            Ycheck(0)
        moveplayer()
        collisionstop(0,0,0,0)
        # kontrollitav suund on paremale
    # järgnev kood otsib teisi klahve. nagu space, shift ja enter.
    hudfunc2(testcompletion)
    if keyboard.is_pressed("space") and nerdregion == True and currentlevelcompleted != 1:
        if keyboard.is_pressed("space") and nerdregion == True and getkeytriggerspeed == 0:
            getkeytriggerspeed = 1
        elif keyboard.is_pressed("space") and nerdregion == True and getkeytriggerspeed == 1:
            getkeytriggerspeed = 0
            testcompletion += 1
    elif keyboard.is_pressed("enter") and startpause == True and enterlock == 0:
        pausegame()
    if testcompletion == 160:
        currentlevelcompleted = 1
    else:
        currentlevelcompleted = 0
    if keyboard.is_pressed("3") and currentlevelcompleted == 1:
        turnintest = 1
    if turnintest == 1:
#         screenupdate()
        turnintest = 0
        levelclear_gotonext()
        nooption = 0
    if keyboard.is_pressed("4"):
        collisionstop(1,1,1,1)
#         failstate_inlevel() #test function for level failure
        failstate_caughtscreen()
    teacherpath()
    screenupdate() #uuendab tahvlit liigutatud mängijaga
    time.sleep(0.001) # 50 fps setting is 0.005. if it is anything other than this, speed is affected
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
# - done - draw level  (still need desk and student gfx, see collision below)
# - done - move player
# - done - check collision 
# - done - split collision types into solid and AOE (also implement student & desk/chair graphics)
# - done - more robust gameloop allowing for multiple levels
# - WIP  - teachers & moving the teachers around on predetermined paths. this includes the AOE FOV
# - done - pause menu & title screen (involves modifying the gameloop more)
# - done - save game & load game systems basing on text files
# - done - ending & failstate
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
# unused variables:
#
# # COLLWTEXT = None
# COLLATEXT = None
# COLLSTEXT = None
# COLLDTEXT = None
# TdeskWASD = [0,0,0,0]
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


# def collisionstoplist(a, b, c, d, list):
#     global Wcollision
#     Wcollision = a + list[0]
#     if Wcollision > 1:
#         Wcollision == 1
#     global Acollision
#     Acollision = b + list[1]
#     if Acollision > 1:
#         Acollision == 1
#     global Scollision
#     Scollision = c + list[2]
#     if Scollision > 1:
#         Scollision == 1
#     global Dcollision
#     Dcollision = d + list[3]
#     if Dcollision > 1:
#         Dcollision == 1
# def f_coll2(a, b, c, d, e, f, list):
#     if a-16 < b < c-8 and d-8 < e < f-8:
#         hudtest(PAL6)
#         collisionstoplist(Wcollision, Acollision, Scollision, 1, list)
#     elif a-16 < b < c-2 and d < e < f:
#         hudtest(PAL6)
#         collisionstoplist(1, Acollision, Scollision, Dcollision, list)
#     elif a-16 < b < c-8 and d-16 < e < f:
#         hudtest(PAL6)
#         collisionstoplist(Wcollision, Acollision,1 , Dcollision, list)
#     elif a-8 < b < c and d-16 < e < f:
#         hudtest(PAL6)
#         collisionstoplist(Wcollision, 1, Scollision, Dcollision, list) #Eva
#     else:
#         collisionstoplist(0, 0, 0, 0, list)
#         hudtest(PAL4)
# 
# def tograyscale():
#     global PAL2
#     global PAL3
#     global PAL4
#     global PAL5
#     global PAL6
#     global PAL7
#     PAL2 = "DimGray"
#     PAL3 = "Gainsboro"
#     PAL4 = "DarkGray"
#     PAL5 = "Silver"
#     PAL6 = "Gray"
#     PAL7 = "LightGray"
#     
# def graphics_failstate():
#     tahvel.create_text(162, 62, text="TABATUD", fill=PAL8, font=("terminal", 32))
#     tahvel.create_text(158, 66, text="TABATUD", fill=PAL8, font=("terminal", 32))
#     tahvel.create_text(162, 66, text="TABATUD", fill=PAL8, font=("terminal", 32))
#     tahvel.create_text(158, 62, text="TABATUD", fill=PAL8, font=("terminal", 32))
#     tahvel.create_text(160, 64, text="TABATUD", fill=SPAL9, font=("terminal", 32))
#     tahvel.create_text(160, 120, text="ENTER alustab esimeselt levelilt uuesti", fill=SPAL9, font=("terminal", 10))
#     tahvel.create_text(160, 136, text="X laeb salvestatud mängu", fill=SPAL9, font=("terminal", 10))
# 
# def failstate_inlevel():
#     tograyscale()
#     #need to redraw graphics with new palette. otherwise, no bueno
#     graphics_failstate()
#     screenupdate()    
#     global nooption
#     nooption = 0
#     while nooption < 1:
#         if keyboard.is_pressed("enter"): #continue to next level
#             if saveprogress == 0:
#                 nooption = 1
#                 return
#         #         errorscreen(1101) as level 0 isnt suppose to be playable.
#             elif saveprogress == 1:
#         #         errorscreen() needed as level 1 is already autoinitialised and never called again.
# #                 tahvel.delete("all")
#                 initialiseroom1()
#                 screenupdate()
#                 nooption = 1
#                 return
#             return
#         elif keyboard.is_pressed("z"): #save. currently does nothing. used to save a text file with current progress.
#             instructions()
# #         elif keyboard.is_pressed("x"): #load. currently does nothing. used to load a save from a text file.            
#         elif keyboard.is_pressed("esc"): #exit game
#             quit() #this quits, in later version, this needs to go back to title screen instead
#      #uuendab tahvlit liigutatud mängijaga
#     time.sleep(0.001)
#     
# #     PAL2 = "blue" #paletti 2. värv - tumesinine. paletti muudetakse vajaduselt ekraanil olevale graafikale.
# #     PAL3 = "cyan" #paletti 3. värv - helesinine. paletti muudetakse vajaduselt ekraanil olevale graafikale.
# #     PAL4 = "red" #paletti 4. värv - punane. paletti muudetakse vajaduselt ekraanil olevale graafikale.
# #     PAL5 = "orange" #paletti 5. värv - oranz. paletti muudetakse vajaduselt ekraanil olevale graafikale.
# #     PAL6 = "green" #paletti 6. värv - roheline. paletti muudetakse vajaduselt ekraanil olevale graafikale.
# #     PAL7 = "yellow" #paletti 7. värv - kollane. paletti muudetakse vajaduselt ekraanil olevale graafikale.
