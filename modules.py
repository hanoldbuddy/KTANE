import time
from pygame.locals import *
import pygame
import numpy as np

def button(facts):
    button_facts = []
    button_facts.append(input("\nColor: "))
    button_facts.append(input("Word: "))
    if 'b' == button_facts[0] and 'a' == button_facts[1]:
        hold()
    elif int(facts[0]) >= 2 and button_facts[1] == "d":
        press_and_release()
    elif button_facts[0] == "w" and facts[1] == "y":
        hold()
    elif int(facts[0]) >= 3 and facts[2] == "y":
        press_and_release()
    elif button_facts[0] == "y":
        hold()
    elif button_facts[0] == "r" and button_facts[1] == "h":
        press_and_release()
    else:
        hold()
    time.sleep(3)

def hold():
    print("\n\nHOLD....\n\nBLUE: 4\nWHITE: 1\nYELLOW: 5\nOTHER: 1")
def press_and_release():
    print("\n\nPRESS & RELEASE")

def wires(facts):
    colors = input('\nInput wire colors seperated by a space.\nr -  RED\nk - BLACK\nb -  BLUE\nw -  WHITE\ny -  YELLOW\n\n')
    color_list = colors.split(' ')
    num_wires = len(color_list)
    if num_wires == 3:
        #check = ['r']
        res = True
        for i in range(0,3):
            if color_list[i] == 'r':
                res = False
                break
        #res = [ele for ele in check if(ele in colors)]
        if res:
            print('\n2ND wire.')
            time.sleep(1.5)
        elif color_list[2] == 'w':
            print(color_list[2])
            print('\nLAST wire.')
            time.sleep(1.5)
        elif colors.count('b') >= 2:
            print('\nLAST BLUE wire.')
            time.sleep(1.5)
        else:
            print('\nLAST wire.')
            time.sleep(1.5)
    elif num_wires == 4:
        test = 0
        if facts[3] == 'n':
            for i in range(0,4):
                if color_list[i] == 'r':
                    test += 1
                    if test >= 2:
                        print('\nLAST RED wire.')
                        time.sleep(1.5)
                        break
        elif color_list[3] == 'y':
            test = 0
            for i in 4:
                if color_list[i] != 'r':
                    test += 1
                if test == 4:
                    print('\n1ST wire.')
                    time.sleep(1.5)
        elif colors.count('b') == 1:
            print('1ST wire.')
            time.sleep(1.5)
        elif colors.count('y') > 1:
            print('LAST wire.')
            time.sleep(1.5)
        else:
            print('2ND wire.')
            time.sleep(1.5)
    elif num_wires == 5:
        if color_list[4] == 'k' and facts[3] == 'n':
            print('4TH wire.')
            time.sleep(1.5)
        elif colors.count('r') == 1 and colors.count('y') > 1:
            print('1ST wire.')
            time.sleep(1.5)
        elif colors.count('k') == 0:
            print('2ND wire.')
            time.sleep(1.5)
        else:
            print('1ST wire.')
            time.sleep(1.5)
    elif num_wires == 6:
        if colors.count('y') == 0 and facts[3] == 'n':
            print('3RD wire.')
            time.sleep(1.5)
        elif colors.count('y') == 1 and colors.count('w') > 1:
            print('4TH wire.')
            time.sleep(1.5)
        elif colors.count('r') == 0:
            print('LAST wire.')
            time.sleep(1.5)
        else:
            print('4TH wire.')
            time.sleep(1.5)

def ss(facts):
    flash = True
    list = []
    if facts[4] == 'y':
        while flash:
            color = input('\n\nInput flashes seperated by a space.\nColor: \nr -  RED\ny - YELLOW\nb -  BLUE\ng -  GREEN\n\n')
            if color == 'n':
                flash = False
            elif color == 'r':
                list.append('Blue')
                print(list)
            elif color == 'y':
                list.append('Green')
                print(list)
            elif color == 'b':
                list.append('Red')
                print(list)
            elif color == 'g':
                list.append('Yellow')
                print(list)
            time.sleep(2)
    if facts[4] == 'n':
        while flash:
            color = input('\n\nInput flashes seperated by a space.\nColor: \nr -  RED\ny - YELLOW\nb -  BLUE\ng -  GREEN\n\n')
            if color == 'n':
                flash = False
            elif color == 'r':
                list.append('Blue')
                print(list)
            elif color == 'y':
                list.append('Red')
                print(list)
            elif color == 'b':
                list.append('Yellow')
                print(list)
            elif color == 'g':
                list.append('Green')
                print(list)
            time.sleep(2)
    
