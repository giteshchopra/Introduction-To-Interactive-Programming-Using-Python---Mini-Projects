'''Blackjack is a simple, popular card game that is played in many casinos. Cards in Blackjack have the following values: an ace may be valued as either 1 or 11 (player's choice), face cards (kings, queens and jacks) are valued at 10 and the value of the remaining cards corresponds to their number. During a round of Blackjack, the players plays against a dealer with the goal of building a hand (a collection of cards) whose cards have a total value that is higher than the value of the dealer's hand, but not over 21. (A round of Blackjack is also sometimes referred to as a hand.)

The game logic for oursimplified version of Blackjack is as follows. The player and the dealer are each dealt two cards initially with one of the dealer's cards being dealt faced down (his hole card). The player may then ask for the dealer to repeatedly "hit" his hand by dealing him another card. If, at any point, the value of the player's hand exceeds 21, the player is "busted" and loses immediately. At any point prior to busting, the player may "stand" and the dealer will then hit his hand until the value of his hand is 17 or more. (For the dealer, aces count as 11 unless it causes the dealer's hand to bust). If the dealer busts, the player wins. Otherwise, the player and dealer then compare the values of their hands and the hand with the higher value wins. The dealer wins ties in our version.'''
# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
winner=""


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand :
    def __init__(self):
        self.cards=[]
        
    def add_card(self ,card):
        self.cards.append(card)
    def __str__(self):
        
        str1=""
        for i in range (len(self.cards)):
            str1=str1 + " " + str(self.cards[i])
        return "Hand contains " + str1
    def get_value(self):
        hand_value = 0
        aces = False
        
        for cards in self.cards:
            
            hand_value += VALUES[cards.get_rank()]
            
            if cards.get_rank() == 'A':
                aces = True
                
        if aces and (hand_value + 10) <= 21:
                    hand_value += 10
            
               

        return hand_value
            
            
            
    def draw(self, canvas, pos):
        i=RANKS.index(self.suit)
        j=SUITS.index(self.rank)
        card_pos=[CARD_CENTER+i*CARD_SIZE[0],CARD_CENTER+j*CARD_SIZE[0]]
        canvas.draw_image(card_image,card_pos,CARD_SIZE,pos,CARD_SIZE)
                  

Dealer=Hand()
Player=Hand()
        
# define deck class 
class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                c=Card(suit,rank)
                self.deck.append(c)

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)    # use random.shuffle()

    def deal_card(self):
        return random.choice(self.deck)
            
    
    def __str__(self):
        str1=""
        for i in range (len(self.deck)):
            str1=str1 + str(self.deck[i])
        return "Deck contains" + str1



#define event handlers for buttons
def deal():
    global outcome, in_play,deck,Dealer,Player,winner,score
    if in_play:
        score-=1
        in_play=False
        winner="PLAYER LOST , because You quit"
        outcome="new deal ? "
    winner=""
    outcome="HIT OR STAND ?"
    deck=Deck()
    deck.shuffle()
    Dealer=Hand()
    Player=Hand()
    Player.add_card(deck.deal_card())
    Player.add_card(deck.deal_card())
    Dealer.add_card(deck.deal_card())
    Dealer.add_card(deck.deal_card())
    
    
    
    
    # your code goes here
    
    in_play = True

def hit():
    global in_play,Player,Dealer,outcome,winner,score
    if in_play:
        outcome="HIT OR STAND ?"
        print Player.get_value()
        if Player.get_value()<=21:
            Player.add_card(deck.deal_card())
            if Player.get_value()>21:
                
                outcome="NEW DEAL ? "
                winner="YOU BUSTED , DEALER WINS"
                in_play=False
                score=score-1
        else:
            
            outcome="NEW DEAL?"
            winner="YOU BUSTED DEALER WINS"
            score=score-1
            in_play=False
            
    # replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global Dealer,in_play,outcome,winner,score
    if not in_play:
        
        outcome="NEW DEAL ? "
        
    else:
        in_play=False
        while Dealer.get_value()<17:
            Dealer.add_card(deck.deal_card())
            if Dealer.get_value()>21:
                    
                    winner="PLAYER WINS DEALER BUSTED"
                   
                    
        if (Dealer.get_value()<=21)and( Dealer.get_value()>Player.get_value() or Dealer.get_value()==Player.get_value()):
            
            winner="DEALER WINS"
            outcome="NEW DEAL?"
            score=score-1
        else:
            
            winner="player WINS"
            outcome="NEW DEAL?"
            score=score+1
        
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    global Player,Dealer,outcome,winner,in_play,score
    posp=[100,400]
    posd=[100,150]
    for card in Player.cards:
        
        card.draw(canvas, posp)
        posp[0]+=2*CARD_SIZE[0]
    for card in Dealer.cards:
        card.draw(canvas,posd)
        posd[0]+=2*CARD_SIZE[0]
        if in_play:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100 + CARD_BACK_CENTER[0], 150 + CARD_BACK_CENTER[1]], CARD_SIZE)    
    canvas.draw_text('BLACKJACK',(50,50),25,'White')
    canvas.draw_text('PLAYER',(100,350),25,'White')
    canvas.draw_text('DEALER',(100,100),25,'White')
    canvas.draw_text(outcome, (300,350),25,'WHITE')
    canvas.draw_text(winner, (300,100),25,'WHITE')
    canvas.draw_text("SCORE : "+str(score), (700,25),25,'RED')
        

    
    
    


# initialization frame
frame = simplegui.create_frame("Blackjack", 900, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


