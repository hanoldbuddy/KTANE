import sys
from modules import *

again = True
completed = 0
sessions = 1
timepermodule = 0
num_modules = 0
comp_time = 0

def credits(completed, comp_time, timepermodule):
    victory = input("Did you WIN? (y/n): ")
    if victory == "y":
        print("Congrats to JOSH & JONNY!!")
        #adding rick rolled content
        again = play(sessions)
    elif victory == "n":
        print('Better luck next time!\nY\'all completed ' , completed , ' modules in ' , time , '.\nThat\'s ' , timepermodule , ' per module.')
        again = play(sessions)
    return again

def compute_score(comp_time, num_modules):
    num_modules += 1
    #get time. time by modules
    return timepermodule

def play(sessions):
    again = input('Play Again? (y/n): ')
    if again == 'y':
        sessions += 1
        again = True
    elif again == 'n':
        again = False
    else:
        print("...(y/n)")
        #add some comedic content
    return again

def init():
    facts = []
    facts.append(input("Number of batteries: "))
    facts.append(input("Lit CAR (y/n): "))
    facts.append(input("Lit FRK? (y/n): "))
    facts.append(input("Last diget of serial # EVEN? (y/n): "))
    facts.append(input("Vowel in serial #? (y/n): "))
    facts.append(input("Parallel Port? (y/n): "))
    return facts

while again:
    facts = init()
    while True:
        module = int(input("\n\nModule:\n  1 - Needy Knob\n  2 - Wires\n  3 - Button\n  4 - Simon Says\n  5 - LED Word\n  6 - LED Number\n  7 - Maze\n  8 - Symbols\n  9 - Password/Word Scroll\n 10 - Mega Hertz\n 11 - Numbers Wires Letters\n 12 - Wire Star LED\n 99 - GAME OVER\n\n"))
        if module == 1:
            needy(facts)
            #done
        elif module == 2:
            wires(facts)
            #done
        elif module == 3:
            button(facts)
            #done
        elif module == 4:
            ss(facts)
            #done
        elif module == 5:
            led_word(facts)
        elif module == 6:
            led_num()
        elif module == 7:
            maze()
        elif module == 8:
            symbols(facts)
        elif module == 9:
            password(facts)
        elif module == 10:
            mhg(facts)
        elif module == 11:
            nwl()
        elif module == 12:
            led_star_wire(facts)
        elif module == 99:
            again = credits(completed, comp_time, timepermodule)
            break
        else:
            continue
        compute_score(comp_time, num_modules)
    break



