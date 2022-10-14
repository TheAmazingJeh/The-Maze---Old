# █ ░ ╚ ╔ ╩ ╦ ╠ ═ ╬ ║ ╣ ╗ ╝

from os import system, name 
from time import sleep
import msvcrt
import os
import winsound
def detect_press():    # detects when a key is pressed.
    hit = False       
    while hit == False:
        hit = msvcrt.kbhit()
def wait_for(key):     # waits until the specified key is pressed. (string)
    key=key.lower()
    cor = False
    while cor == False:
        hit = False       
        while hit == False:            
            hit = msvcrt.kbhit()
        pressed = msvcrt.getch()
        pressed = str(pressed)
        pressed = pressed.strip("b'")
        pressed = pressed.strip("'")            
        if pressed != key:
            pass        
        else:
            cor = True
def test_for(key):     # returns either True or False if the key pressed is 'key' (string)
    detect_press()
    key=key.lower()
    cor = False
    while cor == False:
        hit = False       
        while hit == False:            
            hit = msvcrt.kbhit()
        pressed = msvcrt.getch()
        pressed = str(pressed)
        pressed = pressed.strip("b'")
        pressed = pressed.strip("'")            
        if pressed != key:
            return False        
        else:
            cor = True
            return True
def what_key():        #
    global keypressed
    detect_press()
    process = msvcrt.getch()
    process = str(process)
    process = process.strip("b'")
    process = process.strip("'")
    keypressed = process
def what_key_return(): #
    global keypressed
    detect_press()
    process = msvcrt.getch()
    process = str(process)
    process = process.strip("b'")
    process = process.strip("'")
    return process

#input(what_key_return())



def start():
    try:
        f = open("gameData.data","r")
        RUNFILE()
    except Exception:
        os.system("color 0c")
        clear()
        print("\n\n  WARNING!!\n  This game contains flashing, and may cause epilepsy to be triggered. If you\n  have epilepsy please do not play this game.\n  Press the TAB key to continue")
        os.system("color 07")
        wait_for("\\t")
        clear()
        print(""" 
     Welcome to ...
      _____ _          _____ _____ _____ _____ 
     |_   _| |_ ___   |     |  _  |__   |   __|
       | | |   | -_|  | | | |     |   __|   __|
       |_| |_|_|___|  |_|_|_|__|__|_____|_____|
    
     If this is your first time playing please put the game                          
     in its own dedicated file as it will create lots of text
     files.
     Press 'y' if you have already done that, or 
     'n' to close the program.
    """)
        q = what_key_return()
        if q == "y":
            with open("gameData.data", "w") as temp:
                pass
            temp.close()
            with open("gameData.data","a+") as file_object:
                file_object.write("07")
            clear()
            buffer()
            createallfiles()
            RUNFILE()
        elif q == "n":
            quit()
        else:
            pass
    
def clear(): ## clears the screen
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')
    
def setcolor(): ## reads gameData.data and set the colour that is in it.
    global color1
    f = open('gameData.data')
    colors = ["07","0f","0c","0e","0a","0b","05","0d"]
    prefline = f.readlines()
    if prefline[0] in colors:
        color1 = "color " + str(prefline[0])
    else:
        color1 = "color 07"
    os.system(color1)
    f.close()
    clear()


######################################################################################################################################################################################
def Tutorial(): ## assigning the Tutorial to lists for future use.
    global tlist    
    t1 =  "╔════════════════════════════════════════════════╗\n"
    t2 =  "║                                                ║\n"
    t3 =  "║  P                                             ║\n"
    t4 =  "║                                                ║\n"
    t5 =  "║                                                ║\n"
    t6 =  "║  ■                                             ║\n"
    t7 =  "║                                                ║\n"
    t8 =  "║                                                ║\n"
    t9 =  "║                                                ║\n"
    t10 = "║                                                ║\n"
    t11 = "║                                                ║\n"
    t12 = "╚════════════════════════════════════════════════╝\n"
    t13 = "\n"
    t14 = "The start point should be marked with a 'P'\n"
    t15 = "The end point should be marked with a '■'\n"
    t15 = "Ice should be marked with a '░'\n"
    t151= "Acid should be marked with a '▒'\n"
    t152= "Breakable walls should be marked with  '└,┌,┐,┘,┴,├,┬,┤,┼,─,│'\n"
    t153= "Portals should be marked with Ø and ø.\n"
    t16 = "\n"
    t17 = "The player will only collide with items from this list\n"
    t18 = "\n"
    t19 = "╚,╔,╗,╝,╩,╠,╦,╣,╬,═,║\n"
    t20 = "\n"
    t21 = "The game area can only be 12 characters tall (the top and bottom line\n"
    t22 = "have to be buffers, ie you can't move on to them)\n"
    t23 = "\n"
    t24 = "However the game area can be as long as you want it to be. (30 wide is\n"
    t25 = "the acceptable maximum)\n"
    t26 = "\n"
    t26 = "new items will be added soon\n"

    tlist = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t151,t152,t153,t16,t17,t18,t19,t20,t21,t22,t23,t24,t25,t26]