def needy(facts):
    pos = input('Enter first 6 positions with no spaces.\n\n')
    if pos == '010111' or pos == '100111':
        print('\nUP')
        time.sleep(1)
    elif pos == '011111' or pos == '100110':
        print('\nDOWN')
        time.sleep(1)
    elif pos == '010000' or pos == '000000':
        print('\nLEFT')
        time.sleep(1)
    elif pos == '110111':
        print('\nRIGHT')
        time.sleep(1)
    else: 
        print('\nTry Again...\n')

def nwl():
    r, b, k = 0, 0, 0
    red =   ['C','B','A','AC','B','AC','CUT','AB','B']
    blue =  ['B','AC','B','A','B','BC','C','AC','A']
    black = ['CUT','AC','B','AC','B','BC','AB','C','C']
    while True:
        color = input('\n1 - RED\n2 - BLUE\n3 - BLACK\nn - STOP\n\nWire Color: ')
        if color == 'n':
            break
        elif color == '1':
            cut = red[r]
            r += 1
        elif color == '2':
            cut = blue[b]
            b += 1
        elif color == '3':
            cut = black[k]
            k += 1
        if cut == 'A':
            print('ALPHA')
        elif cut == 'B':
            print('BRAVO')
        elif cut == 'C':
            print('CHARLIE')
        elif cut == 'CUT':
            print(cut)
        elif cut == 'AB':
            print('ALPHA-BRAVO')
        elif cut == 'AC':
            print('ALPHA-CHARLIE')
        elif cut == 'BC':
            print('BRAVO-CHARLIE')
        time.sleep(.5)
def led_star_wire(facts):
    while True:
        print('Input details below.\n\n1 = True\n0 = False\n\n  B   S\nR L L T\nE U E A\nD E D R\n')
        det = str(input())
        c = '\nCUT\n'
        d = '\nLEAVE\n'
        if int(facts[0]) >= 2:
            b = '\nCUT'
        else:
            b = '\nLEAVE\n'
        if facts[3] == 'y':
            s = '\nCUT'
        else:
            s = '\nLEAVE\n'
        if facts[5] == 'y':
            p = '\nCUT'
        else:
            p = '\nLEAVE\n'
        if det == '0000' or det == '0001' or det == '1001':
            print(c)
        elif det == '0010' or det == '1111' or det == '0101':
            print(d)
        elif  det == '0011' or det == '1010' or det == '1011':
            print(b)
        elif det == '0100' or det == '1000' or det == '1100' or det == '1110':
            print(s)
        elif det == '0110' or det == '0111' or det == '1101':
            print(p)
        elif det == 'n':
            break
        else:
            print('error...')
        time.sleep(1)

