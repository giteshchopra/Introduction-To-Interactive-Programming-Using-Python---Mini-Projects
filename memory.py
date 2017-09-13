#Memory is a card game in which the player deals out a set of cards face down. In Memory, a turn (or a move) consists of the player flipping over two cards. If they match, the player leaves them face up. If they don't match, the player flips the cards back face down. The goal of Memory is to end up with all of the cards flipped face up in the minimum number of turns. For this project, we will keep our model for Memory fairly simple. A Memory deck consists of eight pairs of matching cards.
# implementation of card game - Memory
import simplegui
import random
c = 0

i = 0
i = 0
j = 0
state  = 0
list1 = range(8)
list2= range(8)
exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
list3 = list1 + list2
random.shuffle(list3)
count =0
# helper function to initialize globals
def new_game():
    global exposed,count,turns
    count=0
    turns=0
    label.set_text("Turns = "+str(count))
    exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state,i,j,cards,count
    if 0<=pos[0]<=799 and exposed[pos[0] // 50] == False:
        cardno = pos[0]//50
        
        if state == 0:
            state = 1
            exposed[cardno] = True
            i = cardno
        
        elif state == 1:
            state = 2
            exposed[cardno] = True
            j = cardno
            count+=1
            label.set_text("Turns = "+str(count))                   
        elif state == 2:
            state = 0
            if list3[i] == list3[j]:
                exposed[i] = True
                exposed[j] = True
            else:
                exposed[i] = False
                exposed[j] = False
            mouseclick(pos)
                
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global c,d,i,state
    c=0
    for check in exposed:
            if check == True:
                    canvas.draw_text(str(list3[c]), (c*50,75), 75, 'White')
                    c = c+1
            elif check == False:
                    canvas.draw_polygon([(c*50, 0), ((c+1)*50, 0), ((c+1)*50, 100), (c*50, 100)], 1,"brown", "green")
                    c = c+1
    
    
        
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)

label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()    