Tutorial()
def levels1(): ## assigning the stages of level 1 to lists for future use.
    global l1_1,l1_2,l1_3,l1_4,l1_5

    topbuffer1 =     '╔════════════════════════════════╗\n'
    line01 =         '║                                ║\n'
    line11 =         '║                           ■    ║\n'
    line21 =         '║                                ║\n'
    line31 =         '║     ╔══════════════════════════╝\n'
    line41 =         '║     ║                           \n'
    line51 =         '║     ║  Get to the ■ to beat the \n'
    line61 =         '║     ║    level.                 \n'
    line71 =         '║     ║                           \n'
    line81 =         '║     ║  WASD to move             \n'
    line91 =         '║  P  ║                           \n'
    bottombuffer1 =  '╚═════╝                           \n'    

    l1_1 = [topbuffer1,line01,line11,line21,line31,line41,line51,line61,line71,line81,line91,bottombuffer1]
    
    topbuffer1 =     '╔══════════════╗ ╔═════════════╗\n'
    line01 =         '║              ║ ║             ║\n'
    line11 =         '║   ╔══════╗   ║ ║   ╔═════╗   ║\n'
    line21 =         '║   ║      ║   ╚═╝   ║     ║   ║\n'
    line31 =         '║   ║      ║         ║     ║   ║\n'
    line41 =         '║   ║      ╚═════════╝     ║   ║\n'
    line51 =         '║   ║                      ║   ║\n'
    line61 =         '║   ║                      ║ ■ ║\n'
    line71 =         '║   ║                      ╚═══╝\n'
    line81 =         '║   ║                           \n'
    line91 =         '║ P ║                           \n'
    bottombuffer1 =  '╚═══╝                           \n'

    l1_2 = [topbuffer1,line01,line11,line21,line31,line41,line51,line61,line71,line81,line91,bottombuffer1]
    
    topbuffer1 =     '                                \n'
    line01 =         '                                \n'
    line11 =         '                                \n'
    line21 =         '╔══════════════╗                \n'
    line31 =         '║            ■ ║                \n'
    line41 =         '║   ╔════╦═════╝                \n'
    line51 =         '║   │    ║                      \n'
    line61 =         '║   │    ║                      \n'
    line71 =         '╠═══╬────╣                      \n'
    line81 =         '║   │    ║  Some walls are      \n'
    line91 =         '║ P │    ║    breakable         \n'
    bottombuffer1 =  '╚═══╩════╝                      \n'    
    
    l1_3 = [topbuffer1,line01,line11,line21,line31,line41,line51,line61,line71,line81,line91,bottombuffer1]    

    topbuffer1 =     '╔═══════╦════╦══════════╦══════╗\n'
    line01 =         '║       │    ║          │    ■ ║\n'
    line11 =         '║ ╔═════╝    ╚╗         ║  ╔═══╣\n'
    line21 =         '║ ║           ║    ╔───═╩══╣   ║\n'
    line31 =         '║ ╚════╣      ║   ╔╝       ║   ║\n'
    line41 =         '║      ╠══╗   ╠══╦╝        ╚╗  ║\n'
    line51 =         '║ ╔════╝  ╠═══╝  │          ╚──╣\n'
    line61 =         '║ ║       ║      ║╔══╗         ║\n'
    line71 =         '║ ║       ╠───═══╬╝  ╠═══╦═════╣\n'
    line81 =         '║ ╚═───═══╝      ╚══╦╝   │     ║\n'
    line91 =         '║ P                 │    ╚╗    ║\n'
    bottombuffer1 =  '╚═══════════════════╩═════╩════╝\n'

    l1_4 = [topbuffer1,line01,line11,line21,line31,line41,line51,line61,line71,line81,line91,bottombuffer1]

    topbuffer1 =     '╔═══════════════╦═════════════╗\n'
    line01 =         '║               │             ║\n'
    line11 =         '║   ╔═══════╦═══╩═════───═╗   ║\n'
    line21 =         '║   ║       │             ║   ║\n'
    line31 =         '╠───╣   ╔═══╩═╦═══════╗   ║   ║\n'
    line41 =         '║   ║   ║     │     ■ ╠───╣   ║\n'
    line51 =         '║   ║   ║   ╔═╩═══════╣   ╠───╣\n'
    line61 =         '║   ║   ║   ╚═════════╝   ║   ║\n'
    line71 =         '║   ║   ║                 ║   ║\n'
    line81 =         '║   ║   ╚══════════════╦══╝   ║\n'
    line91 =         '║ P ║                  │      ║\n'
    bottombuffer1 =  '╚═══╩══════════════════╩══════╝\n'

    l1_5 = [topbuffer1,line01,line11,line21,line31,line41,line51,line61,line71,line81,line91,bottombuffer1]
levels1()
def levels2(): ## assigning the stages of level 2 to lists for future use.
    global l2_1,l2_2,l2_3,l2_4,l2_5
    
    topbuffer1 =     '╔════▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line01 =         '║    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line11 =         '║      ▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒   ■  ▒▒▒▒▒▒\n'
    line21 =         '║        ▒▒▒▒        ▒▒        ▒▒▒▒\n'
    line31 =         '║                                ▒\n'
    line41 =         '║                                ║\n'
    line51 =         '║                                ║\n'
    line61 =         '║     ╔══════════════════════════╝\n'
    line71 =         '║     ║                           \n'
    line81 =       '''║     ║   Don't touch the acid    \n'''
    line91 =         '║  P  ║     you will die.         \n'
    bottombuffer1 =  '╚═════╝                           \n'
    
    l2_1 = [topbuffer1,line01,line11,line21,line31,line41,line51,line61,line71,line81,line91,bottombuffer1] 
     
    topbuffer1 =     '╔════════════▒▒▒▒▒▒════════════╗\n'
    line01 =         '║            ▒▒▒▒▒▒▒           ║\n'
    line11 =         '║   ╔════──╗▒▒▒▒▒▒▒  ╔────═╗   ║\n'
    line21 =         '║   ║      ║ ▒▒▒▒▒▒▒ ║     ║   ║\n'
    line31 =         '║   ║      ║  ▒▒▒▒▒  ║     ║   ║\n'
    line41 =         '║   ║      ╚═▒▒▒▒▒▒▒▒╝     ║   ║\n'
    line51 =         '║   ║          ▒▒▒▒▒       │   ║\n'
    line61 =         '║   ║           ▒▒         │ ■ ║\n'
    line71 =         '║   ╠════╗              ╔══╩═══╝\n'
    line81 =         '║   ║    ║      ▒▒      ║       \n'
    line91 =         '║ P ║    ╚════▒▒▒▒▒═════╝       \n'
    bottombuffer1 =  '╚═══╝        ▒▒▒▒▒▒▒▒           \n'

    l2_2 = [topbuffer1,line01,line11,line21,line31,line41,line51,line61,line71,line81,line91,bottombuffer1]
    
    topbuffer1 =     '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line01 =         '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line11 =         '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line21 =         '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line31 =         '▒            ■ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line41 =         '▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line51 =         '▒   │       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line61 =         '▒   │       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line71 =         '▒▒▒▒▒▒▒▒────▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line81 =         '▒   │       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line91 =         '▒ P │       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    bottombuffer1 =  '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'    
    
    l2_3 = [topbuffer1,line01,line11,line21,line31,line41,line51,line61,line71,line81,line91,bottombuffer1]    

    topbuffer1 =     '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line01 =         '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line11 =         '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       ▒▒▒▒▒▒▒▒▒\n'
    line21 =         '▒▒▒         ▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒\n'
    line31 =         '▒▒▒ ▒▒▒▒▒▒▒  ▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒\n'
    line41 =         '▒▒▒ ▒▒▒▒▒▒▒▒     ▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒\n'
    line51 =         '▒▒▒     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒\n'
    line61 =         '▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒\n'
    line71 =         '▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒\n'
    line81 =         '▒  P    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ■ ▒▒▒▒▒\n'
    line91 =         '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    bottombuffer1 =  '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n' 

    l2_4 = [topbuffer1,line01,line11,line21,line31,line41,line51,line61,line71,line81,line91,bottombuffer1]

    topbuffer1 =     '╔═══════╦══════╦════╦══════════════╗\n'
    line01 =         '║▒▒▒▒▒▒▒▒      ▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒║\n'
    line11 =         '║▒▒▒▒▒▒▒▒─▒▒▒▒ ▒ ▒▒▒▒▒▒▒▒▒▒     ▒▒▒║\n'
    line21 =         '║▒        ▒▒ ▒─▒       │    ▒▒▒ ▒▒▒║\n'
    line31 =         '║▒ ▒─▒▒▒▒▒▒▒   ▒▒ ▒▒▒▒▒▒▒▒▒ ▒▒▒ ▒─▒║\n'
    line41 =         '║▒ ▒ ▒▒▒▒▒▒▒▒▒▒▒▒─▒▒▒   │ ▒─▒▒▒─▒ ▒║\n'
    line51 =         '║▒ ▒   │      │   ▒▒▒ ▒▒▒ ▒ ▒▒▒   ▒║\n'
    line61 =         '║▒ ▒▒▒▒▒▒▒─▒▒▒▒▒▒▒▒▒▒ ▒▒▒   ▒▒▒▒ ▒▒║\n'
    line71 =         '╠▒ ▒▒▒▒▒▒▒     ▒▒▒▒▒▒─▒▒▒▒▒▒▒▒▒  ▒▒║\n'
    line81 =         '║   ▒▒▒▒▒▒▒▒▒▒─▒▒▒▒▒▒  ■ ▒▒▒▒   ▒▒▒║\n'
    line91 =         '║ P ▒▒▒▒▒▒▒▒▒▒      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒║\n'
    bottombuffer1 =  '╚═══╩════════╩══════╩══════════════╝\n'

    l2_5 = [topbuffer1,line01,line11,line21,line31,line41,line51,line61,line71,line81,line91,bottombuffer1]