def led_word():
    top_word = [['YES', 'MIDDLE-LEFT'],
                ['FIRST', 'TOP-RIGHT'] ,
                ['DISPLAY', 'BOTTOM-RIGHT'],
                ['OKAY', 'TOP-RIGHT'],
                ['SAYS', 'BOTTOM-RIGHT'],
                ['NOTHING','MIDDLE-LEFT'],
                ['       ', 'BOTTOM-LEFT'],
                ['BLANK', 'MIDDLE-RIGHT'],
                ['NO', 'BOTTOM-RIGHT'],
                ['LED','MIDDLE-LEFT'],
                ['LEAD', 'BOTTOM-RIGHT'],
                ['READ','MIDDLE-RIGHT'],
                ['RED','MIDDLE-RIGHT'],
                ['REED', 'BOTTOM-LEFT'],
                ['LEED','BOTTOM-LEFT'],
                ['HOLD ON','BOTTOM-RIGHT'],
                ['YOU', 'MIDDLE-RIGHT'],
                ['YOU ARE', 'BOTTOM-RIGHT'],
                ['YOUR','MIDDLE-RIGHT'],
                ['YOU\'RE','MIDDLE-RIGHT'],
                ['UR','TOP-LEFT'],
                ['THERE','BOTTOM-RIGHT'],
                ['THEY\'RE','BOTTOM-LEFT'],
                ['THEIR','MIDDLE-RIGHT'],
                ['THEY ARE','MIDDLE-LEFT'],
                ['SEE','BOTTOM-RIGHT'],
                ['C','TOP-RIGHT'],
                ['CEE','BOTTOM-RIGHT']]
    top_word.sort()
    print('\n')
    for i in range(len(top_word)):
        print(top_word[i])
    input('\n\nPress Enter to continue...')
    second_word = [["READY:   YES, OKAY, WHAT, MIDDLE, LEFT, PRESS, RIGHT, BLANK, READY, NO, FIRST, UHHH, NOTHING, WAIT"],
                   ["FIRST:   LEFT, OKAY, YES, MIDDLE, NO, RIGHT, NOTHING, UHHH, WAIT, READY, BLANK, WHAT, PRESS, FIRST"],
                   ["NO:      BLANK, UHHH, WAIT, FIRST, WHAT, READY, RIGHT, YES, NOTHING, LEFT, PRESS, OKAY, NO, MIDDLE"],
                   ["BLANK:   WAIT, RIGHT, OKAY, MIDDLE, BLANK, PRESS, READY, NOTHING, NO, WHAT, LEFT, UHHH, YES, FIRST"],
                   ["NOTHING: UHHH, RIGHT, OKAY, MIDDLE, YES, BLANK, NO, PRESS, LEFT, WHAT, WAIT, FIRST, NOTHING, READY"],
                   ["YES:     OKAY, RIGHT, UHHH, MIDDLE, FIRST, WHAT, PRESS, READY, NOTHING, YES, LEFT, BLANK, NO, WAIT"],
                   ["WHAT:    UHHH, WHAT, LEFT, NOTHING, READY, BLANK, MIDDLE, NO, OKAY, FIRST, WAIT, YES, PRESS, RIGHT"],
                   ["UHHH:    READY, NOTHING, LEFT, WHAT, OKAY, YES, RIGHT, NO, PRESS, BLANK, UHHH, MIDDLE, WAIT, FIRST"],
                   ["LEFT:    RIGHT, LEFT, FIRST, NO, MIDDLE, YES, BLANK, WHAT, UHHH, WAIT, PRESS, READY, OKAY, NOTHING"],
                   ["RIGHT:   YES, NOTHING, READY, PRESS, NO, WAIT, WHAT, RIGHT, MIDDLE, LEFT, UHHH, BLANK, OKAY, FIRST"],
                   ["MIDDLE:  BLANK, READY, OKAY, WHAT, NOTHING, PRESS, NO, WAIT, LEFT, MIDDLE, RIGHT, FIRST, UHHH, YES"],
                   ["OKAY:    MIDDLE, NO, FIRST, YES, UHHH, NOTHING, WAIT, OKAY, LEFT, READY, BLANK, PRESS, WHAT, RIGHT"],
                   ["WAIT:    UHHH, NO, BLANK, OKAY, YES, LEFT, FIRST, PRESS, WHAT, WAIT, NOTHING, READY, RIGHT, MIDDLE"],
                   ["PRESS:   RIGHT, MIDDLE, YES, READY, PRESS, OKAY, NOTHING, UHHH, BLANK, LEFT, FIRST, WHAT, NO, WAIT"],
                   ["YOU:     SURE, YOU ARE, YOUR, YOU\'RE, NEXT, UH HUH, UR, HOLD, WHAT?, YOU, UH UH, LIKE, DONE, U"],
                   ["YOU ARE: YOUR, NEXT, LIKE, UH HUH, WHAT?, DONE, UH UH, HOLD, YOU, U, YOU\'RE, SURE, UR, YOU ARE"],
                   ["YOUR:    UH UH, YOU ARE, UH HUH, YOUR, NEXT, UR, SURE, U, YOU\'RE, YOU, WHAT?, HOLD, LIKE, DONE"],
                   ["YOU'RE:  YOU, YOU\'RE, UR, NEXT, UH UH, YOU ARE, U, YOUR, WHAT?, UH HUH, SURE, DONE, LIKE, HOLD"],
                   ["UR:      DONE, U, UR, UH HUH, WHAT?, SURE, YOUR, HOLD, YOU\'RE, LIKE, NEXT, UH UH, YOU ARE, YOU"],
                   ["U:       UH HUH, SURE, NEXT, WHAT?, YOU\'RE, UR, UH UH, DONE, U, YOU, LIKE, HOLD, YOU ARE, YOUR"],
                   ["UH HUH:  UH HUH, YOUR, YOU ARE, YOU, DONE, HOLD, UH UH, NEXT, SURE, LIKE, YOU\'RE, UR, U, WHAT?"],
                   ["UH UH:   UR, U, YOU ARE, YOU\'RE, NEXT, UH UH, DONE, YOU, UH HUH, LIKE, YOUR, SURE, HOLD, WHAT?"],
                   ["WHAT?:   YOU, HOLD, YOU\'RE, YOUR, U, DONE, UH UH, LIKE, YOU ARE, UH HUH, UR, NEXT, WHAT?, SURE"],
                   ["DONE:    SURE, UH HUH, NEXT, WHAT?, YOUR, UR, YOU\'RE, HOLD, LIKE, YOU, U, YOU ARE, UH UH, DONE"],
                   ["NEXT:    WHAT?, UH HUH, UH UH, YOUR, HOLD, SURE, NEXT, LIKE, DONE, YOU ARE, UR, YOU\'RE, U, YOU"],
                   ["HOLD:    YOU ARE, U, DONE, UH UH, YOU, UR, SURE, WHAT?, YOU\'RE, NEXT, HOLD, UH HUH, YOUR, LIKE"],
                   ["SURE:    YOU ARE, DONE, LIKE, YOU\'RE, YOU, HOLD, UH HUH, UR, SURE, U, WHAT?, NEXT, YOUR, UH UH"],
                   ["LIKE:    YOU\'RE, NEXT, U, UR, HOLD, DONE, UH UH, WHAT?, UH HUH, YOU, LIKE, SURE, YOU ARE, YOUR"]]
    second_word.sort()
    for i in range(len(second_word)):
        print(second_word[i])
        


