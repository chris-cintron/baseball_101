import sys, random

position = 0
outs = 0 
runs = 0
first_base = False
second_base = False
third_base = False
home_plate_scored = False

def play_ball():
    global outs
    at_bat = input("Press b to swing the bat ")
    if at_bat == 'b':
        swing()        
   

def swing():
    hits =('flyout', 'strikeout', 'groundout', 'single', 'double', 'triple', 'homerun')

    swing = random.choice(hits)
        
    if swing == hits[0]:
        print("You swung the bat and....Flyout!")
        out()
    elif swing == hits[1]:
        print("You swung the bat and....strikeout!")
        out()
    elif swing == hits[2]:
        print("You swung the bat and....ground out!")
        out()
    elif swing == hits[3]:
        print("You swung the bat and....single!")
        single()
        score()
    elif swing == hits[4]:
        print("You swung the bat and....double!")
        double()
        score()
    elif swing == hits[5]:
        print("You swung the bat and....triple!")
        triple()        
        score()
    elif swing == hits[6]:
        print("You swung the bat and....HOME RUN!")
        homerun()        
        score()


def score():
    print("Outs: ", outs)
    print("Runs: ", runs)                      

 
def homerun():

    global runs    
    global home_plate_scored
    global first_base
    global second_base
    global third_base
    
    
    if first_base == True:
        runs += 1
    if first_base == True and second_base == True and third_base == True:
        runs += 3
    if first_base == True and second_base == True and third_base == False:
        runs += 2
    if first_base == True and  second_base == False and third_base == True:
        runs += 2
    if first_base == False and  second_base == False and third_base == True:
        runs += 1
    if first_base == False and  second_base == True and third_base == True:
        runs += 2
    if first_base == False and  second_base == True and third_base == False:
        runs += 1
    if first_base == True and  second_base == False and third_base == True:
        runs += 2
    first_base = False
    second_base = False
    third_base = False

    home_plate_scored = True
    print("Touch all the bases!")
    runs += 1
    
    score()
    next_batter()    


def single():
    global runs
    global first_base
    global second_base
    global third_base
    global home_plate_scored
    
    if first_base == True:
        first_base = True
        second_base = True
        third_base = False
    elif first_base == True and second_base == True:
        first_base= True
        second_base = True        
        third_base = True
    elif first_base == True and second_base== True and third_base==True:
        runs += 1
        first_base = True
        second_base = True
        third_base = True
    elif second_base == True:
        first_base = True
        second_base = False
        third_base = True
    elif second_base == True and third_base == True:
        first_base = True
        second_base = False
        third_base = True
        home_plate_scored = True
        runs +=1
    elif third_base == True:
        first_base = True
        second_base = False
        third_base = False
        home_plate_scored = True
        runs += 1
    
    first_base = True
    second_base = False
    third_base = False
    print ('\nYou reached first base', '\n')   
    
    score ()
    next_batter() 


def double():

    
    global first_base
    global second_base
    global third_base
    global home_plate_scored
    global runs
    
    
    if first_base == True:
        first_base = False
        second_base = True
        third_base = True
    elif first_base==True and second_base == True :
        home_plate_scored = True
        runs += 1
        first_base = False
        second_base = True
        third_base = False
    elif first_base == True and third_base == True:
        home_plate_scored = True
        runs += 1
        first_base = False
        second_base = True
        third_base = False
    elif first_base == True and second_base == True and third_base == True:
        home_plate_scored = True
        runs += 2
        first_base = False
        second_base = True
        third_base = True
    elif second_base == True:
        first_base = False
        second_base = True
        third_base = False
        home_plate_scored = True
        runs += 1
    elif second_base == True and third_base == True:
        home_plate_scored = True
        runs += 2
        first_base = False
        second_base = True
        third_base = False
    elif third_base == True:
        home_plate_scored = True
        runs += 1
        first_base = False
        second_base = True
        third_base = False
    
    second_base = True
    first_base = False
    third_base = False
    print ('\nYou reached second base''\n')   
    
    score()
    next_batter()


def triple():

    global runs
    global first_base
    global second_base
    global third_base
    global home_plate_scored
    
    if first_base == True:
        home_plate_scored = True
        runs +=1
        first_base = False
        second_base = False
        third_base = True
    elif first_base == True and second_base == True:
        first_base = False
        second_base = False
        third_base = True
        home_plate_scored = True
        runs +=2
    elif first_base == True and third_base == True:
        home_plate_scored = True
        runs +=2
        first_base = False
        second_base = False
        third_base = True
    elif second_base == True:
        home_plate_scored = True
        runs +=1
        first_base = False
        second_base = False
        third_base = True
    elif second_base == True and third_base == True:
        home_plate_scored = True
        runs +=2
        first_base = False
        second_base = False
        third_base = True
    elif third_base == True:
        home_plate_scored = True
        runs +=1
        first_base = False
        second_base = False
        third_base = True
    
    third_base = True
    first_base = False
    second_base = False
    print ('\nYou reached third base' '\n')
    
    score()
    next_batter()

    
def out():

    global outs

    print ('You are OUT!\n')

    while outs <= 3:

        outs += 1

        print ('Outs: ', outs, '\n')

        if outs == 3:
            print ('End of inning')
            print(team_name.upper(),  "scored", runs, "runs.")
            sys.exit()

        next_batter()


def next_batter():
    
    global playing

    playing = input('Bring next batter?(y/n): ')

    if playing == 'y':        
        
        play_ball()

    if playing == 'n':
        print ('\nThanks for playing!')
        sys.exit()


        #initial screen
print('      BATTER UP!')
print("P         D         P")
print('L       -   -       L')
print('A     -        -    A')
print('Y   D            D  Y')
print("B     -        -    B")
print("A       -    -      A")
print('L         D         L')
print('L                   L')
choice= input("Wanna Play? Y or N: ")
if choice.upper() == 'Y':
    team_name = input("What is your teams name? ")
    print(team_name.upper(),  "! You're up to bat.")
    play_ball() 
else:
    print("That's too bad!")
    sys.ext()