levels2()
def levels3(): ## assigning the stages of level 3 to lists for future use.
    global l3_1,l3_2,l3_3,l3_4,l3_5
    
    topbuffer1 =     '╔════════════════════════════════╗\n'
    line01 =         '║                                ║\n'
    line11 =         '║                           ■    ║\n'
    line21 =         '║                                ║\n'
    line31 =         '║     ╔══════════════════════════╝\n'
    line41 =         '║     ║                           \n'
    line51 =         '║     ║  Get to the ■ to beat the \n'
    line61 =         '║     ║    level.                 \n'
    line71 =         '║     ║                           \n'
    line81 =         '║     ║  WASD to move             \n'
    line91 =         '║  P  ║                           \n'
    bottombuffer1 =  '╚═════╝                           \n'
    
    l3_1 = [topbuffer1,line01,line11,line21,line31,line41,line51,line61,line71,line81,line91,bottombuffer1] 
     
    topbuffer1 =     '╔════════════▒▒▒▒▒▒════════════╗\n'
    line01 =         '║            ▒▒▒▒▒▒▒           ║\n'
    line11 =         '║   ╔════──╗▒▒▒▒▒▒▒  ╔────═╗   ║\n'
    line21 =         '║   ║      ║ ▒▒▒▒▒▒▒ ║     ║   ║\n'
    line31 =         '║   ║      ║  ▒▒▒▒▒  ║     ║   ║\n'
    line41 =         '║   ║      ╚═▒▒▒▒▒▒▒▒╝     ║   ║\n'
    line51 =         '║   ║          ▒▒▒▒▒       │   ║\n'
    line61 =         '║   ║           ▒▒         │ ■ ║\n'
    line71 =         '║   ╠════╗              ╔══╩═══╝\n'
    line81 =         '║   ║    ║      ▒▒      ║       \n'
    line91 =         '║ P ║    ╚════▒▒▒▒▒═════╝       \n'
    bottombuffer1 =  '╚═══╝        ▒▒▒▒▒▒▒▒           \n'

    l3_2 = [topbuffer1,line01,line11,line21,line31,line41,line51,line61,line71,line81,line91,bottombuffer1]
    
    topbuffer1 =     '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line01 =         '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line11 =         '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line21 =         '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line31 =         '▒            ■ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line41 =         '▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line51 =         '▒   │       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line61 =         '▒   │       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line71 =         '▒▒▒▒▒▒▒▒────▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line81 =         '▒   │       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line91 =         '▒ P │       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    bottombuffer1 =  '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'    
    
    l3_3 = [topbuffer1,line01,line11,line21,line31,line41,line51,line61,line71,line81,line91,bottombuffer1]    

    topbuffer1 =     '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line01 =         '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line11 =         '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       ▒▒▒▒▒▒▒▒▒\n'
    line21 =         '▒▒▒         ▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒\n'
    line31 =         '▒▒▒ ▒▒▒▒▒▒▒  ▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒\n'
    line41 =         '▒▒▒ ▒▒▒▒▒▒▒▒     ▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒\n'
    line51 =         '▒▒▒     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒\n'
    line61 =         '▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒\n'
    line71 =         '▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒\n'
    line81 =         '▒  P    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ■ ▒▒▒▒▒\n'
    line91 =         '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    bottombuffer1 =  '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n' 

    l3_4 = [topbuffer1,line01,line11,line21,line31,line41,line51,line61,line71,line81,line91,bottombuffer1]

    topbuffer1 =     '╔═══════╦══════╦════╦══════════════╗\n'
    line01 =         '║▒▒▒▒▒▒▒▒      ▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒║\n'
    line11 =         '║▒▒▒▒▒▒▒▒─▒▒▒▒ ▒ ▒▒▒▒▒▒▒▒▒▒     ▒▒▒║\n'
    line21 =         '║▒        ▒▒ ▒─▒       │    ▒▒▒ ▒▒▒║\n'
    line31 =         '║▒ ▒─▒▒▒▒▒▒▒   ▒▒ ▒▒▒▒▒▒▒▒▒ ▒▒▒ ▒─▒║\n'
    line41 =         '║▒ ▒ ▒▒▒▒▒▒▒▒▒▒▒▒─▒▒▒   │ ▒─▒▒▒─▒ ▒║\n'
    line51 =         '║▒ ▒   │      │   ▒▒▒ ▒▒▒ ▒ ▒▒▒   ▒║\n'
    line61 =         '║▒ ▒▒▒▒▒▒▒─▒▒▒▒▒▒▒▒▒▒ ▒▒▒   ▒▒▒▒ ▒▒║\n'
    line71 =         '╠▒ ▒▒▒▒▒▒▒     ▒▒▒▒▒▒─▒▒▒▒▒▒▒▒▒  ▒▒║\n'
    line81 =         '║   ▒▒▒▒▒▒▒▒▒▒─▒▒▒▒▒▒  ■ ▒▒▒▒   ▒▒▒║\n'
    line91 =         '║ P ▒▒▒▒▒▒▒▒▒▒      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒║\n'
    bottombuffer1 =  '╚═══╩════════╩══════╩══════════════╝\n'

    l3_5 = [topbuffer1,line01,line11,line21,line31,line41,line51,line61,line71,line81,line91,bottombuffer1]
