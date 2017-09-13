'''One of the simplest two-player games is “Guess the number”. The first player thinks of a secret number in some known range while the second player attempts to guess the number. After each guess, the first player answers either “Higher”, “Lower” or “Correct!” depending on whether the secret number is higher, lower or equal to the guess. In this project, you will build a simple interactive program in Python where the computer will take the role of the first player while you play as the second player.

When discussing ranges in this mini-project, we will follow the standard Python convention of including the low end of the range and excluding the high end of the range. Mathematically, we will express ranges via the notation [𝚕𝚘𝚠, 𝚑𝚒𝚐𝚑). The square bracket of the left of the range indicates that the corresponding bound should be included. The left parenthesis on the right of the range indicates that corresponding bound should be excluded. For example, the range [𝟶, 𝟹) consists of numbers starting at 0 up to, but not including 3. In other words 0, 1, and 2.'''

import random
import simplegui

# initialize global variables used in your code
global num_range,b
num_range=100
b=7

#number= random.randrange(0,100)

# helper function to start and restart the game
def new_game():
    
    global secret_number,num_range,rem,b
    rem=b
    print "new game started"
    print
    print"the new range is 0 to ",num_range
    secret_number = random.randrange(0,num_range);
    print "number of remaining guesses=",rem
    
    


def range100():
    # button that changes range to range [0,100) and restarts
    global num_range,b
    b=7
    num_range=100
    
    
    new_game()
    
   

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range,b
    num_range=1000
    
    b=10
    
    new_game()
    
    
    
   
def input_guess(guess):
    global val,secret_number,rem

    val=int(guess)
    
    
    rem=rem-1
    
    print "the guess was",val
    print "number of remaining guesses=",rem
    
   
        
    if(val>secret_number):
        if rem==0:
            
            print "you ran out of guesses ,new game will begin now"
            print "the number was",secret_number
            print
            new_game()
        else:
                print "Lower"
                print
            
        
            
    elif(val<secret_number):
        if rem==0:
            
            print "you ran out of guesses ,new game will begin now"
            print "the number was",secret_number
            print
            new_game()
        else:
            print "higher"
            print
    else:
        
         print "correct"
         print
         new_game()
    
    
    
    
   

    



# create frame
frame=simplegui.create_frame('Testing', 300, 300)
frame.add_button("Range is [0,100)",range100,200)
frame.add_button("Range is [0,1000)",range1000,200)
inp = frame.add_input('Enter a guess', input_guess, 200)


new_game()
frame.start();

# call new_game and start frame



