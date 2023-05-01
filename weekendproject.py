import random


card_dict = {'A':11, 'K':10, 'Q':10,'J':10,'10':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def  __str__(self):
        return self.value + ' of ' + self.suit + ':'
    



class Deck:

    def __init__(self):
        self.suits = ['hearts','diamonds','spades','clubs']
        self.card_values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.deck = []   
        for suit in self.suits:
            for card_value in self.card_values:
                card = Card(suit,card_value)
                self.deck.append(card)
        random.shuffle(self.deck)
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
            return 'the deck has' + deck_comp
    
    def draw_card(self):
        if len(self.deck) == 0:
            print('deck is empty')
            return None
        return self.deck.pop()
    
   
class Player:

    def __init__(self):
        self.hand = []
        self.value = 0
    
    def __str__(self):
        hand_comp = ' '
        for card in self.hand:
            hand_comp += ' ' + card.__str__() 
        return hand_comp + ' your total value is ' + self.value.__str__()
    
    def add_card(self,card):
        self.hand.append(card)
        self.value += card_dict[card.value]
    





def main():
    
    #DATA CREATIon
    dealer = Player()
    player = Player()
    deck = Deck()
    player.add_card(deck.draw_card())
    player.add_card(deck.draw_card())
    dealer.add_card(deck.draw_card())
    dealer.add_card(deck.draw_card())
    print(player.__str__())
    flag = True
    while flag:
        res = input('would you like to hit or stand: enter h or s: ')
        if res == 'h':
            player.add_card(deck.draw_card())
            print(player.__str__())
            if player.value > 21:
                print('you have busted')
                res2 = input('would you like to play again? enter y or n: ' )
                if res2 == 'y':
                    main()
                elif res2 == 'n':
                    flag = False
                else:
                    print('please enter a valid character')
        elif res == 's':
            print(dealer.__str__())
            while dealer.value <=17:
                dealer.add_card(deck.draw_card())
                print(dealer.__str__())
            if dealer.value > 21:
                print('dealer busts, player wins')
                res6 = input('would you like to play again? enter y or n: ' )
                if res6 == 'y':
                    main()
                elif res6 == 'n':
                    flag = False
                else:
                    print('please enter a valid character')
            if dealer.value > player.value:
                print('dealer wins')
                res3 = input('would you like to play again? enter y or n: ' )
                if res3 == 'y':
                    main()
                elif res3 == 'n':
                    flag = False
                else:
                    print('please enter a valid character')
            elif dealer.value < player.value:
                print('player wins')
                res4 = input('would you like to play again? enter y or n: ' )
                if res4 == 'y':
                    main()
                elif res4 == 'n':
                    flag = False
                else:
                    print('please enter a valid character')
            else:
                print('hand pushed, no body wins')
                res5 = input('would you like to play again? enter y or n: ' )
                if res5 == 'y':
                    main()
                elif res5 == 'n':
                    flag = False
                else:
                    print('please enter a valid character')
        else:
            print('please enter a valid character')
        
    
            

    

    


#     #GAME LOGIC
#     #dealer deals out cards
#     #tell player what cards they have
#     #tell player one of dealers cards
#     #check for bust player
#     #check if player == 21 player wins
#     #player hits or stands
#         # hits 
#             # call draw card
#             # if over 21 bust
#             # give option to hit again
#         #stands
#             #go on to the dealer
#     #dealer shows cards
#         #if over 21: bust
#         #if 21
#             #if player also 21 push
#             #if player under 21 dealer wins
#         #if under 17 hit
#         # when over 17 
#             # compare player and dealers cards
#             # if players cards over dealers cards player wins
#             # if dealers cards over players cards player wins
#             #if dealers cards == players cards push
    
    
#     #END OF GAME
#     #ask if they want to continue or not
#         #if yes continue
#             #clear cards and  hands
#         #if no quit

if __name__ == "__main__":
    main()