levels3()
def levels4(): ## assigning the stages of level 4 to lists for future use.
    global l4_1,l4_2,l4_3,l4_4,l4_5
    
    topbuffer1 =     '╔════════════════════════════════╗\n'
    line01 =         '║                                ║\n'
    line11 =         '║                           ■    ║\n'
    line21 =         '║                                ║\n'
    line31 =         '║     ╔══════════════════════════╝\n'
    line41 =         '║     ║                           \n'
    line51 =         '║     ║  Get to the ■ to beat the \n'
    line61 =         '║     ║    level.                 \n'
    line71 =         '║     ║                           \n'
    line81 =         '║     ║  WASD to move             \n'
    line91 =         '║  P  ║                           \n'
    bottombuffer1 =  '╚═════╝                           \n'
    
    l4_1 = [topbuffer1,line01,line11,line21,line31,line41,line51,line61,line71,line81,line91,bottombuffer1] 
     
    topbuffer1 =     '╔════════════▒▒▒▒▒▒════════════╗\n'
    line01 =         '║            ▒▒▒▒▒▒▒           ║\n'
    line11 =         '║   ╔════──╗▒▒▒▒▒▒▒  ╔────═╗   ║\n'
    line21 =         '║   ║      ║ ▒▒▒▒▒▒▒ ║     ║   ║\n'
    line31 =         '║   ║      ║  ▒▒▒▒▒  ║     ║   ║\n'
    line41 =         '║   ║      ╚═▒▒▒▒▒▒▒▒╝     ║   ║\n'
    line51 =         '║   ║          ▒▒▒▒▒       │   ║\n'
    line61 =         '║   ║           ▒▒         │ ■ ║\n'
    line71 =         '║   ╠════╗              ╔══╩═══╝\n'
    line81 =         '║   ║    ║      ▒▒      ║       \n'
    line91 =         '║ P ║    ╚════▒▒▒▒▒═════╝       \n'
    bottombuffer1 =  '╚═══╝        ▒▒▒▒▒▒▒▒           \n'

    l4_2 = [topbuffer1,line01,line11,line21,line31,line41,line51,line61,line71,line81,line91,bottombuffer1]
    
    topbuffer1 =     '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line01 =         '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line11 =         '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line21 =         '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line31 =         '▒            ■ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line41 =         '▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line51 =         '▒   │       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line61 =         '▒   │       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line71 =         '▒▒▒▒▒▒▒▒────▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line81 =         '▒   │       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line91 =         '▒ P │       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    bottombuffer1 =  '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'    
    
    l4_3 = [topbuffer1,line01,line11,line21,line31,line41,line51,line61,line71,line81,line91,bottombuffer1]    

    topbuffer1 =     '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line01 =         '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    line11 =         '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       ▒▒▒▒▒▒▒▒▒\n'
    line21 =         '▒▒▒         ▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒\n'
    line31 =         '▒▒▒ ▒▒▒▒▒▒▒  ▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒\n'
    line41 =         '▒▒▒ ▒▒▒▒▒▒▒▒     ▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒\n'
    line51 =         '▒▒▒     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒\n'
    line61 =         '▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒\n'
    line71 =         '▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒\n'
    line81 =         '▒  P    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ■ ▒▒▒▒▒\n'
    line91 =         '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n'
    bottombuffer1 =  '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n' 

    l4_4 = [topbuffer1,line01,line11,line21,line31,line41,line51,line61,line71,line81,line91,bottombuffer1]

    topbuffer1 =     '╔═══════╦══════╦════╦══════════════╗\n'
    line01 =         '║▒▒▒▒▒▒▒▒      ▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒║\n'
    line11 =         '║▒▒▒▒▒▒▒▒─▒▒▒▒ ▒ ▒▒▒▒▒▒▒▒▒▒     ▒▒▒║\n'
    line21 =         '║▒        ▒▒ ▒─▒       │    ▒▒▒ ▒▒▒║\n'
    line31 =         '║▒ ▒─▒▒▒▒▒▒▒   ▒▒ ▒▒▒▒▒▒▒▒▒ ▒▒▒ ▒─▒║\n'
    line41 =         '║▒ ▒ ▒▒▒▒▒▒▒▒▒▒▒▒─▒▒▒   │ ▒─▒▒▒─▒ ▒║\n'
    line51 =         '║▒ ▒   │      │   ▒▒▒ ▒▒▒ ▒ ▒▒▒   ▒║\n'
    line61 =         '║▒ ▒▒▒▒▒▒▒─▒▒▒▒▒▒▒▒▒▒ ▒▒▒   ▒▒▒▒ ▒▒║\n'
    line71 =         '╠▒ ▒▒▒▒▒▒▒     ▒▒▒▒▒▒─▒▒▒▒▒▒▒▒▒  ▒▒║\n'
    line81 =         '║   ▒▒▒▒▒▒▒▒▒▒─▒▒▒▒▒▒  ■ ▒▒▒▒   ▒▒▒║\n'
    line91 =         '║ P ▒▒▒▒▒▒▒▒▒▒      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒║\n'
    bottombuffer1 =  '╚═══╩════════╩══════╩══════════════╝\n'

    l4_5 = [topbuffer1,line01,line11,line21,line31,line41,line51,line61,line71,line81,line91,bottombuffer1]
levels4()


def createfile(name,list0): ## Creates a file using the specified list.
    try:
        os.remove(name)
    except Exception:
        pass
    with open(name, "w",encoding="utf-8") as temp:
        pass
    temp.close()
    
    with open(name,"a+",encoding="utf-8") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
        for i in range(0,len(list0)):
            file_object.write(list0[i])

