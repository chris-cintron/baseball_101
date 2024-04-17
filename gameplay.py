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

  # Add a run for batter themself
  runs += 1
  home_plate_scored = True

  # Add runs for runners on base (who haven't scored yet)
  runs += first_base + (second_base and not third_base) + third_base

  first_base = False
  second_base = False
  third_base = False

  print("Touch all the bases!")
  score()
  next_batter()



def single():
  global runs
  global first_base
  global second_base
  global third_base
  global home_plate_scored

  # Move runner on third (if any) and score them
  if third_base:
    runs += 1
    print("Runner on third scores!")  # Announce the score
    third_base = False

  # Move runner on second to third (if any)
  elif second_base:
    third_base = True
    second_base = False
    print("Runner on second advances to third.")

  # Move runner on first to second (if any)
  elif first_base:
    second_base = True
    first_base = False
    print("Runner on first advances to second.")

  # Move batter to first
  first_base = True
  print("You single and reach first base!")

  # Reset home_plate_scored for next batter
  home_plate_scored = False
  score()
  next_batter()



def double():
  global runs
  global first_base
  global second_base
  global third_base
  global home_plate_scored

  # Move runner on third (if any) and score them
  if third_base:
    runs += 1
    third_base = False

  # Move runner on second to third and score them
  elif second_base:
    runs += 1
    third_base = True
    second_base = False

  # Move runner on first to third (considering it wasn't scored on the triple)
  elif first_base:
    third_base = True
    # We don't add a run here because the runner from first moved to third on the triple and shouldn't score again

  # Move batter to second
  second_base = True

  # Add runs for runners who HAVEN'T scored yet (were on 2nd or 3rd), considering runner wasn't created by the batter
  if second_base and not (first_base or second_base or third_base):  # Check for runner on second AND no runners on before
    runs += second_base

  # Reset home_plate_scored for next batter
  home_plate_scored = False
  print ('\nYou hit a DOUBLE and reached second base!\n')
  score()
  next_batter()


def triple():
  global runs
  global first_base
  global second_base
  global third_base
  global home_plate_scored

  # Move runners on third and second (if any) and score them (if not already scored)
  if third_base and not home_plate_scored:  # Only score runner on third if not scored before
    runs += 1
    third_base = False
  if second_base and not home_plate_scored:  # Only score runner on second if not scored before
    runs += 1
    third_base = True
    second_base = False

  # Move runner on first to third
  elif first_base:
    third_base = True
    first_base = False

  # Move batter to third
  third_base = True

  # Reset home_plate_scored for next batter
  home_plate_scored = False
  print ('\nYou hit a TRIPLE and reached third base!\n')
  score()
  next_batter()


    
def out():

    global outs

    print ('You are OUT!\n')

    while outs <= 3:

        outs += 1

        print ('Outs: ', outs)
        print('Runs:', runs)

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