#def maze():
#    circle_loc = [input('Circle Location...\nROW: '),input('COLUMN: ')]
#    led_loc = [input('\n\nLED Location...\nROW: '),input('COLUMN: ')]
#    triangle_loc = [input('Circle Location...\nROW: '),input('COLUMN: ')]
    #pygame.init()
    #class Maze1:
    #def __init__(self):
    #    self.M = 10
    #    self.N = 8
    #    self.maze = [ 1,1,1,1,1,1,1,1,1,1,1,1,1,
    #                  1,0,0,0,0,0,1,0,0,0,0,0,1,
    #                  1,0,1,1,1,0,1,0,1,1,1,1,1,
    #                  1,0,1,0,0,0,1,0,0,0,0,0,1,
    #                  1,0,1,0,1,1,1,1,1,1,1,0,1,
    #                  1,0,1,0,0,0,1,0,0,0,0,0,1,
    #                  1,0,1,1,1,0,1,0,1,1,1,0,1,
    #                  1,0,1,0,0,0,0,0,1,0,0,0,1,
    #                  1,0,1,1,1,1,1,1,1,1,1,0,1,
    #                  1,0,0,0,0,0,1,0,0,0,1,0,1,
    #                  1,0,1,1,1,0,1,0,1,1,1,0,1,
    #                  1,0,0,0,1,0,0,0,1,0,0,0,1,
    #                  1,1,1,1,1,1,1,1,1,1,1,1,1]

print('testing again')