collisionlist = ["╚","╔","╗","╝","╩","╠","╦","╣","╬","═","║"]
breaklist =     ["└","┌","┐","┘","┴","├","┬","┤","┼","─","│"]

######################################################################################################################################################################################
   
def loadlevel(file): ## loads the file specified into the level line lists

    global topbuffer
    global line0
    global line1 
    global line2 
    global line3 
    global line4 
    global line5
    global line6
    global line7 
    global line8 
    global line9 

    global bottombuffer
    txtfile = open(file,'rU',encoding='utf8')
    levellist = []
    for i in txtfile.readlines():
        levellist.append(list(i))
    topbuffer = levellist[0]
    line0 = levellist[1]
    line1 = levellist[2]
    line2 = levellist[3]
    line3 = levellist[4]
    line4 = levellist[5]
    line5 = levellist[6]
    line6 = levellist[7]
    line7 = levellist[8]
    line8 = levellist[9]
    line9 = levellist[10]
    bottombuffer = levellist[11]

def load0(): ## prints a loading bar. --- left to right
    print("\n    LOADING   \n")
    print(" ]░░░░░░░░░░░░[", end="\r")
    sleep(0.1)
    print(" [█░░░░░░░░░░░]", end="\r")
    sleep(0.1)
    print(" ]██░░░░░░░░░░[", end="\r")
    sleep(0.1)
    print(" [███░░░░░░░░░]", end="\r")
    sleep(0.1)
    print(" ]████░░░░░░░░[", end="\r")
    sleep(0.1)
    print(" [█████░░░░░░░]", end="\r")
    sleep(0.1)
    print(" ]██████░░░░░░[", end="\r")
    sleep(0.1)
    print(" [███████░░░░░]", end="\r")
    sleep(0.1)
    print(" ]████████░░░░[", end="\r")
    sleep(0.1)
    print(" [█████████░░░]", end="\r")
    sleep(0.1)
    print(" ]██████████░░[", end="\r")
    sleep(0.1)
    print(" [███████████░]", end="\r")
    sleep(0.1)
    print(" [████████████]", end="\r")
    sleep(0.1)
    print("\n\n   Complete")
    sleep(0.5)
def loadcool():  ## prints a loading bar. --- ricochet from side to side
    print("\n    LOADING   \n")
    for i in range(2):
        print(" ]░░░░░░░░░░░░[", end="\r")
        sleep(0.1)
        print(" [█░░░░░░░░░░█]", end="\r")
        sleep(0.1)
        print(" ]██░░░░░░░░██[", end="\r")
        sleep(0.1)
        print(" [███░░░░░░███]", end="\r")
        sleep(0.1)
        print(" ]████░░░░████[", end="\r")
        sleep(0.1)
        print(" [█████░░█████]", end="\r")
        sleep(0.1)
        print(" ]████████████[", end="\r")
        sleep(0.1)
        print(" [█████░░█████]", end="\r")
        sleep(0.1)
        print(" ]████░░░░████[", end="\r")
        sleep(0.1)
        print(" [███░░░░░░███]", end="\r")
        sleep(0.1)
        print(" ]██░░░░░░░░██[", end="\r")
        sleep(0.1)
        print(" [█░░░░░░░░░░█]", end="\r")
        sleep(0.1)
        print(" ]░░░░░░░░░░░░[", end="\r")
        sleep(0.1)
        print(" [█░░░░░░░░░░█]", end="\r")
        sleep(0.1)
    print(" [█░░░░░░░░░░█]", end="\r")
    sleep(0.1)
    print(" ]░░░░░░░░░░░░[", end="\r")
    sleep(0.1)
    print(" [█░░░░░░░░░░█]", end="\r")
    sleep(0.1)
    print(" ]██░░░░░░░░██[", end="\r")
    sleep(0.1)
    print(" [███░░░░░░███]", end="\r")
    sleep(0.1)
    print(" ]████░░░░████[", end="\r")
    sleep(0.1)
    print(" [█████░░█████]", end="\r")
    sleep(0.1)
    print(" ]████████████[", end="\r")
    print("\n\n   Complete")
    sleep(0.5)
def load(message):  ## prints a loading bar with a message that is specified. --- left to right
    print("\n    LOADING   ")
    print("\n   ",message,"\n") 
    print(" ]░░░░░░░░░░░░[", end="\r")
    sleep(0.1)
    print(" [█░░░░░░░░░░░]", end="\r")
    sleep(0.1)
    print(" ]██░░░░░░░░░░[", end="\r")
    sleep(0.1)
    print(" [███░░░░░░░░░]", end="\r")
    sleep(0.1)
    print(" ]████░░░░░░░░[", end="\r")
    sleep(0.1)
    print(" [█████░░░░░░░]", end="\r")
    sleep(0.1)
    print(" ]██████░░░░░░[", end="\r")
    sleep(0.1)
    print(" [███████░░░░░]", end="\r")
    sleep(0.1)
    print(" ]████████░░░░[", end="\r")
    sleep(0.1)
    print(" [█████████░░░]", end="\r")
    sleep(0.1)
    print(" ]██████████░░[", end="\r")
    sleep(0.1)
    print(" [███████████░]", end="\r")
    sleep(0.1)
    print(" [████████████]", end="\r")
    sleep(0.1)
    print("\n\n   Complete")
    sleep(0.5)
def buffer():  ## prints a spinny line and then a bar that says somthing.
    print()
    for i in range(0,7):
        print(" Loading game... \\", end="\r")
        sleep(0.1)
        print(" Loading game... |", end="\r")
        sleep(0.1)
        print(" Loading game... /", end="\r")
        sleep(0.1)
        print(" Loading game... -", end="\r")
        sleep(0.1)
    clear()
    print()
    for i in range(4):
        print(" Finalising    ", end="\r")
        sleep(0.2)
        print(" Finalising.   ", end="\r")
        sleep(0.2)
        print(" Finalising..  ", end="\r")
        sleep(0.2)
        print(" Finalising... ", end="\r")
        sleep(0.2)
    clear()
    print()
    print("  COMPLETE")
    sleep(0.5)
    
def lbreak(): ## literally a useless linebreak
    print("\n"*20)
def playlevel(lnum,file,loadtext): ## plays the current level
    global levelnum,play,movecount
    clear()
    levelnum = lnum
    loadlevel(file)
    load(loadtext)
    printscreen()
    play = True
    movecount = 0
    while play == True:        
        move()
        movecount += 1
        if play == False:
            break

