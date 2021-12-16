import random
game_on = True

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self) -> str:
        return self.rank + " of " + self.suit

    def r_value(self):
        return self.value

class Deck:

    def __init__(self) -> None:
        
        self.allCards = []
        self.card_traded = -1

        for suit in suits:
            for rank in ranks:
                self.allCards.append(Card(suit,rank))
        
    def shuffle(self):
        random.shuffle(self.allCards)
    
    def initialize(self):
        self.card_traded = -1
    
    def deal_one(self):
        self.card_traded += 1
        return self.allCards[self.card_traded]

        
    




class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces11 = 0
    
    def initialize(self):
        self.cards = []
        self.value = 0
        self.aces11 = 0
        

    def addCard(self,Card):
        if (Card.rank == 'Ace'):
            self.aces11 += 1
        
        self.value += Card.r_value()
        self.cards.append(Card)

    def str(self,num):
        for i in range(0,num):
            print(self.cards[i])
        if num!=1:
            print("total value of player = {}".format(self.value))
    
    def player_value(self):
        return self.value

    def card_count(self):
        return len(self.cards)



def bet_amt(credits):
    b = True
    while b:
        try: 
            bet = int(input("Enter the amount of money, you would like to bet: "))
        except:
            print("uh oh! enter numerals only.")
        else:
            print("validating {} credits for bet".format(bet))
            if(bet < credits):
                print("bet amount valid!")
                b = False
            else:
                print("bet value cannot exceed your credits")
    return bet

def rules():
    print("this is the blackjack tutorial\nat the start of the game the dealer and  the player get two card each")
    print("each card has an associated value which is as follows.")
    print(values)
    print("the ace can have the value 1 or 11. by default it is set to 11\nhowever in the course of game you will get the option to switch once")
    print("the total value must be less than 21 else the player busts and loses the bet, same restriction is on dealer")
    print("the user will know all his cards and the first card of dealer")
    print("he can choose hit to get more cards one at a time until he or the dealer busts\nat the first hit, dealer's value is made to cross 17")
    print("player can choose to stand, which will mean, the comparison of both the values of dealer and player, one with the higher value, wins")
    print("i hope that you like the game")

print("Welcome to BlackJack!\nTo play start by entering your name: ")
playerName = input()

print("We will start by giving you 1000 chips!\nYou will be betting using this virtual credit.")
credits = 1000
new_deck = Deck()
player = Hand()
dealer = Hand()

while True:
    new_deck.initialize()
    player.initialize()
    dealer.initialize()
    print("\n\nlet's start the game\ndo you wish to see the rules?")

    while True:
        try:
            rule = int(input("press 1 for yes, 0 for no.")) % 2
        except:
            print("uh oh! you did not enter a number. enter again")
        else:
            print("choice received\n")
            break


    if rule ==1:
        rules()

    new_deck.shuffle()
    print("\nthe cards have been shuffled")



    for i in range(0,2):
        player.addCard(new_deck.deal_one())
        dealer.addCard(new_deck.deal_one())

    player_card_count = player.card_count()
    dealer_card_count = dealer.card_count()

    print("your cards are: \n")
    player.str(player.card_count())

    print("\ndealer has this card:\n")
    dealer.str(1)
    game_on = False

    bet = bet_amt(credits)
    credits = credits - bet
    print("\n\nthe current value of your credits is {}".format(credits))



    while True:
        print("\n\ndo you wish to hit or stand?")
        while True: 
            try: 
                hit = int(input("press 1 for hit, 0 for stand."))%2
            except:
                print("uh oh! you did not enter a number. enter again")
            else:
                print("choice received\n")
                break

        if hit == 1:
            player.addCard(new_deck.deal_one())

            print("\nyour cards and the total value till now")
            player.str(player.card_count())

            if player.aces11 > 0:
                print("want to change the value of aces?")
                while True:
                    try:
                        aces_chnge = int(input("press 1 for yes, 0 for no.")) % 2
                    except:
                        print("uh oh! you did not enter a number. enter again")
                    else:
                        print("choice received\n")
                        break
                if aces_chnge == 1:
                    print("how many aces you would like to change?")
                    while True:
                        try:
                            change = int(input("enter the value:")) % player.aces11
                        except:
                            print("uh oh! you did not enter a number. enter again")
                        else:
                            print("choice received\n")
                            break
                            
                        num_to_change = player.aces11 - change
                        player.value = player.value - num_to_change*10
                        player.aces11 = player.aces11 - num_to_change

            

            if (player.player_value() > 21):
                print("\nplayer busted!\nyou lost the bet")
                break
        else: 
            print("\nplayer chooses to stand")
            while dealer.player_value() < 18 :
                dealer.addCard(new_deck.deal_one())

            if player.player_value() > dealer.player_value() or dealer.player_value()>21:
                print("\ncongrats! you win the bet.\nyou get twice the bet amount")
                credits = credits + 2*bet
                break
            else:
                print("you lost the bet : (\n")
                break
    
    print("do you wish to continue playing?")
    while True:
        try:
            game_On = int(input("press 1 for yes, 0 for no.")) % 2
        except:
            print("uh oh! you did not enter a number. enter again")
        else:
            print("choice received")
            break
    if game_On == 0:
        print("You won {} credits!".format(credits - 1000))
        print("thank you for playing blackjack. Bonne soiree")
        break



            

        


    


