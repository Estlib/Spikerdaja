```flow
st=>start: Start
op2=>operation: from tkinter import *
op4=>operation: import time
op6=>operation: import keyboard
op8=>operation: raam = Tk()
sub10=>subroutine: raam.title('Spikerdaja')
op12=>operation: tahvel = Canvas(raam, width=320, height=240)
op14=>operation: playerX = 0
op16=>operation: playerY = 0
op18=>operation: startX = 104
op20=>operation: startY = 188
op22=>operation: PAL1 = 'black'
op24=>operation: PAL2 = 'blue'
op26=>operation: PAL3 = 'cyan'
op28=>operation: PAL4 = 'red'
op30=>operation: PAL5 = 'orange'
op32=>operation: PAL6 = 'green'
op34=>operation: PAL7 = 'yellow'
op36=>operation: PAL8 = 'white'
op38=>operation: SPAL9 = 'red'
op40=>operation: gameExitvalue = 0
op42=>operation: saveprogress = 1
op44=>operation: editorsave = 0
op46=>operation: playergraphic = None
op48=>operation: Tdesk = None
op50=>operation: Sdesk1 = None
op52=>operation: Sdesk2 = None
op54=>operation: Sdesk3 = None
op56=>operation: Sdesk4 = None
op58=>operation: Sdesk5 = None
op60=>operation: Sdesk6 = None
op62=>operation: Sdesk7 = None
op64=>operation: Sdesk8 = None
op66=>operation: Sdesk9 = None
op68=>operation: AOECHECK = None
op70=>operation: TESTGRAPHIC = None
op72=>operation: Wcollision = 0
op74=>operation: Acollision = 0
op76=>operation: Scollision = 0
op78=>operation: Dcollision = 0
op80=>operation: nerdbox = None
op82=>operation: testcompletion = 0
op84=>operation: currentlevelcompleted = 0
op86=>operation: hudtestcompletionlines = [264, 264, 264, 264, 264]
op88=>operation: nerdregion = None
op90=>operation: startpause = True
op92=>operation: enumerativeline1 = None
op94=>operation: enumerativeline2 = None
op96=>operation: enumerativeline3 = None
op98=>operation: enumerativeline4 = None
op100=>operation: enumerativeline5 = None
op102=>operation: getkeytriggerspeed = 0
op104=>operation: nooption = 0
op106=>operation: turnintest = 0
op108=>operation: pausegraphic = None
op110=>operation: pausetext = None
op112=>operation: enterlock = 0
op114=>operation: playercontainer = None
op116=>operation: pcontainerW = None
op118=>operation: pcontainerA = None
op120=>operation: pcontainerS = None
op122=>operation: pcontainerD = None
op124=>operation: saverequested = 0
op126=>operation: loadrequested = 0
op128=>operation: leveltext = None
op130=>operation: leveltextcomplete = None
st133=>start: start splashscreen
io135=>inputoutput: input: 
sub138=>subroutine: tahvel.create_rectangle(0, 0, 320, 240, fill=PAL8, outline=PAL8)
op140=>operation: img = PhotoImage(file='TTHK-logo.ppm')
sub142=>subroutine: tahvel.create_image(8, 50, anchor=NW, image=img)
sub144=>subroutine: screenupdate()
sub146=>subroutine: time.sleep(3.0)
e148=>end: end splashscreen
st152=>start: start roomcollision
io154=>inputoutput: input: 
op157=>operation: global pcontainerW
op159=>operation: pcontainerW = tahvel.create_rectangle(0, 0, (- 8), 240, fill=PAL8, outline=PAL8)
op161=>operation: global pcontainerA
op163=>operation: pcontainerA = tahvel.create_rectangle(0, (- 8), 320, 0, fill=PAL8, outline=PAL8)
op165=>operation: global pcontainerS
op167=>operation: pcontainerS = tahvel.create_rectangle(240, 0, 320, 240, fill=PAL8, outline=PAL8)
op169=>operation: global pcontainerD
op171=>operation: pcontainerD = tahvel.create_rectangle(0, 240, 320, 248, fill=PAL8, outline=PAL8)
e173=>end: end roomcollision
st177=>start: start worksheet
io179=>inputoutput: input: 
sub182=>subroutine: tahvel.create_rectangle(0, 0, 320, 240, fill=PAL8, outline=PAL8)
sub184=>subroutine: tahvel.create_line(0, 0, 0, 240, fill=PAL3, width=1)
sub186=>subroutine: tahvel.create_line(16, 0, 16, 240, fill=PAL3, width=1)
sub188=>subroutine: tahvel.create_line(32, 0, 32, 240, fill=PAL3, width=1)
sub190=>subroutine: tahvel.create_line(48, 0, 48, 240, fill=PAL3, width=1)
sub192=>subroutine: tahvel.create_line(64, 0, 64, 240, fill=PAL3, width=1)
sub194=>subroutine: tahvel.create_line(80, 0, 80, 240, fill=PAL3, width=1)
sub196=>subroutine: tahvel.create_line(96, 0, 96, 240, fill=PAL3, width=1)
sub198=>subroutine: tahvel.create_line(112, 0, 112, 240, fill=PAL3, width=1)
sub200=>subroutine: tahvel.create_line(128, 0, 128, 240, fill=PAL3, width=1)
sub202=>subroutine: tahvel.create_line(144, 0, 144, 240, fill=PAL3, width=1)
sub204=>subroutine: tahvel.create_line(160, 0, 160, 240, fill=PAL3, width=1)
sub206=>subroutine: tahvel.create_line(176, 0, 176, 240, fill=PAL3, width=1)
sub208=>subroutine: tahvel.create_line(192, 0, 192, 240, fill=PAL3, width=1)
sub210=>subroutine: tahvel.create_line(208, 0, 208, 240, fill=PAL3, width=1)
sub212=>subroutine: tahvel.create_line(224, 0, 224, 240, fill=PAL3, width=1)
sub214=>subroutine: tahvel.create_line(240, 0, 240, 240, fill=PAL3, width=1)
sub216=>subroutine: tahvel.create_line(256, 0, 256, 240, fill=PAL3, width=1)
sub218=>subroutine: tahvel.create_line(272, 0, 272, 240, fill=PAL3, width=1)
sub220=>subroutine: tahvel.create_line(288, 0, 288, 240, fill=PAL3, width=1)
sub222=>subroutine: tahvel.create_line(304, 0, 304, 240, fill=PAL3, width=1)
sub224=>subroutine: tahvel.create_line(320, 0, 320, 240, fill=PAL3, width=1)
sub226=>subroutine: tahvel.create_line(0, 0, 320, 0, fill=PAL3, width=1)
sub228=>subroutine: tahvel.create_line(0, 16, 320, 16, fill=PAL3, width=1)
sub230=>subroutine: tahvel.create_line(0, 32, 320, 32, fill=PAL3, width=1)
sub232=>subroutine: tahvel.create_line(0, 48, 320, 48, fill=PAL3, width=1)
sub234=>subroutine: tahvel.create_line(0, 64, 320, 64, fill=PAL3, width=1)
sub236=>subroutine: tahvel.create_line(0, 80, 320, 80, fill=PAL3, width=1)
sub238=>subroutine: tahvel.create_line(0, 96, 320, 96, fill=PAL3, width=1)
sub240=>subroutine: tahvel.create_line(0, 112, 320, 112, fill=PAL3, width=1)
sub242=>subroutine: tahvel.create_line(0, 128, 320, 128, fill=PAL3, width=1)
sub244=>subroutine: tahvel.create_line(0, 144, 320, 144, fill=PAL3, width=1)
sub246=>subroutine: tahvel.create_line(0, 160, 320, 160, fill=PAL3, width=1)
sub248=>subroutine: tahvel.create_line(0, 176, 320, 176, fill=PAL3, width=1)
sub250=>subroutine: tahvel.create_line(0, 192, 320, 192, fill=PAL3, width=1)
sub252=>subroutine: tahvel.create_line(0, 208, 320, 208, fill=PAL3, width=1)
sub254=>subroutine: tahvel.create_line(0, 224, 320, 224, fill=PAL3, width=1)
sub256=>subroutine: tahvel.create_line(0, 240, 320, 240, fill=PAL3, width=1)
e258=>end: end worksheet
st262=>start: start story1
io264=>inputoutput: input: 
sub267=>subroutine: worksheet()
sub269=>subroutine: tahvel.create_text(160, 24, text='Esimene kontrolltöö.', fill=PAL1, font=('terminal', 10))
sub271=>subroutine: tahvel.create_text(160, 56, text='Nohik ütles et aitab mind, kuigi', fill=PAL1, font=('terminal', 10))
sub273=>subroutine: tahvel.create_text(160, 72, text='ma teda väga ei usu. Istun klassis', fill=PAL1, font=('terminal', 10))
sub275=>subroutine: tahvel.create_text(160, 88, text='ta kõrvale, vaatan kas peab oma', fill=PAL1, font=('terminal', 10))
sub277=>subroutine: tahvel.create_text(160, 104, text='sõnast kinni. Kui ei pea, siis...', fill=PAL1, font=('terminal', 10))
sub279=>subroutine: tahvel.create_text(160, 120, text='siis on nii minu, kui tema lips läbi', fill=PAL1, font=('terminal', 10))
op281=>operation: global nooption
op283=>operation: nooption = 0
sub285=>subroutine: time.sleep(0.2)
cond288=>condition: while (nooption < 1)
cond312=>condition: if keyboard.is_pressed('enter')
op316=>operation: nooption = 1
e319=>end: end function return
sub324=>subroutine: screenupdate()
op326=>operation: nooption = 0
e331=>end: end story1
st335=>start: start story2
io337=>inputoutput: input: 
sub340=>subroutine: worksheet()
sub342=>subroutine: tahvel.create_text(160, 24, text='Teine kontrolltöö.', fill=PAL1, font=('terminal', 10))
sub344=>subroutine: tahvel.create_text(160, 56, text='Olen oma hinnetega nii kraavis, et', fill=PAL1, font=('terminal', 10))
sub346=>subroutine: tahvel.create_text(160, 72, text='ühest spikerdamisest ei piisa. Ta', fill=PAL1, font=('terminal', 10))
sub348=>subroutine: tahvel.create_text(160, 88, text='lubas ka edaspidigi aidata, ainult', fill=PAL1, font=('terminal', 10))
sub350=>subroutine: tahvel.create_text(160, 104, text='et õpetaja on haisu ninna saanud.', fill=PAL1, font=('terminal', 10))
sub352=>subroutine: tahvel.create_text(160, 120, text='Ta ei lase mul enam koos nohikuga', fill=PAL1, font=('terminal', 10))
sub354=>subroutine: tahvel.create_text(160, 136, text='istuda, paneb minu alati kuskile', fill=PAL1, font=('terminal', 10))
sub356=>subroutine: tahvel.create_text(160, 152, text='mujale istuma. :C', fill=PAL1, font=('terminal', 10))
op358=>operation: global nooption
op360=>operation: nooption = 0
sub362=>subroutine: time.sleep(0.2)
cond365=>condition: while (nooption < 1)
cond389=>condition: if keyboard.is_pressed('enter')
op393=>operation: nooption = 1
e396=>end: end function return
sub401=>subroutine: screenupdate()
op403=>operation: nooption = 0
e408=>end: end story2
st412=>start: start story3
io414=>inputoutput: input: 
sub417=>subroutine: worksheet()
sub419=>subroutine: tahvel.create_text(160, 24, text='Kolmas kontrolltöö.', fill=PAL1, font=('terminal', 10))
sub421=>subroutine: tahvel.create_text(160, 56, text='story3', fill=PAL1, font=('terminal', 10))
sub423=>subroutine: tahvel.create_text(160, 72, text='0', fill=PAL1, font=('terminal', 10))
sub425=>subroutine: tahvel.create_text(160, 88, text='0', fill=PAL1, font=('terminal', 10))
sub427=>subroutine: tahvel.create_text(160, 104, text='0', fill=PAL1, font=('terminal', 10))
sub429=>subroutine: tahvel.create_text(160, 120, text='0', fill=PAL1, font=('terminal', 10))
sub431=>subroutine: tahvel.create_text(160, 136, text='0', fill=PAL1, font=('terminal', 10))
sub433=>subroutine: tahvel.create_text(160, 152, text='0', fill=PAL1, font=('terminal', 10))
op435=>operation: global nooption
op437=>operation: nooption = 0
sub439=>subroutine: time.sleep(0.2)
cond442=>condition: while (nooption < 1)
cond466=>condition: if keyboard.is_pressed('enter')
op470=>operation: nooption = 1
e473=>end: end function return
sub478=>subroutine: screenupdate()
op480=>operation: nooption = 0
e485=>end: end story3
st489=>start: start story4
io491=>inputoutput: input: 
sub494=>subroutine: worksheet()
sub496=>subroutine: tahvel.create_text(160, 24, text='Neljas kontrolltöö.', fill=PAL1, font=('terminal', 10))
sub498=>subroutine: tahvel.create_text(160, 56, text='story4', fill=PAL1, font=('terminal', 10))
sub500=>subroutine: tahvel.create_text(160, 72, text='0', fill=PAL1, font=('terminal', 10))
sub502=>subroutine: tahvel.create_text(160, 88, text='0', fill=PAL1, font=('terminal', 10))
sub504=>subroutine: tahvel.create_text(160, 104, text='0', fill=PAL1, font=('terminal', 10))
sub506=>subroutine: tahvel.create_text(160, 120, text='0', fill=PAL1, font=('terminal', 10))
sub508=>subroutine: tahvel.create_text(160, 136, text='0', fill=PAL1, font=('terminal', 10))
sub510=>subroutine: tahvel.create_text(160, 152, text='0', fill=PAL1, font=('terminal', 10))
op512=>operation: global nooption
op514=>operation: nooption = 0
sub516=>subroutine: time.sleep(0.2)
cond519=>condition: while (nooption < 1)
cond543=>condition: if keyboard.is_pressed('enter')
op547=>operation: nooption = 1
e550=>end: end function return
sub555=>subroutine: screenupdate()
op557=>operation: nooption = 0
e562=>end: end story4
st566=>start: start story5
io568=>inputoutput: input: 
sub571=>subroutine: worksheet()
sub573=>subroutine: tahvel.create_text(160, 24, text='Viies kontrolltöö.', fill=PAL1, font=('terminal', 10))
sub575=>subroutine: tahvel.create_text(160, 56, text='story5', fill=PAL1, font=('terminal', 10))
sub577=>subroutine: tahvel.create_text(160, 72, text='0', fill=PAL1, font=('terminal', 10))
sub579=>subroutine: tahvel.create_text(160, 88, text='0', fill=PAL1, font=('terminal', 10))
sub581=>subroutine: tahvel.create_text(160, 104, text='0', fill=PAL1, font=('terminal', 10))
sub583=>subroutine: tahvel.create_text(160, 120, text='0', fill=PAL1, font=('terminal', 10))
sub585=>subroutine: tahvel.create_text(160, 136, text='0', fill=PAL1, font=('terminal', 10))
sub587=>subroutine: tahvel.create_text(160, 152, text='0', fill=PAL1, font=('terminal', 10))
op589=>operation: global nooption
op591=>operation: nooption = 0
sub593=>subroutine: time.sleep(0.2)
cond596=>condition: while (nooption < 1)
cond620=>condition: if keyboard.is_pressed('enter')
op624=>operation: nooption = 1
e627=>end: end function return
sub632=>subroutine: screenupdate()
op634=>operation: nooption = 0
e639=>end: end story5
st643=>start: start story6
io645=>inputoutput: input: 
sub648=>subroutine: worksheet()
sub650=>subroutine: tahvel.create_text(160, 24, text='Kuues kontrolltöö.', fill=PAL1, font=('terminal', 10))
sub652=>subroutine: tahvel.create_text(160, 56, text='story6', fill=PAL1, font=('terminal', 10))
sub654=>subroutine: tahvel.create_text(160, 72, text='0', fill=PAL1, font=('terminal', 10))
sub656=>subroutine: tahvel.create_text(160, 88, text='0', fill=PAL1, font=('terminal', 10))
sub658=>subroutine: tahvel.create_text(160, 104, text='0', fill=PAL1, font=('terminal', 10))
sub660=>subroutine: tahvel.create_text(160, 120, text='0', fill=PAL1, font=('terminal', 10))
sub662=>subroutine: tahvel.create_text(160, 136, text='0', fill=PAL1, font=('terminal', 10))
sub664=>subroutine: tahvel.create_text(160, 152, text='0', fill=PAL1, font=('terminal', 10))
op666=>operation: global nooption
op668=>operation: nooption = 0
sub670=>subroutine: time.sleep(0.2)
cond673=>condition: while (nooption < 1)
cond697=>condition: if keyboard.is_pressed('enter')
op701=>operation: nooption = 1
e704=>end: end function return
sub709=>subroutine: screenupdate()
op711=>operation: nooption = 0
e716=>end: end story6
st720=>start: start story7
io722=>inputoutput: input: 
sub725=>subroutine: worksheet()
sub727=>subroutine: tahvel.create_text(160, 24, text='Seitsmes kontrolltöö.', fill=PAL1, font=('terminal', 10))
sub729=>subroutine: tahvel.create_text(160, 56, text='story7', fill=PAL1, font=('terminal', 10))
sub731=>subroutine: tahvel.create_text(160, 72, text='0', fill=PAL1, font=('terminal', 10))
sub733=>subroutine: tahvel.create_text(160, 88, text='0', fill=PAL1, font=('terminal', 10))
sub735=>subroutine: tahvel.create_text(160, 104, text='0', fill=PAL1, font=('terminal', 10))
sub737=>subroutine: tahvel.create_text(160, 120, text='0', fill=PAL1, font=('terminal', 10))
sub739=>subroutine: tahvel.create_text(160, 136, text='0', fill=PAL1, font=('terminal', 10))
sub741=>subroutine: tahvel.create_text(160, 152, text='0', fill=PAL1, font=('terminal', 10))
op743=>operation: global nooption
op745=>operation: nooption = 0
sub747=>subroutine: time.sleep(0.2)
cond750=>condition: while (nooption < 1)
cond774=>condition: if keyboard.is_pressed('enter')
op778=>operation: nooption = 1
e781=>end: end function return
sub786=>subroutine: screenupdate()
op788=>operation: nooption = 0
e793=>end: end story7
st797=>start: start story8
io799=>inputoutput: input: 
sub802=>subroutine: worksheet()
sub804=>subroutine: tahvel.create_text(160, 24, text='Kaheksas kontrolltöö.', fill=PAL1, font=('terminal', 10))
sub806=>subroutine: tahvel.create_text(160, 56, text='story8', fill=PAL1, font=('terminal', 10))
sub808=>subroutine: tahvel.create_text(160, 72, text='0', fill=PAL1, font=('terminal', 10))
sub810=>subroutine: tahvel.create_text(160, 88, text='0', fill=PAL1, font=('terminal', 10))
sub812=>subroutine: tahvel.create_text(160, 104, text='0', fill=PAL1, font=('terminal', 10))
sub814=>subroutine: tahvel.create_text(160, 120, text='0', fill=PAL1, font=('terminal', 10))
sub816=>subroutine: tahvel.create_text(160, 136, text='0', fill=PAL1, font=('terminal', 10))
sub818=>subroutine: tahvel.create_text(160, 152, text='0', fill=PAL1, font=('terminal', 10))
op820=>operation: global nooption
op822=>operation: nooption = 0
sub824=>subroutine: time.sleep(0.2)
cond827=>condition: while (nooption < 1)
cond851=>condition: if keyboard.is_pressed('enter')
op855=>operation: nooption = 1
e858=>end: end function return
sub863=>subroutine: screenupdate()
op865=>operation: nooption = 0
e870=>end: end story8
st874=>start: start story9
io876=>inputoutput: input: 
sub879=>subroutine: worksheet()
sub881=>subroutine: tahvel.create_text(160, 24, text='Üheksas kontrolltöö.', fill=PAL1, font=('terminal', 10))
sub883=>subroutine: tahvel.create_text(160, 56, text='story9', fill=PAL1, font=('terminal', 10))
sub885=>subroutine: tahvel.create_text(160, 72, text='0', fill=PAL1, font=('terminal', 10))
sub887=>subroutine: tahvel.create_text(160, 88, text='0', fill=PAL1, font=('terminal', 10))
sub889=>subroutine: tahvel.create_text(160, 104, text='0', fill=PAL1, font=('terminal', 10))
sub891=>subroutine: tahvel.create_text(160, 120, text='0', fill=PAL1, font=('terminal', 10))
sub893=>subroutine: tahvel.create_text(160, 136, text='0', fill=PAL1, font=('terminal', 10))
sub895=>subroutine: tahvel.create_text(160, 152, text='0', fill=PAL1, font=('terminal', 10))
op897=>operation: global nooption
op899=>operation: nooption = 0
sub901=>subroutine: time.sleep(0.2)
cond904=>condition: while (nooption < 1)
cond928=>condition: if keyboard.is_pressed('enter')
op932=>operation: nooption = 1
e935=>end: end function return
sub940=>subroutine: screenupdate()
op942=>operation: nooption = 0
e947=>end: end story9
st951=>start: start story10
io953=>inputoutput: input: 
sub956=>subroutine: worksheet()
sub958=>subroutine: tahvel.create_text(160, 24, text='Lõpueksam', fill=PAL1, font=('terminal', 10))
sub960=>subroutine: tahvel.create_text(160, 56, text='story10', fill=PAL1, font=('terminal', 10))
sub962=>subroutine: tahvel.create_text(160, 72, text='0', fill=PAL1, font=('terminal', 10))
sub964=>subroutine: tahvel.create_text(160, 88, text='0', fill=PAL1, font=('terminal', 10))
sub966=>subroutine: tahvel.create_text(160, 104, text='0', fill=PAL1, font=('terminal', 10))
sub968=>subroutine: tahvel.create_text(160, 120, text='0', fill=PAL1, font=('terminal', 10))
sub970=>subroutine: tahvel.create_text(160, 136, text='0', fill=PAL1, font=('terminal', 10))
sub972=>subroutine: tahvel.create_text(160, 152, text='0', fill=PAL1, font=('terminal', 10))
op974=>operation: global nooption
op976=>operation: nooption = 0
sub978=>subroutine: time.sleep(0.2)
cond981=>condition: while (nooption < 1)
cond1005=>condition: if keyboard.is_pressed('enter')
op1009=>operation: nooption = 1
e1012=>end: end function return
sub1017=>subroutine: screenupdate()
op1019=>operation: nooption = 0
e1024=>end: end story10
st1028=>start: start titlescreen
io1030=>inputoutput: input: 
sub1033=>subroutine: worksheet()
sub1035=>subroutine: tahvel.create_text(163, 67, text='Spikerdaja', fill=PAL1, font=('terminal', 32))
sub1037=>subroutine: tahvel.create_text(162, 66, text='Spikerdaja', fill=PAL1, font=('terminal', 32))
sub1039=>subroutine: tahvel.create_text(161, 65, text='Spikerdaja', fill=PAL1, font=('terminal', 32))
sub1041=>subroutine: tahvel.create_text(160, 64, text='Spikerdaja', fill=PAL4, font=('terminal', 32))
sub1043=>subroutine: tahvel.create_text(161, 121, text='ENTER alustab mängu', fill=PAL1, font=('terminal', 10))
sub1045=>subroutine: tahvel.create_text(160, 120, text='ENTER alustab mängu', fill=PAL2, font=('terminal', 10))
sub1047=>subroutine: tahvel.create_text(161, 137, text='Z näitab juhiseid', fill=PAL1, font=('terminal', 10))
sub1049=>subroutine: tahvel.create_text(160, 136, text='Z näitab juhiseid', fill=PAL2, font=('terminal', 10))
sub1051=>subroutine: tahvel.create_text(161, 153, text='X laeb salvestatud mängu', fill=PAL1, font=('terminal', 10))
sub1053=>subroutine: tahvel.create_text(160, 152, text='X laeb salvestatud mängu', fill=PAL2, font=('terminal', 10))
sub1055=>subroutine: tahvel.create_text(160, 184, text='Juhendaja: Kristjan Kivikangur', fill=PAL1, font=('terminal', 10))
sub1057=>subroutine: tahvel.create_text(160, 200, text='Autorid: Jüri Vaitmaa ning', fill=PAL1, font=('terminal', 10))
sub1059=>subroutine: tahvel.create_text(160, 216, text='Eva-Kristina Vesiallik', fill=PAL1, font=('terminal', 10))
sub1061=>subroutine: tahvel.create_text(160, 232, text='TTHK TARge21 - 2021 v3.1x', fill=PAL1, font=('terminal', 10))
sub1063=>subroutine: screenupdate()
op1065=>operation: global nooption
op1067=>operation: nooption = 0
cond1070=>condition: while (nooption < 1)
cond1155=>condition: if keyboard.is_pressed('enter')
cond1160=>condition: if (saveprogress == 0)
op1164=>operation: nooption = 1
e1167=>end: end function return
cond1173=>condition: if (saveprogress == 1)
sub1177=>subroutine: story1()
sub1179=>subroutine: initialiseroom1()
sub1181=>subroutine: screenupdate()
op1183=>operation: nooption = 1
e1186=>end: end function return
e1194=>end: end function return
cond1200=>condition: if keyboard.is_pressed('z')
sub1204=>subroutine: instructions()
cond1209=>condition: if keyboard.is_pressed('x')
op1213=>operation: loadrequested = 1
sub1215=>subroutine: gameload()
cond1220=>operation: quit() if  keyboard.is_pressed('esc')
sub1235=>subroutine: time.sleep(0.001)
e1237=>end: end titlescreen
st1241=>start: start instructions
io1243=>inputoutput: input: 
sub1246=>subroutine: worksheet()
sub1248=>subroutine: tahvel.create_text(160, 10, text='Juhised: ', fill=PAL4, font=('terminal', 10))
sub1250=>subroutine: tahvel.create_text(160, 30, text='Oled lohakas õpilane ning oled jätnud', fill=PAL4, font=('terminal', 10))
sub1252=>subroutine: tahvel.create_text(160, 40, text='oma kodutöö tegemata. Käes on kontroll-', fill=PAL4, font=('terminal', 10))
sub1254=>subroutine: tahvel.create_text(160, 50, text='töö päev, ning sul pole mitte midagi ', fill=PAL4, font=('terminal', 10))
sub1256=>subroutine: tahvel.create_text(160, 60, text='õpitud kontrolltööks. Su sõber, klassi', fill=PAL4, font=('terminal', 10))
sub1258=>subroutine: tahvel.create_text(160, 70, text='nohik on nõustunud sind aitama. Spikerda', fill=PAL4, font=('terminal', 10))
sub1260=>subroutine: tahvel.create_text(160, 80, text='nohiku pealt oma töö maha, ilma et ', fill=PAL4, font=('terminal', 10))
sub1262=>subroutine: tahvel.create_text(160, 90, text='õpetaja sind spikerdamas avastaks.', fill=PAL4, font=('terminal', 10))
sub1264=>subroutine: tahvel.create_text(160, 130, text='WASD liigutab mängijat', fill=PAL1, font=('terminal', 10))
sub1266=>subroutine: tahvel.create_text(160, 140, text='Space spikerdab', fill=PAL1, font=('terminal', 10))
sub1268=>subroutine: tahvel.create_text(160, 150, text='3 - esitab töö (olenemata asukohast)', fill=PAL1, font=('terminal', 10))
sub1270=>subroutine: tahvel.create_text(160, 160, text='ENTER - mäng pausil', fill=PAL1, font=('terminal', 10))
sub1272=>subroutine: tahvel.create_text(160, 170, text='ESC - Välju mängust', fill=PAL1, font=('terminal', 10))
sub1274=>subroutine: tahvel.create_text(160, 200, text='Vajuta ENTER et alustada', fill=PAL4, font=('terminal', 10))
sub1276=>subroutine: tahvel.create_text(160, 210, text='või X et salvestatud mängu jätkata', fill=PAL4, font=('terminal', 10))
sub1278=>subroutine: screenupdate()
op1280=>operation: global nooption
op1282=>operation: nooption = 0
cond1285=>condition: while (nooption < 1)
cond1346=>condition: if keyboard.is_pressed('enter')
cond1351=>condition: if (saveprogress == 0)
op1355=>operation: nooption = 1
e1358=>end: end function return
cond1364=>condition: if (saveprogress == 1)
sub1368=>subroutine: initialiseroom1()
sub1370=>subroutine: screenupdate()
op1372=>operation: nooption = 1
e1375=>end: end function return
e1383=>end: end function return
cond1389=>operation: quit() if  keyboard.is_pressed('esc')
sub1402=>subroutine: time.sleep(0.001)
e1404=>end: end instructions
st1408=>start: start graphics_bgcolor
io1410=>inputoutput: input: a, b
sub1413=>subroutine: tahvel.create_rectangle(0, 0, 320, 240, fill=a, outline=b)
e1415=>end: end graphics_bgcolor
st1419=>start: start graphics_carpet
io1421=>inputoutput: input: a, b
op1424=>operation: global playercontainer
op1426=>operation: playercontainer = tahvel.create_rectangle(8, 8, 232, 232, fill=a, outline=b)
e1428=>end: end graphics_carpet
st1432=>start: start graphics_leftwall_windows
io1434=>inputoutput: input: a, b
sub1437=>subroutine: tahvel.create_rectangle(0, 32, 8, 64, fill=a, outline=b)
sub1439=>subroutine: tahvel.create_rectangle(0, 96, 8, 128, fill=a, outline=b)
sub1441=>subroutine: tahvel.create_rectangle(0, 160, 8, 196, fill=a, outline=b)
e1443=>end: end graphics_leftwall_windows
st1447=>start: start graphics_rightwall_exitdoor
io1449=>inputoutput: input: a, b
sub1452=>subroutine: tahvel.create_rectangle(232, 32, 240, 64, fill=a, outline=b)
e1454=>end: end graphics_rightwall_exitdoor
st1458=>start: start graphics_rightwall_exitdoorlow
io1460=>inputoutput: input: a, b
sub1463=>subroutine: tahvel.create_rectangle(232, 200, 240, 232, fill=a, outline=b)
e1465=>end: end graphics_rightwall_exitdoorlow
st1469=>start: start graphics_teacherdesk_leftwall
io1471=>inputoutput: input: a, b
op1474=>operation: global Tdesk
op1476=>operation: Tdesk = tahvel.create_rectangle(16, 32, 80, 56, fill=a, outline=b)
e1478=>end: end graphics_teacherdesk_leftwall
st1482=>start: start graphics_teacherdesk_centerroom
io1484=>inputoutput: input: a, b
op1487=>operation: global Tdesk
op1489=>operation: Tdesk = tahvel.create_rectangle(80, 32, 144, 56, fill=a, outline=b)
e1491=>end: end graphics_teacherdesk_centerroom
st1495=>start: start graphics_studentdesklayout_2person
io1497=>inputoutput: input: a, b
op1500=>operation: global Sdesk1
op1502=>operation: Sdesk1 = tahvel.create_rectangle(16, 64, 72, 88, fill=a, outline=b)
op1504=>operation: global Sdesk2
op1506=>operation: Sdesk2 = tahvel.create_rectangle(16, 112, 72, 136, fill=a, outline=b)
op1508=>operation: global Sdesk3
op1510=>operation: Sdesk3 = tahvel.create_rectangle(16, 160, 72, 184, fill=a, outline=b)
op1512=>operation: global Sdesk4
op1514=>operation: Sdesk4 = tahvel.create_rectangle(96, 64, 152, 88, fill=a, outline=b)
op1516=>operation: global Sdesk5
op1518=>operation: Sdesk5 = tahvel.create_rectangle(96, 112, 152, 136, fill=a, outline=b)
op1520=>operation: global Sdesk6
op1522=>operation: Sdesk6 = tahvel.create_rectangle(96, 160, 152, 184, fill=a, outline=b)
op1524=>operation: global Sdesk7
op1526=>operation: Sdesk7 = tahvel.create_rectangle(176, 64, 232, 88, fill=a, outline=b)
op1528=>operation: global Sdesk8
op1530=>operation: Sdesk8 = tahvel.create_rectangle(176, 112, 232, 136, fill=a, outline=b)
op1532=>operation: global Sdesk9
op1534=>operation: Sdesk9 = tahvel.create_rectangle(176, 160, 232, 184, fill=a, outline=b)
e1536=>end: end graphics_studentdesklayout_2person
st1540=>start: start graphics_studentdesklayout_3column
io1542=>inputoutput: input: a, b
op1545=>operation: global Sdesk1
op1547=>operation: Sdesk1 = tahvel.create_rectangle(16, 64, 44, 208, fill=a, outline=b)
op1549=>operation: global Sdesk2
op1551=>operation: Sdesk2 = tahvel.create_rectangle(96, 64, 152, 184, fill=a, outline=b)
op1553=>operation: global Sdesk3
op1555=>operation: Sdesk3 = tahvel.create_rectangle(204, 64, 232, 208, fill=a, outline=b)
op1557=>operation: global Sdesk4
op1559=>operation: Sdesk4 = tahvel.create_rectangle((- 16), (- 16), (- 32), (- 32), fill=a, outline=b)
op1561=>operation: global Sdesk5
op1563=>operation: Sdesk5 = tahvel.create_rectangle((- 16), (- 16), (- 32), (- 32), fill=a, outline=b)
op1565=>operation: global Sdesk6
op1567=>operation: Sdesk6 = tahvel.create_rectangle((- 16), (- 16), (- 32), (- 32), fill=a, outline=b)
op1569=>operation: global Sdesk7
op1571=>operation: Sdesk7 = tahvel.create_rectangle((- 16), (- 16), (- 32), (- 32), fill=a, outline=b)
op1573=>operation: global Sdesk8
op1575=>operation: Sdesk8 = tahvel.create_rectangle((- 16), (- 16), (- 32), (- 32), fill=a, outline=b)
op1577=>operation: global Sdesk9
op1579=>operation: Sdesk9 = tahvel.create_rectangle((- 16), (- 16), (- 32), (- 32), fill=a, outline=b)
e1581=>end: end graphics_studentdesklayout_3column
st1585=>start: start graphics_studentdesklayout_square
io1587=>inputoutput: input: a, b
op1590=>operation: global Sdesk1
op1592=>operation: Sdesk1 = tahvel.create_rectangle(16, 64, 72, 112, fill=a, outline=b)
op1594=>operation: global Sdesk2
op1596=>operation: Sdesk2 = tahvel.create_rectangle(96, 112, 152, 160, fill=a, outline=b)
op1598=>operation: global Sdesk3
op1600=>operation: Sdesk3 = tahvel.create_rectangle(176, 64, 232, 112, fill=a, outline=b)
op1602=>operation: global Sdesk4
op1604=>operation: Sdesk4 = tahvel.create_rectangle(16, 160, 72, 208, fill=a, outline=b)
op1606=>operation: global Sdesk5
op1608=>operation: Sdesk5 = tahvel.create_rectangle(176, 160, 232, 208, fill=a, outline=b)
op1610=>operation: global Sdesk6
op1612=>operation: Sdesk6 = tahvel.create_rectangle((- 16), (- 16), (- 32), (- 32), fill=a, outline=b)
op1614=>operation: global Sdesk7
op1616=>operation: Sdesk7 = tahvel.create_rectangle((- 16), (- 16), (- 32), (- 32), fill=a, outline=b)
op1618=>operation: global Sdesk8
op1620=>operation: Sdesk8 = tahvel.create_rectangle((- 16), (- 16), (- 32), (- 32), fill=a, outline=b)
op1622=>operation: global Sdesk9
op1624=>operation: Sdesk9 = tahvel.create_rectangle((- 16), (- 16), (- 32), (- 32), fill=a, outline=b)
e1626=>end: end graphics_studentdesklayout_square
st1630=>start: start graphics_studentlayout_2person
io1632=>inputoutput: input: a, b
sub1635=>subroutine: tahvel.create_oval(24, 80, 40, 96, fill=a, outline=b)
sub1637=>subroutine: tahvel.create_oval(48, 84, 64, 100, fill=a, outline=b)
sub1639=>subroutine: tahvel.create_oval(24, 130, 40, 146, fill=a, outline=b)
sub1641=>subroutine: tahvel.create_oval(48, 128, 64, 144, fill=a, outline=b)
sub1643=>subroutine: tahvel.create_oval(24, 180, 40, 196, fill=a, outline=b)
sub1645=>subroutine: tahvel.create_oval(50, 180, 66, 196, fill=a, outline=b)
sub1647=>subroutine: tahvel.create_oval(104, 80, 120, 96, fill=a, outline=b)
sub1649=>subroutine: tahvel.create_oval(128, 84, 144, 100, fill=a, outline=b)
sub1651=>subroutine: tahvel.create_oval(104, 130, 120, 146, fill=a, outline=b)
sub1653=>subroutine: tahvel.create_oval(128, 128, 144, 144, fill=a, outline=b)
sub1655=>subroutine: tahvel.create_oval(130, 180, 146, 196, fill=a, outline=b)
sub1657=>subroutine: tahvel.create_oval(184, 80, 200, 96, fill=a, outline=b)
sub1659=>subroutine: tahvel.create_oval(208, 84, 224, 100, fill=a, outline=b)
sub1661=>subroutine: tahvel.create_oval(184, 130, 200, 146, fill=a, outline=b)
sub1663=>subroutine: tahvel.create_oval(208, 128, 224, 144, fill=a, outline=b)
sub1665=>subroutine: tahvel.create_oval(184, 180, 200, 196, fill=a, outline=b)
e1667=>end: end graphics_studentlayout_2person
st1671=>start: start graphics_studentlayout_3column
io1673=>inputoutput: input: a, b
sub1676=>subroutine: tahvel.create_oval(46, 64, 62, 80, fill=a, outline=b)
sub1678=>subroutine: tahvel.create_oval(48, 84, 64, 100, fill=a, outline=b)
sub1680=>subroutine: tahvel.create_oval(43, 104, 59, 120, fill=a, outline=b)
sub1682=>subroutine: tahvel.create_oval(44, 128, 60, 144, fill=a, outline=b)
sub1684=>subroutine: tahvel.create_oval(44, 180, 60, 196, fill=a, outline=b)
sub1686=>subroutine: tahvel.create_oval(74, 64, 90, 80, fill=a, outline=b)
sub1688=>subroutine: tahvel.create_oval(80, 86, 96, 102, fill=a, outline=b)
sub1690=>subroutine: tahvel.create_oval(78, 108, 94, 124, fill=a, outline=b)
sub1692=>subroutine: tahvel.create_oval(74, 128, 90, 144, fill=a, outline=b)
sub1694=>subroutine: tahvel.create_oval(80, 150, 96, 166, fill=a, outline=b)
sub1696=>subroutine: tahvel.create_oval(78, 172, 94, 188, fill=a, outline=b)
sub1698=>subroutine: tahvel.create_oval(106, 184, 122, 200, fill=a, outline=b)
sub1700=>subroutine: tahvel.create_oval(148, 70, 164, 86, fill=a, outline=b)
sub1702=>subroutine: tahvel.create_oval(150, 88, 166, 104, fill=a, outline=b)
sub1704=>subroutine: tahvel.create_oval(154, 108, 170, 124, fill=a, outline=b)
sub1706=>subroutine: tahvel.create_oval(148, 128, 164, 144, fill=a, outline=b)
sub1708=>subroutine: tahvel.create_oval(154, 150, 170, 166, fill=a, outline=b)
sub1710=>subroutine: tahvel.create_oval(152, 172, 168, 188, fill=a, outline=b)
sub1712=>subroutine: tahvel.create_oval(184, 80, 200, 96, fill=a, outline=b)
sub1714=>subroutine: tahvel.create_oval(188, 104, 204, 120, fill=a, outline=b)
sub1716=>subroutine: tahvel.create_oval(184, 130, 200, 146, fill=a, outline=b)
sub1718=>subroutine: tahvel.create_oval(192, 150, 208, 166, fill=a, outline=b)
sub1720=>subroutine: tahvel.create_oval(184, 180, 200, 196, fill=a, outline=b)
e1722=>end: end graphics_studentlayout_3column
st1726=>start: start graphics_studentlayout_square
io1728=>inputoutput: input: a, b
sub1731=>subroutine: tahvel.create_oval(24, 50, 40, 66, fill=a, outline=b)
sub1733=>subroutine: tahvel.create_oval(68, 84, 84, 100, fill=a, outline=b)
sub1735=>subroutine: tahvel.create_oval(24, 111, 40, 127, fill=a, outline=b)
sub1737=>subroutine: tahvel.create_oval(48, 109, 64, 125, fill=a, outline=b)
sub1739=>subroutine: tahvel.create_oval(24, 207, 40, 223, fill=a, outline=b)
sub1741=>subroutine: tahvel.create_oval(50, 143, 66, 159, fill=a, outline=b)
sub1743=>subroutine: tahvel.create_oval(104, 96, 120, 112, fill=a, outline=b)
sub1745=>subroutine: tahvel.create_oval(160, 100, 176, 116, fill=a, outline=b)
sub1747=>subroutine: tahvel.create_oval(104, 162, 120, 178, fill=a, outline=b)
sub1749=>subroutine: tahvel.create_oval(128, 160, 144, 176, fill=a, outline=b)
sub1751=>subroutine: tahvel.create_oval(184, 45, 200, 61, fill=a, outline=b)
sub1753=>subroutine: tahvel.create_oval(208, 49, 224, 65, fill=a, outline=b)
sub1755=>subroutine: tahvel.create_oval(184, 146, 200, 162, fill=a, outline=b)
sub1757=>subroutine: tahvel.create_oval(208, 112, 224, 128, fill=a, outline=b)
sub1759=>subroutine: tahvel.create_oval(184, 207, 200, 223, fill=a, outline=b)
sub1761=>subroutine: tahvel.create_oval(208, 207, 224, 223, fill=a, outline=b)
e1763=>end: end graphics_studentlayout_square
st1767=>start: start graphics_studentlayout_2person_nerd_pos1
io1769=>inputoutput: input: a, b
op1772=>operation: global nerdbox
op1774=>operation: nerdbox = tahvel.create_oval(130, 180, 146, 196, fill=a, outline=b)
e1776=>end: end graphics_studentlayout_2person_nerd_pos1
st1780=>start: start graphics_studentlayout_3column_nerd_pos1
io1782=>inputoutput: input: a, b
op1785=>operation: global nerdbox
op1787=>operation: nerdbox = tahvel.create_oval(148, 70, 164, 86, fill=a, outline=b)
e1789=>end: end graphics_studentlayout_3column_nerd_pos1
st1793=>start: start graphics_studentlayout_square_nerd_pos1
io1795=>inputoutput: input: a, b
op1798=>operation: global nerdbox
op1800=>operation: nerdbox = tahvel.create_oval(129, 97, 145, 113, fill=a, outline=b)
e1802=>end: end graphics_studentlayout_square_nerd_pos1
st1806=>start: start graphics_studentlayout_2person_nerd_pos2
io1808=>inputoutput: input: a, b
op1811=>operation: global nerdbox
op1813=>operation: nerdbox = tahvel.create_oval(24, 80, 40, 96, fill=a, outline=b)
e1815=>end: end graphics_studentlayout_2person_nerd_pos2
st1819=>start: start graphics_studentlayout_square_nerd_pos2
io1821=>inputoutput: input: a, b
op1824=>operation: global nerdbox
op1826=>operation: nerdbox = tahvel.create_oval(208, 144, 224, 160, fill=a, outline=b)
e1828=>end: end graphics_studentlayout_square_nerd_pos2
st1832=>start: start graphics_studentlayout_3column_nerd_pos2
io1834=>inputoutput: input: a, b
op1837=>operation: global nerdbox
op1839=>operation: nerdbox = tahvel.create_oval(129, 186, 145, 202, fill=a, outline=b)
e1841=>end: end graphics_studentlayout_3column_nerd_pos2
st1845=>start: start graphics_studentlayout_square_nerd_pos3
io1847=>inputoutput: input: a, b
op1850=>operation: global nerdbox
op1852=>operation: nerdbox = tahvel.create_oval(49, 210, 65, 226, fill=a, outline=b)
e1854=>end: end graphics_studentlayout_square_nerd_pos3
st1858=>start: start graphics_studentlayout_3column_nerd_pos3
io1860=>inputoutput: input: a, b
op1863=>operation: global nerdbox
op1865=>operation: nerdbox = tahvel.create_oval(80, 150, 96, 166, fill=a, outline=b)
e1867=>end: end graphics_studentlayout_3column_nerd_pos3
st1871=>start: start graphics_studentlayout_2person_nerd_pos3
io1873=>inputoutput: input: a, b
op1876=>operation: global nerdbox
op1878=>operation: nerdbox = tahvel.create_oval(128, 132, 144, 148, fill=a, outline=b)
e1880=>end: end graphics_studentlayout_2person_nerd_pos3
st1884=>start: start screenupdate
io1886=>inputoutput: input: 
sub1889=>subroutine: tahvel.pack()
sub1891=>subroutine: raam.update()
e1893=>end: end screenupdate
st1897=>start: start drawhud
io1899=>inputoutput: input: 
sub1902=>subroutine: tahvel.create_rectangle(240, 0, 320, 240, fill=PAL7, outline=PAL7)
op1904=>operation: global AOECHECK
op1906=>operation: AOECHECK = tahvel.create_rectangle(248, 8, 256, 16, fill=PAL4, outline=PAL1)
op1908=>operation: global TESTGRAPHIC
op1910=>operation: TESTGRAPHIC = tahvel.create_polygon(256, 64, 256, 128, 304, 128, 304, 72, 296, 64, 296, 72, 304, 72, 296, 64, fill=PAL8, outline=PAL1)
op1912=>operation: global enumerativeline1
op1914=>operation: enumerativeline1 = tahvel.create_line(264, 80, 264, 80, fill=PAL1, width=1)
op1916=>operation: global enumerativeline2
op1918=>operation: enumerativeline2 = tahvel.create_line(264, 88, 264, 88, fill=PAL1, width=1)
op1920=>operation: global enumerativeline3
op1922=>operation: enumerativeline3 = tahvel.create_line(264, 96, 264, 96, fill=PAL1, width=1)
op1924=>operation: global enumerativeline4
op1926=>operation: enumerativeline4 = tahvel.create_line(264, 104, 264, 104, fill=PAL1, width=1)
op1928=>operation: global enumerativeline5
op1930=>operation: enumerativeline5 = tahvel.create_line(264, 112, 264, 112, fill=PAL1, width=1)
op1932=>operation: global pausegraphic
op1934=>operation: global pausetext
op1936=>operation: pausegraphic = tahvel.create_rectangle(248, 208, 312, 232, fill=PAL7, outline=PAL7)
op1938=>operation: pausetext = tahvel.create_text(280, 220, text='Pause ', fill=PAL7, font=('terminal', 10))
op1940=>operation: global leveltext
op1942=>operation: global leveltextcomplete
op1944=>operation: leveltext = tahvel.create_text(280, 140, text=(str(saveprogress) + '. Töö '), fill=PAL1, font=('terminal', 10))
op1946=>operation: leveltextcomplete = tahvel.create_text(280, 152, text='Tehtud!', fill=PAL7, font=('terminal', 10))
e1948=>end: end drawhud
st1952=>start: start hudtest
io1954=>inputoutput: input: a
sub1957=>subroutine: tahvel.itemconfig(AOECHECK, fill=a)
sub1959=>subroutine: tahvel.itemconfig(TESTGRAPHIC, fill=a)
op1961=>operation: global hudtestcompletionlines
op1963=>operation: global leveltextcomplete
cond1966=>condition: if (testcompletion < 33)
op1970=>operation: hudtestcompletionlines[0] = (264 + testcompletion)
sub2055=>subroutine: tahvel.coords(enumerativeline1, 264, 80, hudtestcompletionlines[0], 80)
sub2057=>subroutine: tahvel.coords(enumerativeline2, 264, 88, hudtestcompletionlines[1], 88)
sub2059=>subroutine: tahvel.coords(enumerativeline3, 264, 96, hudtestcompletionlines[2], 96)
sub2061=>subroutine: tahvel.coords(enumerativeline4, 264, 104, hudtestcompletionlines[3], 104)
sub2063=>subroutine: tahvel.coords(enumerativeline5, 264, 112, hudtestcompletionlines[4], 112)
e2065=>end: end hudtest
st2069=>start: start drawplayer
io2071=>inputoutput: input: 
op2074=>operation: global playergraphic
op2076=>operation: playergraphic = tahvel.create_oval((startX + playerX), (startY + playerY), ((startX + 16) + playerX), ((startY + 16) + playerY), fill=PAL5, outline=PAL1)
e2078=>end: end drawplayer
st2082=>start: start initialiseroom1
io2084=>inputoutput: input: 
op2087=>operation: global startX
op2089=>operation: global startY
op2091=>operation: startX = 104
op2093=>operation: startY = 188
sub2095=>subroutine: drawroom_peterson()
sub2097=>subroutine: drawhud()
sub2099=>subroutine: drawplayer()
e2101=>end: end initialiseroom1
st2105=>start: start initialiseroom2
io2107=>inputoutput: input: 
op2110=>operation: global startX
op2112=>operation: global startY
op2114=>operation: startX = 47
op2116=>operation: startY = 152
sub2118=>subroutine: drawroom_class2()
sub2120=>subroutine: drawhud()
sub2122=>subroutine: drawplayer()
e2124=>end: end initialiseroom2
st2128=>start: start initialiseroom3
io2130=>inputoutput: input: 
op2133=>operation: global startX
op2135=>operation: global startY
op2137=>operation: startX = 36
op2139=>operation: startY = 208
sub2141=>subroutine: drawroom_class3()
sub2143=>subroutine: drawhud()
sub2145=>subroutine: drawplayer()
e2147=>end: end initialiseroom3
st2151=>start: start initialiseroom4
io2153=>inputoutput: input: 
op2156=>operation: global startX
op2158=>operation: global startY
op2160=>operation: startX = 208
op2162=>operation: startY = 180
sub2164=>subroutine: drawroom_class4()
sub2166=>subroutine: drawhud()
sub2168=>subroutine: drawplayer()
e2170=>end: end initialiseroom4
st2174=>start: start initialiseroom5
io2176=>inputoutput: input: 
op2179=>operation: global startX
op2181=>operation: global startY
op2183=>operation: startX = 48
op2185=>operation: startY = 48
sub2187=>subroutine: drawroom_class5()
sub2189=>subroutine: drawhud()
sub2191=>subroutine: drawplayer()
e2193=>end: end initialiseroom5
st2197=>start: start initialiseroom6
io2199=>inputoutput: input: 
op2202=>operation: global startX
op2204=>operation: global startY
op2206=>operation: startX = 47
op2208=>operation: startY = 152
sub2210=>subroutine: drawroom_class6()
sub2212=>subroutine: drawhud()
sub2214=>subroutine: drawplayer()
e2216=>end: end initialiseroom6
st2220=>start: start initialiseroom7
io2222=>inputoutput: input: 
op2225=>operation: global startX
op2227=>operation: global startY
op2229=>operation: startX = 160
op2231=>operation: startY = 69
sub2233=>subroutine: drawroom_class7()
sub2235=>subroutine: drawhud()
sub2237=>subroutine: drawplayer()
e2239=>end: end initialiseroom7
st2243=>start: start initialiseroom8
io2245=>inputoutput: input: 
op2248=>operation: global startX
op2250=>operation: global startY
op2252=>operation: startX = 186
op2254=>operation: startY = 66
sub2256=>subroutine: drawroom_class8()
sub2258=>subroutine: drawhud()
sub2260=>subroutine: drawplayer()
e2262=>end: end initialiseroom8
st2266=>start: start initialiseroom9
io2268=>inputoutput: input: 
op2271=>operation: global startX
op2273=>operation: global startY
op2275=>operation: startX = 46
op2277=>operation: startY = 63
sub2279=>subroutine: drawroom_class9()
sub2281=>subroutine: drawhud()
sub2283=>subroutine: drawplayer()
e2285=>end: end initialiseroom9
st2289=>start: start initialiseroom10
io2291=>inputoutput: input: 
op2294=>operation: global startX
op2296=>operation: global startY
op2298=>operation: startX = 103
op2300=>operation: startY = 132
sub2302=>subroutine: drawroom_class10()
sub2304=>subroutine: drawhud()
sub2306=>subroutine: drawplayer()
e2308=>end: end initialiseroom10
st2312=>start: start end1
io2314=>inputoutput: input: 
sub2317=>subroutine: worksheet()
sub2319=>subroutine: tahvel.create_text(160, 24, text='Ending TBD.', fill=PAL1, font=('terminal', 10))
sub2321=>subroutine: tahvel.create_text(160, 56, text='Game Over', fill=PAL1, font=('terminal', 10))
sub2323=>subroutine: tahvel.create_text(160, 72, text='0', fill=PAL1, font=('terminal', 10))
sub2325=>subroutine: tahvel.create_text(160, 88, text='0', fill=PAL1, font=('terminal', 10))
sub2327=>subroutine: tahvel.create_text(160, 104, text='0', fill=PAL1, font=('terminal', 10))
sub2329=>subroutine: tahvel.create_text(160, 120, text='0', fill=PAL1, font=('terminal', 10))
sub2331=>subroutine: tahvel.create_text(160, 136, text='0', fill=PAL1, font=('terminal', 10))
sub2333=>subroutine: tahvel.create_text(160, 152, text='0', fill=PAL1, font=('terminal', 10))
op2335=>operation: global nooption
op2337=>operation: nooption = 0
sub2339=>subroutine: time.sleep(0.2)
cond2342=>condition: while (nooption < 1)
cond2366=>condition: if keyboard.is_pressed('enter')
op2370=>operation: nooption = 1
e2373=>end: end function return
sub2378=>subroutine: screenupdate()
op2380=>operation: nooption = 0
e2385=>end: end end1
st2389=>start: start end2
io2391=>inputoutput: input: 
sub2394=>subroutine: worksheet()
sub2396=>subroutine: tahvel.create_text(160, 24, text='Juhendaja: Kristjan Kivikangur', fill=PAL1, font=('terminal', 10))
sub2398=>subroutine: tahvel.create_text(160, 56, text='Mängu tegid:', fill=PAL1, font=('terminal', 10))
sub2400=>subroutine: tahvel.create_text(160, 72, text='Jüri Vaitmaa ning', fill=PAL1, font=('terminal', 10))
sub2402=>subroutine: tahvel.create_text(160, 88, text='Eva-Kristina Vesiallik', fill=PAL1, font=('terminal', 10))
sub2404=>subroutine: tahvel.create_text(160, 120, text='Kasutatud vahendid:', fill=PAL1, font=('terminal', 10))
sub2406=>subroutine: tahvel.create_text(160, 136, text='Tkinter, Time, Keyboard moodulid.', fill=PAL1, font=('terminal', 10))
sub2408=>subroutine: tahvel.create_text(160, 152, text='Otsingumootor google.', fill=PAL1, font=('terminal', 10))
sub2410=>subroutine: tahvel.create_text(160, 184, text='Põhineb mängul:', fill=PAL1, font=('terminal', 10))
sub2412=>subroutine: tahvel.create_text(160, 200, text='The Classroom (2003, luksy of c404)', fill=PAL1, font=('terminal', 10))
op2414=>operation: global nooption
op2416=>operation: nooption = 0
sub2418=>subroutine: time.sleep(0.2)
cond2421=>condition: while (nooption < 1)
cond2445=>condition: if keyboard.is_pressed('enter')
op2449=>operation: nooption = 1
e2452=>end: end function return
sub2457=>subroutine: screenupdate()
op2459=>operation: nooption = 0
e2464=>end: end end2
st2468=>start: start end3
io2470=>inputoutput: input: 
sub2473=>subroutine: worksheet()
sub2475=>subroutine: tahvel.create_text(160, 24, text='Enter viib tagasi titlescreenile', fill=PAL1, font=('terminal', 10))
sub2477=>subroutine: tahvel.create_text(160, 56, text='X laeb viimase salvestatud mängu', fill=PAL1, font=('terminal', 10))
op2479=>operation: global nooption
op2481=>operation: nooption = 0
cond2484=>condition: while (nooption < 1)
cond2508=>condition: if keyboard.is_pressed('enter')
op2512=>operation: nooption = 1
e2515=>end: end function return
sub2520=>subroutine: screenupdate()
op2522=>operation: nooption = 0
e2527=>end: end end3
st2531=>start: start initialiseending
io2533=>inputoutput: input: 
sub2536=>subroutine: end1()
sub2538=>subroutine: end2()
e2540=>end: end initialiseending
st2544=>start: start Ycheck
io2546=>inputoutput: input: int
op2549=>operation: global playerY
cond2552=>operation: playerY = int if  (playerY != int)
e2562=>end: end Ycheck
st2566=>start: start Xcheck
io2568=>inputoutput: input: int
op2571=>operation: global playerX
cond2574=>operation: playerX = int if  (playerX != int)
e2584=>end: end Xcheck
st2588=>start: start collisionstop
io2590=>inputoutput: input: a, b, c, d
op2593=>operation: global Wcollision
op2595=>operation: Wcollision = a
op2597=>operation: global Acollision
op2599=>operation: Acollision = b
op2601=>operation: global Scollision
op2603=>operation: Scollision = c
op2605=>operation: global Dcollision
op2607=>operation: Dcollision = d
e2609=>end: end collisionstop
st2613=>start: start f_coll
io2615=>inputoutput: input: a, b, c, d, e, f
cond2619=>condition: if (((a - 16) < b < (c - 8)) and ((d - 8) < e < (f - 8)))
sub2623=>subroutine: collisionstop(Wcollision, Acollision, Scollision, 1)
e2660=>end: end f_coll
st2664=>start: start f_coll_aoe
io2666=>inputoutput: input: 
e2670=>end: end function return
cond2628=>condition: if (((a - 16) < b < (c - 2)) and (d < e < f))
sub2632=>subroutine: collisionstop(1, Acollision, Scollision, Dcollision)
cond2637=>condition: if (((a - 16) < b < (c - 8)) and ((d - 16) < e < f))
sub2641=>subroutine: collisionstop(Wcollision, Acollision, 1, Dcollision)
cond2646=>condition: if (((a - 8) < b < c) and ((d - 16) < e < f))
sub2650=>subroutine: collisionstop(Wcollision, 1, Scollision, Dcollision)
sub2654=>subroutine: collisionstop(0, 0, 0, 0)
cond1975=>condition: if (testcompletion < 65)
op1979=>operation: hudtestcompletionlines[1] = (264 + (testcompletion - 32))
op1981=>operation: hudtestcompletionlines[0] = (264 + 32)
cond1986=>condition: if (testcompletion < 97)
op1990=>operation: hudtestcompletionlines[2] = (264 + (testcompletion - 64))
op1992=>operation: hudtestcompletionlines[1] = (264 + 32)
op1994=>operation: hudtestcompletionlines[0] = (264 + 32)
cond1999=>condition: if (testcompletion < 129)
op2003=>operation: hudtestcompletionlines[3] = (264 + (testcompletion - 96))
op2005=>operation: hudtestcompletionlines[2] = (264 + 32)
op2007=>operation: hudtestcompletionlines[1] = (264 + 32)
op2009=>operation: hudtestcompletionlines[0] = (264 + 32)
cond2014=>condition: if (testcompletion < 161)
op2018=>operation: hudtestcompletionlines[4] = (264 + (testcompletion - 128))
op2020=>operation: hudtestcompletionlines[3] = (264 + 32)
op2022=>operation: hudtestcompletionlines[2] = (264 + 32)
op2024=>operation: hudtestcompletionlines[1] = (264 + 32)
op2026=>operation: hudtestcompletionlines[0] = (264 + 32)
cond2031=>condition: if (testcompletion == 160)
op2035=>operation: leveltextcomplete = tahvel.create_text(280, 152, text='Tehtud!', fill=PAL6, font=('terminal', 10))
op2037=>operation: hudtestcompletionlines[4] = (264 + 32)
op2039=>operation: hudtestcompletionlines[3] = (264 + 32)
op2041=>operation: hudtestcompletionlines[2] = (264 + 32)
op2043=>operation: hudtestcompletionlines[1] = (264 + 32)
op2045=>operation: hudtestcompletionlines[0] = (264 + 32)

op2->op4
op4->op6
op6->op8
op8->sub10
sub10->op12
op12->op14
op14->op16
op16->op18
op18->op20
op20->op22
op22->op24
op24->op26
op26->op28
op28->op30
op30->op32
op32->op34
op34->op36
op36->op38
op38->op40
op40->op42
op42->op44
op44->op46
op46->op48
op48->op50
op50->op52
op52->op54
op54->op56
op56->op58
op58->op60
op60->op62
op62->op64
op64->op66
op66->op68
op68->op70
op70->op72
op72->op74
op74->op76
op76->op78
op78->op80
op80->op82
op82->op84
op84->op86
op86->op88
op88->op90
op90->op92
op92->op94
op94->op96
op96->op98
op98->op100
op100->op102
op102->op104
op104->op106
op106->op108
op108->op110
op110->op112
op112->op114
op114->op116
op116->op118
op118->op120
op120->op122
op122->op124
op124->op126
op126->op128
op128->op130
op130->st133
st133->io135
io135->sub138
sub138->op140
op140->sub142
sub142->sub144
sub144->sub146
sub146->e148
e148->st152
st152->io154
io154->op157
op157->op159
op159->op161
op161->op163
op163->op165
op165->op167
op167->op169
op169->op171
op171->e173
e173->st177
st177->io179
io179->sub182
sub182->sub184
sub184->sub186
sub186->sub188
sub188->sub190
sub190->sub192
sub192->sub194
sub194->sub196
sub196->sub198
sub198->sub200
sub200->sub202
sub202->sub204
sub204->sub206
sub206->sub208
sub208->sub210
sub210->sub212
sub212->sub214
sub214->sub216
sub216->sub218
sub218->sub220
sub220->sub222
sub222->sub224
sub224->sub226
sub226->sub228
sub228->sub230
sub230->sub232
sub232->sub234
sub234->sub236
sub236->sub238
sub238->sub240
sub240->sub242
sub242->sub244
sub244->sub246
sub246->sub248
sub248->sub250
sub250->sub252
sub252->sub254
sub254->sub256
sub256->e258
e258->st262
st262->io264
io264->sub267
sub267->sub269
sub269->sub271
sub271->sub273
sub273->sub275
sub275->sub277
sub277->sub279
sub279->op281
op281->op283
op283->sub285
sub285->cond288
cond288(yes)->cond312
cond312(yes)->op316
op316->e319
cond312(no)->sub324
sub324->op326
op326->cond288
cond288(no)->e331
e331->st335
st335->io337
io337->sub340
sub340->sub342
sub342->sub344
sub344->sub346
sub346->sub348
sub348->sub350
sub350->sub352
sub352->sub354
sub354->sub356
sub356->op358
op358->op360
op360->sub362
sub362->cond365
cond365(yes)->cond389
cond389(yes)->op393
op393->e396
cond389(no)->sub401
sub401->op403
op403->cond365
cond365(no)->e408
e408->st412
st412->io414
io414->sub417
sub417->sub419
sub419->sub421
sub421->sub423
sub423->sub425
sub425->sub427
sub427->sub429
sub429->sub431
sub431->sub433
sub433->op435
op435->op437
op437->sub439
sub439->cond442
cond442(yes)->cond466
cond466(yes)->op470
op470->e473
cond466(no)->sub478
sub478->op480
op480->cond442
cond442(no)->e485
e485->st489
st489->io491
io491->sub494
sub494->sub496
sub496->sub498
sub498->sub500
sub500->sub502
sub502->sub504
sub504->sub506
sub506->sub508
sub508->sub510
sub510->op512
op512->op514
op514->sub516
sub516->cond519
cond519(yes)->cond543
cond543(yes)->op547
op547->e550
cond543(no)->sub555
sub555->op557
op557->cond519
cond519(no)->e562
e562->st566
st566->io568
io568->sub571
sub571->sub573
sub573->sub575
sub575->sub577
sub577->sub579
sub579->sub581
sub581->sub583
sub583->sub585
sub585->sub587
sub587->op589
op589->op591
op591->sub593
sub593->cond596
cond596(yes)->cond620
cond620(yes)->op624
op624->e627
cond620(no)->sub632
sub632->op634
op634->cond596
cond596(no)->e639
e639->st643
st643->io645
io645->sub648
sub648->sub650
sub650->sub652
sub652->sub654
sub654->sub656
sub656->sub658
sub658->sub660
sub660->sub662
sub662->sub664
sub664->op666
op666->op668
op668->sub670
sub670->cond673
cond673(yes)->cond697
cond697(yes)->op701
op701->e704
cond697(no)->sub709
sub709->op711
op711->cond673
cond673(no)->e716
e716->st720
st720->io722
io722->sub725
sub725->sub727
sub727->sub729
sub729->sub731
sub731->sub733
sub733->sub735
sub735->sub737
sub737->sub739
sub739->sub741
sub741->op743
op743->op745
op745->sub747
sub747->cond750
cond750(yes)->cond774
cond774(yes)->op778
op778->e781
cond774(no)->sub786
sub786->op788
op788->cond750
cond750(no)->e793
e793->st797
st797->io799
io799->sub802
sub802->sub804
sub804->sub806
sub806->sub808
sub808->sub810
sub810->sub812
sub812->sub814
sub814->sub816
sub816->sub818
sub818->op820
op820->op822
op822->sub824
sub824->cond827
cond827(yes)->cond851
cond851(yes)->op855
op855->e858
cond851(no)->sub863
sub863->op865
op865->cond827
cond827(no)->e870
e870->st874
st874->io876
io876->sub879
sub879->sub881
sub881->sub883
sub883->sub885
sub885->sub887
sub887->sub889
sub889->sub891
sub891->sub893
sub893->sub895
sub895->op897
op897->op899
op899->sub901
sub901->cond904
cond904(yes)->cond928
cond928(yes)->op932
op932->e935
cond928(no)->sub940
sub940->op942
op942->cond904
cond904(no)->e947
e947->st951
st951->io953
io953->sub956
sub956->sub958
sub958->sub960
sub960->sub962
sub962->sub964
sub964->sub966
sub966->sub968
sub968->sub970
sub970->sub972
sub972->op974
op974->op976
op976->sub978
sub978->cond981
cond981(yes)->cond1005
cond1005(yes)->op1009
op1009->e1012
cond1005(no)->sub1017
sub1017->op1019
op1019->cond981
cond981(no)->e1024
e1024->st1028
st1028->io1030
io1030->sub1033
sub1033->sub1035
sub1035->sub1037
sub1037->sub1039
sub1039->sub1041
sub1041->sub1043
sub1043->sub1045
sub1045->sub1047
sub1047->sub1049
sub1049->sub1051
sub1051->sub1053
sub1053->sub1055
sub1055->sub1057
sub1057->sub1059
sub1059->sub1061
sub1061->sub1063
sub1063->op1065
op1065->op1067
op1067->cond1070
cond1070(yes)->cond1155
cond1155(yes)->cond1160
cond1160(yes)->op1164
op1164->e1167
cond1160(no)->cond1173
cond1173(yes)->sub1177
sub1177->sub1179
sub1179->sub1181
sub1181->op1183
op1183->e1186
cond1173(no)->e1194
cond1155(no)->cond1200
cond1200(yes)->sub1204
sub1204->cond1070
cond1200(no)->cond1209
cond1209(yes)->op1213
op1213->sub1215
sub1215->cond1070
cond1209(no)->cond1220
cond1220->cond1070
cond1070(no)->sub1235
sub1235->e1237
e1237->st1241
st1241->io1243
io1243->sub1246
sub1246->sub1248
sub1248->sub1250
sub1250->sub1252
sub1252->sub1254
sub1254->sub1256
sub1256->sub1258
sub1258->sub1260
sub1260->sub1262
sub1262->sub1264
sub1264->sub1266
sub1266->sub1268
sub1268->sub1270
sub1270->sub1272
sub1272->sub1274
sub1274->sub1276
sub1276->sub1278
sub1278->op1280
op1280->op1282
op1282->cond1285
cond1285(yes)->cond1346
cond1346(yes)->cond1351
cond1351(yes)->op1355
op1355->e1358
cond1351(no)->cond1364
cond1364(yes)->sub1368
sub1368->sub1370
sub1370->op1372
op1372->e1375
cond1364(no)->e1383
cond1346(no)->cond1389
cond1389->cond1285
cond1285(no)->sub1402
sub1402->e1404
e1404->st1408
st1408->io1410
io1410->sub1413
sub1413->e1415
e1415->st1419
st1419->io1421
io1421->op1424
op1424->op1426
op1426->e1428
e1428->st1432
st1432->io1434
io1434->sub1437
sub1437->sub1439
sub1439->sub1441
sub1441->e1443
e1443->st1447
st1447->io1449
io1449->sub1452
sub1452->e1454
e1454->st1458
st1458->io1460
io1460->sub1463
sub1463->e1465
e1465->st1469
st1469->io1471
io1471->op1474
op1474->op1476
op1476->e1478
e1478->st1482
st1482->io1484
io1484->op1487
op1487->op1489
op1489->e1491
e1491->st1495
st1495->io1497
io1497->op1500
op1500->op1502
op1502->op1504
op1504->op1506
op1506->op1508
op1508->op1510
op1510->op1512
op1512->op1514
op1514->op1516
op1516->op1518
op1518->op1520
op1520->op1522
op1522->op1524
op1524->op1526
op1526->op1528
op1528->op1530
op1530->op1532
op1532->op1534
op1534->e1536
e1536->st1540
st1540->io1542
io1542->op1545
op1545->op1547
op1547->op1549
op1549->op1551
op1551->op1553
op1553->op1555
op1555->op1557
op1557->op1559
op1559->op1561
op1561->op1563
op1563->op1565
op1565->op1567
op1567->op1569
op1569->op1571
op1571->op1573
op1573->op1575
op1575->op1577
op1577->op1579
op1579->e1581
e1581->st1585
st1585->io1587
io1587->op1590
op1590->op1592
op1592->op1594
op1594->op1596
op1596->op1598
op1598->op1600
op1600->op1602
op1602->op1604
op1604->op1606
op1606->op1608
op1608->op1610
op1610->op1612
op1612->op1614
op1614->op1616
op1616->op1618
op1618->op1620
op1620->op1622
op1622->op1624
op1624->e1626
e1626->st1630
st1630->io1632
io1632->sub1635
sub1635->sub1637
sub1637->sub1639
sub1639->sub1641
sub1641->sub1643
sub1643->sub1645
sub1645->sub1647
sub1647->sub1649
sub1649->sub1651
sub1651->sub1653
sub1653->sub1655
sub1655->sub1657
sub1657->sub1659
sub1659->sub1661
sub1661->sub1663
sub1663->sub1665
sub1665->e1667
e1667->st1671
st1671->io1673
io1673->sub1676
sub1676->sub1678
sub1678->sub1680
sub1680->sub1682
sub1682->sub1684
sub1684->sub1686
sub1686->sub1688
sub1688->sub1690
sub1690->sub1692
sub1692->sub1694
sub1694->sub1696
sub1696->sub1698
sub1698->sub1700
sub1700->sub1702
sub1702->sub1704
sub1704->sub1706
sub1706->sub1708
sub1708->sub1710
sub1710->sub1712
sub1712->sub1714
sub1714->sub1716
sub1716->sub1718
sub1718->sub1720
sub1720->e1722
e1722->st1726
st1726->io1728
io1728->sub1731
sub1731->sub1733
sub1733->sub1735
sub1735->sub1737
sub1737->sub1739
sub1739->sub1741
sub1741->sub1743
sub1743->sub1745
sub1745->sub1747
sub1747->sub1749
sub1749->sub1751
sub1751->sub1753
sub1753->sub1755
sub1755->sub1757
sub1757->sub1759
sub1759->sub1761
sub1761->e1763
e1763->st1767
st1767->io1769
io1769->op1772
op1772->op1774
op1774->e1776
e1776->st1780
st1780->io1782
io1782->op1785
op1785->op1787
op1787->e1789
e1789->st1793
st1793->io1795
io1795->op1798
op1798->op1800
op1800->e1802
e1802->st1806
st1806->io1808
io1808->op1811
op1811->op1813
op1813->e1815
e1815->st1819
st1819->io1821
io1821->op1824
op1824->op1826
op1826->e1828
e1828->st1832
st1832->io1834
io1834->op1837
op1837->op1839
op1839->e1841
e1841->st1845
st1845->io1847
io1847->op1850
op1850->op1852
op1852->e1854
e1854->st1858
st1858->io1860
io1860->op1863
op1863->op1865
op1865->e1867
e1867->st1871
st1871->io1873
io1873->op1876
op1876->op1878
op1878->e1880
e1880->st1884
st1884->io1886
io1886->sub1889
sub1889->sub1891
sub1891->e1893
e1893->st1897
st1897->io1899
io1899->sub1902
sub1902->op1904
op1904->op1906
op1906->op1908
op1908->op1910
op1910->op1912
op1912->op1914
op1914->op1916
op1916->op1918
op1918->op1920
op1920->op1922
op1922->op1924
op1924->op1926
op1926->op1928
op1928->op1930
op1930->op1932
op1932->op1934
op1934->op1936
op1936->op1938
op1938->op1940
op1940->op1942
op1942->op1944
op1944->op1946
op1946->e1948
e1948->st1952
st1952->io1954
io1954->sub1957
sub1957->sub1959
sub1959->op1961
op1961->op1963
op1963->cond1966
cond1966(yes)->op1970
op1970->sub2055
sub2055->sub2057
sub2057->sub2059
sub2059->sub2061
sub2061->sub2063
sub2063->e2065
e2065->st2069
st2069->io2071
io2071->op2074
op2074->op2076
op2076->e2078
e2078->st2082
st2082->io2084
io2084->op2087
op2087->op2089
op2089->op2091
op2091->op2093
op2093->sub2095
sub2095->sub2097
sub2097->sub2099
sub2099->e2101
e2101->st2105
st2105->io2107
io2107->op2110
op2110->op2112
op2112->op2114
op2114->op2116
op2116->sub2118
sub2118->sub2120
sub2120->sub2122
sub2122->e2124
e2124->st2128
st2128->io2130
io2130->op2133
op2133->op2135
op2135->op2137
op2137->op2139
op2139->sub2141
sub2141->sub2143
sub2143->sub2145
sub2145->e2147
e2147->st2151
st2151->io2153
io2153->op2156
op2156->op2158
op2158->op2160
op2160->op2162
op2162->sub2164
sub2164->sub2166
sub2166->sub2168
sub2168->e2170
e2170->st2174
st2174->io2176
io2176->op2179
op2179->op2181
op2181->op2183
op2183->op2185
op2185->sub2187
sub2187->sub2189
sub2189->sub2191
sub2191->e2193
e2193->st2197
st2197->io2199
io2199->op2202
op2202->op2204
op2204->op2206
op2206->op2208
op2208->sub2210
sub2210->sub2212
sub2212->sub2214
sub2214->e2216
e2216->st2220
st2220->io2222
io2222->op2225
op2225->op2227
op2227->op2229
op2229->op2231
op2231->sub2233
sub2233->sub2235
sub2235->sub2237
sub2237->e2239
e2239->st2243
st2243->io2245
io2245->op2248
op2248->op2250
op2250->op2252
op2252->op2254
op2254->sub2256
sub2256->sub2258
sub2258->sub2260
sub2260->e2262
e2262->st2266
st2266->io2268
io2268->op2271
op2271->op2273
op2273->op2275
op2275->op2277
op2277->sub2279
sub2279->sub2281
sub2281->sub2283
sub2283->e2285
e2285->st2289
st2289->io2291
io2291->op2294
op2294->op2296
op2296->op2298
op2298->op2300
op2300->sub2302
sub2302->sub2304
sub2304->sub2306
sub2306->e2308
e2308->st2312
st2312->io2314
io2314->sub2317
sub2317->sub2319
sub2319->sub2321
sub2321->sub2323
sub2323->sub2325
sub2325->sub2327
sub2327->sub2329
sub2329->sub2331
sub2331->sub2333
sub2333->op2335
op2335->op2337
op2337->sub2339
sub2339->cond2342
cond2342(yes)->cond2366
cond2366(yes)->op2370
op2370->e2373
cond2366(no)->sub2378
sub2378->op2380
op2380->cond2342
cond2342(no)->e2385
e2385->st2389
st2389->io2391
io2391->sub2394
sub2394->sub2396
sub2396->sub2398
sub2398->sub2400
sub2400->sub2402
sub2402->sub2404
sub2404->sub2406
sub2406->sub2408
sub2408->sub2410
sub2410->sub2412
sub2412->op2414
op2414->op2416
op2416->sub2418
sub2418->cond2421
cond2421(yes)->cond2445
cond2445(yes)->op2449
op2449->e2452
cond2445(no)->sub2457
sub2457->op2459
op2459->cond2421
cond2421(no)->e2464
e2464->st2468
st2468->io2470
io2470->sub2473
sub2473->sub2475
sub2475->sub2477
sub2477->op2479
op2479->op2481
op2481->cond2484
cond2484(yes)->cond2508
cond2508(yes)->op2512
op2512->e2515
cond2508(no)->sub2520
sub2520->op2522
op2522->cond2484
cond2484(no)->e2527
e2527->st2531
st2531->io2533
io2533->sub2536
sub2536->sub2538
sub2538->e2540
e2540->st2544
st2544->io2546
io2546->op2549
op2549->cond2552
cond2552->e2562
e2562->st2566
st2566->io2568
io2568->op2571
op2571->cond2574
cond2574->e2584
e2584->st2588
st2588->io2590
io2590->op2593
op2593->op2595
op2595->op2597
op2597->op2599
op2599->op2601
op2601->op2603
op2603->op2605
op2605->op2607
op2607->e2609
e2609->st2613
st2613->io2615
io2615->cond2619
cond2619(yes)->sub2623
sub2623->e2660
e2660->st2664
st2664->io2666
io2666->e2670
cond2619(no)->cond2628
cond2628(yes)->sub2632
sub2632->e2660
cond2628(no)->cond2637
cond2637(yes)->sub2641
sub2641->e2660
cond2637(no)->cond2646
cond2646(yes)->sub2650
sub2650->e2660
cond2646(no)->sub2654
sub2654->e2660
cond1966(no)->cond1975
cond1975(yes)->op1979
op1979->op1981
op1981->sub2055
cond1975(no)->cond1986
cond1986(yes)->op1990
op1990->op1992
op1992->op1994
op1994->sub2055
cond1986(no)->cond1999
cond1999(yes)->op2003
op2003->op2005
op2005->op2007
op2007->op2009
op2009->sub2055
cond1999(no)->cond2014
cond2014(yes)->op2018
op2018->op2020
op2020->op2022
op2022->op2024
op2024->op2026
op2026->sub2055
cond2014(no)->cond2031
cond2031(yes)->op2035
op2035->op2037
op2037->op2039
op2039->op2041
op2041->op2043
op2043->op2045
op2045->sub2055
cond2031(no)->sub2055
```