def printscreen(): ## prints the current game state with extra info
    clear()
    header = f"\n  Level {levelnum}\n"
    printgame(header)
def printgame(header): ## prints current game state
    print("""
    {}
    {}
    {}
    {}
    {}
    {}
    {}
    {}
    {}
    {}
    {}
    {}
    {}
    """.format(header,delist(topbuffer),delist(line0),delist(line1),delist(line2),delist(line3),delist(line4),delist(line5),delist(line6),delist(line7),delist(line8),delist(line9),delist(bottombuffer)))

def delist(ptrlist): ## turns a game line from a list into a string
    ptrstr = ''.join(ptrlist)
    ptrstr = ptrstr.strip("\n")
    ptrstr = ptrstr.strip("?")
    return ptrstr


def searchP(line,Y): ## used in search for player
    global Py,Px,templist,line0,line1,line2,line3,line4,line5,line5,line6,line7,line8,line9
    if "P" in line:
        Py = Y
        Px = line.index("P")
        templist = line
def searchp(): ## search for player
    global Py,Px,templist,line0,line1,line2,line3,line4,line5,line5,line6,line7,line8,line9
    searchP(line0,0)
    searchP(line1,1)
    searchP(line2,2)
    searchP(line3,3)
    searchP(line4,4)
    searchP(line5,5)
    searchP(line6,6)
    searchP(line7,7)
    searchP(line8,8)
    searchP(line9,9)

def mainmenu(): ## main menu
    global levelnum
    clear()
    print(""" 
 Welcome to ...                                    
  _____ _          _____ _____ _____ _____ 
 |_   _| |_ ___   |     |  _  |__   |   __|
   | | |   | -_|  | | | |     |   __|   __|
   |_| |_|_|___|  |_|_|_|__|__|_____|_____|
                                           
 Please select an option to continue:
 
 1) Play campaign
 2) Load custom level
 3) Create game files
 4) User preferences
 ------------------------------------------
 5) Close game                            
""")
    
    c = what_key_return()
    clear()
    if c == "1":
        campaign()
    if c == "2":
        l = input("\n Please enter the name of the game file\n (eg: level_1.txt)\n >>> ")
        clear()
        levelnum = l
        try:
            playlevel("CUSTOM LEVEL",l,"Custom")
            clear()
            mainmenu()
        except Exception as e:
            print("\n An error has occured.\n This is probably because the file name you have entered does not exsist.\n\n Advanced error >>>",e)
            detect_press()
        mainmenu()
            
    if c == "3":
        print("\n This game works better if you put it in a dedicated file.\n One will be created for you, and it can be renamed.\n Press 'y' to continue or any other button to return\n to the main menu")
        l = what_key_return()
        if l == "y":
            pass
        else:
            clear()
            mainmenu()
        try:
            os.mkdir("Put the game in this folder")
        except Exception:
            print(" "*20,"Folder already exsists")
            createallfiles()
        
        loadcool()
        clear()
    if c == "4":
        userpref()
    if c == "5":
        print(" Are you sure that you want to quit?\n You will lose all progress in the game\n (y/n)")
        l = what_key_return()
        if l == "y":
            quit()
        else:
            clear()
            mainmenu()
    else:
        mainmenu()
def userpref(): ## userpref
    print("""
   _____                            ___                             
  |  |  |___ ___ ___    ___ ___ ___|  _|___ ___ ___ ___ ___ ___ ___ 
  |  |  |_ -| -_|  _|  | . |  _| -_|  _| -_|  _| -_|   |  _| -_|_ -|
  |_____|___|___|_|    |  _|_| |___|_| |___|_| |___|_|_|___|___|___|
  .                    |_|                                          
    
 What do you want to do?
 
 1) Change Text colour

 2) Go back to main menu.


""") 
    c = what_key_return()
    clear()
    if c == "1":
        colmenu()
    if c == "2":
        mainmenu()

def colmenu(): ## userpref
    print("""
 Please select a colour

 1) Default ( Medium grey )
 2) Bright white
 3) Red
 4) Yellow
 5) Green
 6) Aqua
 7) Purple
 8) Pink
 
 Press any other key to exit
 
 

""") 
    c = what_key_return()
    clear()
    f = open("gameData.data","w+")
    if c == "1":
        f.write("07")
    elif c == "2":
        f.write("0f")
    elif c == "3":
        f.write("0c")
    elif c == "4":
        f.write("0e")
    elif c == "5":
        f.write("0a")
    elif c == "6":
        f.write("0b")    
    elif c == "7":
        f.write("05")
    elif c == "8":
        f.write("0d")
    else:
        f.write(color1)
    f.close()
    setcolor()
    userpref()

def checkiceupS(num,currentline,reqline):
    global Px,Py,line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,templist,play
    if Py == num:
        currentline.pop(Px)
        currentline.insert(Px," ")
        reqline.pop(Px)
        reqline.insert(Px,"P") 
def checkiceupM(num,currentline,reqline):
    global Px,Py,line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,templist,play,endup
    if Py == num:
        if reqline[Px] == "▒":
            gameover()
        if reqline[Px] == " ":
            endup = True
        currentline.pop(Px)
        currentline.insert(Px,"░")
        reqline.pop(Px)
        reqline.insert(Px,"P") 
def iceup():
    global Px,Py,line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,templist,play,endup
    endup = False
    itra = 0
    while endup == False:
        searchp()
        if itra == 0:
            checkiceupS(0,line0,line0)
            checkiceupS(1,line1,line0)
            checkiceupS(2,line2,line1)
            checkiceupS(3,line3,line2)            
            checkiceupS(4,line4,line3)
            checkiceupS(5,line5,line4)
            checkiceupS(6,line6,line5)            
            checkiceupS(7,line7,line6)            
            checkiceupS(8,line8,line7)
            checkiceupS(9,line9,line8)
        if itra > 0:
            checkiceupM(0,line0,line0)
            checkiceupM(1,line1,line0)
            checkiceupM(2,line2,line1)
            checkiceupM(3,line3,line2)            
            checkiceupM(4,line4,line3)
            checkiceupM(5,line5,line4)
            checkiceupM(6,line6,line5)            
            checkiceupM(7,line7,line6)            
            checkiceupM(8,line8,line7)
            checkiceupM(9,line9,line8)
        itra += 1
        printscreen()
        sleep(0.1)        
