'''Rock-paper-scissors is a hand game that is played by two people. The players count to three in unison and simultaneously "throw” one of three hand signals that correspond to rock, paper or scissors. The winner is determined by the rules:

Rock smashes scissors
Scissors cuts paper
Paper covers rock
Rock-paper-scissors is a surprisingly popular game that many people play seriously (see the Wikipedia article for details). Due to the fact that a tie happens around 1/3 of the time, several variants of Rock-Paper-Scissors exist that include more choices to make ties less likely.

Rock-paper-scissors-lizard-Spock (RPSLS) is a variant of Rock-paper-scissors that allows five choices. Each choice wins against two other choices, loses against two other choices and ties against itself. Much of RPSLS's popularity is that it has been featured in 3 episodes of the TV series "The Big Bang Theory". The Wikipedia entry for RPSLS gives the complete description of the details of the game.

In our first mini-project, we will build a Python function 𝚛𝚙𝚜𝚕𝚜(𝚗𝚊𝚖𝚎) that takes as input the string 𝚗𝚊𝚖𝚎, which is one of "𝚛𝚘𝚌𝚔", "𝚙𝚊𝚙𝚎𝚛", "𝚜𝚌𝚒𝚜𝚜𝚘𝚛𝚜", "𝚕𝚒𝚣𝚊𝚛𝚍", or "𝚂𝚙𝚘𝚌𝚔". The function then simulates playing a round of Rock-paper-scissors-lizard-Spock by generating its own random choice from these alternatives and then determining the winner using a simple rule that we will next describe.

While Rock-paper-scissor-lizard-Spock has a set of ten rules that logically determine who wins a round of RPSLS, coding up these rules would require a large number (5x5=25) of 𝚒𝚏/𝚎𝚕𝚒𝚏/𝚎𝚕𝚜𝚎 clauses in your mini-project code. A simpler method for determining the winner is to assign each of the five choices a number:

0 — rock
1 — Spock
2 — paper
3 — lizard
4 — scissors
In this expanded list, each choice wins against the preceding two choices and loses against the following two choices (if rock and scissors are thought of as being adjacent using modular arithmetic).'''



import random


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
# convert number to a name using if/elif/else
def number_to_name(number):
    # fill in your code below
    if (number == 0):
        return "rock"
    elif (number == 1):
        return "Spock"
    elif (number == 2):
        return "paper"
    elif (number == 3):
        return "lizard"
    elif (number == 4):
        return "scissors"
    else:
        return "Invalid Number !!"
    
    
 
    
    # convert name to number using if/elif/else
def name_to_number(name):
    # fill in your code below
    if (name=="rock"):
        return 0
    elif (name=="Spock"):
        return 1
    elif (name=="paper"):
        return 2
    elif (name=="lizard"):
        return 3
    elif (name=="scissors"):
        return 4
    else :
        return "invalid"
    # fill in your code below

    
    


def rpsls(name): 
    
    # compute random guess for comp_number using random.randrange()
    comp_num=random.randrange(0,5)
    print "Player chooses",name
    print "Computer chooses",number_to_name(comp_num)
    # convert comp_number to name using number_to_name
    player_num= name_to_number(name);
    # convert name to player_number using name_to_number
    # compute difference of player_number and comp_number modulo five

    diff=player_num-comp_num;
    mod=diff%5
    # use if/elif/else to determine winner
    if(mod==1 or mod==2):
        print "Player wins!"
    elif(mod==3 or mod==4):
        print "Computer wins!"
    else:
        print "Player and computer tie!"
    print
    print
    # print results
    

 

    
    

    
    
    

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