def checkup(num,currentline,reqline):   
    global play
    if Py == num:
        if reqline[Px] in collisionlist:
            pass
        elif reqline[Px] == "■":
            play = False
        elif reqline[Px] == "▒":
            gameover()
        elif reqline[Px] == "░":           
            iceup()
        else:
            currentline.pop(Px)
            currentline.insert(Px," ")
            reqline.pop(Px)
            reqline.insert(Px,"P")
def up():
    global Px,Py,line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,play,templist

    checkup(0,line0,line0)
    checkup(1,line1,line0)
    checkup(2,line2,line1)
    checkup(3,line3,line2)
    checkup(4,line4,line3)
    checkup(5,line5,line4)
    checkup(6,line6,line5)
    checkup(7,line7,line6)
    checkup(8,line8,line7)
    checkup(9,line9,line8)    
    printscreen()

def checkicedownS(num,currentline,reqline):
    global Px,Py,line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,templist,play
    if Py == num:
        currentline.pop(Px)
        currentline.insert(Px," ")
        reqline.pop(Px)
        reqline.insert(Px,"P") 
def checkicedownM(num,currentline,reqline):
    global Px,Py,line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,templist,play,enddown
    if Py == num:
        if reqline[Px] == "▒":
            gameover()
        if reqline[Px] == " ":
            enddown = True
        currentline.pop(Px)
        currentline.insert(Px,"░")
        reqline.pop(Px)
        reqline.insert(Px,"P") 
def icedown():
    global Px,Py,line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,templist,play,enddown
    enddown = False
    itra = 0
    while enddown == False:
        searchp()
        if itra == 0:
            checkicedownS(0,line0,line1)
            checkicedownS(1,line1,line2)
            checkicedownS(2,line2,line3)
            checkicedownS(3,line3,line4)            
            checkicedownS(4,line4,line5)
            checkicedownS(5,line5,line6)
            checkicedownS(6,line6,line7)            
            checkicedownS(7,line7,line8)            
            checkicedownS(8,line8,line9)
            checkicedownS(9,line9,line9)
        if itra > 0:
            checkicedownM(0,line0,line1)
            checkicedownM(1,line1,line2)
            checkicedownM(2,line2,line3)
            checkicedownM(3,line3,line4)            
            checkicedownM(4,line4,line5)
            checkicedownM(5,line5,line6)
            checkicedownM(6,line6,line7)            
            checkicedownM(7,line7,line8)            
            checkicedownM(8,line8,line9)
            checkicedownM(9,line9,line9)
        itra += 1
        printscreen()
        sleep(0.1)        
def checkdown(num,currentline,reqline):
    global play
    if Py == num:
        if reqline[Px] in collisionlist:
            pass
        elif reqline[Px] == "■":
            play = False
        elif reqline[Px] == "▒":
            gameover()
        elif reqline[Px] == "░":            
            icedown()
        else:
            currentline.pop(Px)
            currentline.insert(Px," ")
            reqline.pop(Px)
            reqline.insert(Px,"P")
def down():
    global Px,Py,line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,play,templist

    checkdown(9,line9,line9)
    checkdown(8,line8,line9)
    checkdown(7,line7,line8)
    checkdown(6,line6,line7)
    checkdown(5,line5,line6)
    checkdown(4,line4,line5)
    checkdown(3,line3,line4)
    checkdown(2,line2,line3)
    checkdown(1,line1,line2)    
    checkdown(0,line0,line1)
    printscreen()    

def checkiceleftS(num,line):
    global Px,Py,line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,templist,play
    if Py == num:
        line.pop(Px)
        line.insert(Px," ")
        line.pop(Px-1)
        line.insert(Px-1,"P")    
def checkiceleftM(num,line):
    global Px,Py,line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,templist,play
    if Py == num:
        line.pop(Px)
        line.insert(Px,"░")
        line.pop(Px-1)
        line.insert(Px-1,"P")        
def iceleft():
    global Px,Py,line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,templist,play
    itra = 0
    while 1:
        searchp()
        if templist[Px-1] == "▒":
            gameover()
        if itra == 0:
            checkiceleftS(0,line0)
            checkiceleftS(1,line1)
            checkiceleftS(2,line2)
            checkiceleftS(3,line3)
            checkiceleftS(4,line4)
            checkiceleftS(5,line5)
            checkiceleftS(6,line6)
            checkiceleftS(7,line7)
            checkiceleftS(8,line8)
            checkiceleftS(9,line9)

        elif itra >= 0:
            if templist[Px-1] == "░":
                checkiceleftM(0,line0)
                checkiceleftM(1,line1)
                checkiceleftM(2,line2)
                checkiceleftM(3,line3)
                checkiceleftM(4,line4)
                checkiceleftM(5,line5)
                checkiceleftM(6,line6)
                checkiceleftM(7,line7)
                checkiceleftM(8,line8)
                checkiceleftM(9,line9)
            if templist[Px-1] == " ":
                checkiceleftM(0,line0)
                checkiceleftM(1,line1)
                checkiceleftM(2,line2)
                checkiceleftM(3,line3)
                checkiceleftM(4,line4)
                checkiceleftM(5,line5)
                checkiceleftM(6,line6)
                checkiceleftM(7,line7)
                checkiceleftM(8,line8)
                checkiceleftM(9,line9)
                break
        itra += 1
        printscreen()
        sleep(0.1)   
def checkleft(num,line):
    global play
    if Py == num:
        line.pop(Px)
        line.insert(Px," ")
        line.pop(Px-1)
        line.insert(Px-1,"P")       
def left():
    global Px,Py,line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,templist,play
    
    if templist[Px-1] in collisionlist:
        pass
    elif templist[Px-1] == "■":
            play = False
    elif templist[Px-1] == "▒":
            gameover()
    elif templist[Px-1] == "░":
            iceleft()
    else:
        checkleft(0,line0)
        checkleft(1,line1)
        checkleft(2,line2)
        checkleft(3,line3)
        checkleft(4,line4)
        checkleft(5,line5)
        checkleft(6,line6)
        checkleft(7,line7)
        checkleft(8,line8)
        checkleft(9,line9)
        
    printscreen()    

def checkicerightS(num,line):
    global Px,Py,line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,templist,play
    if Py == num:
        line.pop(Px)
        line.insert(Px," ")
        line.pop(Px+1)
        line.insert(Px+1,"P")    
def checkicerightM(num,line):
    global Px,Py,line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,templist,play
    if Py == num:
        line.pop(Px)
        line.insert(Px,"░")
        line.pop(Px+1)
        line.insert(Px+1,"P")        
def iceright():
    global Px,Py,line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,templist,play
    itra = 0
    while 1:
        searchp()
        if templist[Px+1] == "▒":
            gameover()
        if itra == 0:
            checkicerightS(0,line0)
            checkicerightS(1,line1)
            checkicerightS(2,line2)
            checkicerightS(3,line3)
            checkicerightS(4,line4)
            checkicerightS(5,line5)
            checkicerightS(6,line6)
            checkicerightS(7,line7)
            checkicerightS(8,line8)
            checkicerightS(9,line9)

        elif itra >= 0:
            if templist[Px+1] == "░":
                checkicerightM(0,line0)
                checkicerightM(1,line1)
                checkicerightM(2,line2)
                checkicerightM(3,line3)
                checkicerightM(4,line4)
                checkicerightM(5,line5)
                checkicerightM(6,line6)
                checkicerightM(7,line7)
                checkicerightM(8,line8)
                checkicerightM(9,line9)
            if templist[Px+1] == " ":
                checkicerightM(0,line0)
                checkicerightM(1,line1)
                checkicerightM(2,line2)
                checkicerightM(3,line3)
                checkicerightM(4,line4)
                checkicerightM(5,line5)
                checkicerightM(6,line6)
                checkicerightM(7,line7)
                checkicerightM(8,line8)
                checkicerightM(9,line9)
                break
        itra += 1
        printscreen()
        sleep(0.1)    
def checkright(num,line):
    global play
    if Py == num:
        line.pop(Px)
        line.insert(Px," ")
        line.pop(Px+1)
        line.insert(Px+1,"P")    
def right():
    global Px,Py,line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,templist,play
    
    if templist[Px+1] in collisionlist:
        pass
    elif templist[Px+1] == "■":
            play = False
    elif templist[Px+1] == "▒":
            gameover()
    elif templist[Px+1] == "░":
            iceright()   
    else:
        checkright(0,line0)
        checkright(1,line1)
        checkright(2,line2)
        checkright(3,line3)
        checkright(4,line4)
        checkright(5,line5)
        checkright(6,line6)
        checkright(7,line7)
        checkright(8,line8)
        checkright(9,line9)
        
    printscreen()

def move(): ## This function checks where the player should move.
    global Px,Py
    sleep(0.1)
    what_key()
    searchp()
    if keypressed == "w":
        up()
    elif keypressed == "a":
        left()
    elif keypressed == "s":
        down()
    elif keypressed == "d":
        right()
    else:
        pass

def campaign(): ## This function starts the campaign
    global levelnum,play
    clear()
    print("""
 __                _    _____ _____ __    _____ _____ _____ 
|  |   ___ _ _ ___| |  |   __|   __|  |  |   __|     |_   _|
|  |__| -_| | | -_| |  |__   |   __|  |__|   __|   --| | |  
|_____|___|\_/|___|_|  |_____|_____|_____|_____|_____| |_|  
                                              ,.
 1) Level 1 - Basic movement              __.'_
 2) Level 2 - Acidic tests               |__|__|
 3) Level 3 - Thinking with Portals      |     |
 4) Level 4 - Slippery ice               |-___-|
 5) Level 5 - Combined science           '.___.'
 
 ---------------------------------------------------
 6) Return to main menu
    """)
    c = what_key_return()
    if c == "1":
        playlevel("1 - 1",'level_1-1.lv1',"Level 1\n\n    Stage 1")
        playlevel("1 - 2",'level_1-2.lv1',"Level 1\n\n    Stage 2")
        playlevel("1 - 3",'level_1-3.lv1',"Level 1\n\n    Stage 3")
        playlevel("1 - 4",'level_1-4.lv1',"Level 1\n\n    Stage 4")
        playlevel("1 - 5",'level_1-5.lv1',"Level 1\n\n    Stage 5")
        campaign()
    if c == "2":
        playlevel("2 - 1",'level_2-1.lv2',"Level 2\n\n    Stage 1")
        playlevel("2 - 2",'level_2-2.lv2',"Level 2\n\n    Stage 2")
        playlevel("2 - 3",'level_2-3.lv2',"Level 2\n\n    Stage 3")
        playlevel("2 - 4",'level_2-4.lv2',"Level 2\n\n    Stage 4")
        playlevel("2 - 5",'level_2-5.lv2',"Level 2\n\n    Stage 5")
        campaign()
    if c == "6":
        mainmenu()
    else:
        clear()
        campaign()
def gameover(): ## This function plays the game over message and ends the level
    os.system("color 0c")
    clear()
    print("""
                 *             )            (     
 (       (     (  `         ( /(            )\ )  
 )\ )    )\    )\))(  (     )\())(   (  (  (()/(  
(()/( ((((_)( ((_)()\ )\   ((_)\ )\  )\ )\  /(_)) 
 /(_))_)\ _ )\(_()((_|(_)    ((_|(_)((_|(_)(_))   
(_)) __(_)_\(_)  \/  | __|  / _ \ \ / /| __| _ \  
  | (_ |/ _ \ | |\/| | _|  | (_) \ V / | _||   /  
   \___/_/ \_\|_|  |_|___|  \___/ \_/  |___|_|_\  
                                                  
    Press any key to return to level select...
    """)
    winsound.Beep(440, 500)
    winsound.Beep(293, 500)
    winsound.Beep(440, 500)
    winsound.Beep(293, 700)
    detect_press()
    os.system(color1)
    clear()
    campaign()

######################################################################################################################################################################################
def createallfiles():
    createfile("How_to_make_levels.txt",tlist)
    createfile("level_1-1.lv1",l1_1)
    createfile("level_1-2.lv1",l1_2)
    createfile("level_1-3.lv1",l1_3)
    createfile("level_1-4.lv1",l1_4)
    createfile("level_1-5.lv1",l1_5)
    sleep(1)
    createfile("level_2-1.lv2",l2_1)
    createfile("level_2-2.lv2",l2_2)
    createfile("level_2-3.lv2",l2_3)
    createfile("level_2-4.lv2",l2_4)     
    createfile("level_2-5.lv2",l2_5)
def RUNFILE(): ## runs the file, with a special loading screen.
    try:
        setcolor()
        clear()
        mainmenu()
    except Exception as e:
        print("\n Error,",e)
        input()
        mainmenu()  
start()