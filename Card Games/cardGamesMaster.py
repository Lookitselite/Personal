import random
class Card:
    suitNames = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rankNames = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def getRank(self):
        return self.rank
    def setRank(self, rankIndex):
        self.rank = rankIndex

    def __init__(self, suitIndex, rankIndex):   #constructor method
        self.suit = suitIndex
        self.rank = rankIndex

    def lessThan(self, otherCard):
        if self.suit < otherCard.suit:
            return True
        elif self.suit == otherCard.suit:
            if self.rank < otherCard.rank:
                return True
        return False

    def add(self, otherCard):
        if self.suit + otherCard.suit >= len(Card.suitNames):
            print('Cannot add the cards')
        elif self.rank + otherCard.rank >= len(Card.rankNames):
            print('Cannot add the cards')
        else:
            print(Card(self.suit + otherCard.suit, self.rank + otherCard.rank))

    def __str__(self):
        return Card.rankNames[self.rank] + ' of ' + Card.suitNames[self.suit]

class Deck(Card):
    def __init__(self):
        self.cardList = []

    def populate(self):
        for i in range(4):
            for ii in range(1, 14):
                self.cardList.append(Card(i, ii))
        
    def printCards(self):
        for card in self.cardList:
            print(card)
    
    def addCard(self, c):
        self.cardList.append(c)

    def popCard(self):
        return self.cardList.pop()

    def shuffle(self):
        random.shuffle(self.cardList)


class Hand(Deck):
    def __init__(self):
        self.cardList = []
    
    def printCards(self):
        return super().printCards()
    
    def popCard(self):
        return super().popCard()
    
    def eval(self):
        val = 0
        print(self.cardList)
        for i in self.cardList:
            val += i.getRank()
        return val 
    
    def blackjackEval(self):
        val = 0
        l = []
        for i in self.cardList:
            l.append(i.rank)
        for i in l:
            if i in [11, 12, 13]:
                val += 10
            else:
                val += i
        return val


    
def blackjack():
    gameDeck = Deck()
    gameDeck.populate()
    gameDeck.shuffle()
    pHand = Hand()
    dHand = Hand()
    round = 0
    exceed = True

    #game loop
    while exceed:
        round += 1
        if round == 1:
            for i in range(2):
                pHand.addCard(gameDeck.popCard())
                dHand.addCard(gameDeck.popCard())
        else:
            if input('Hit or Stand: ') in ['hit', 'Hit']:
                pHand.addCard(gameDeck.popCard())
                if pHand.blackjackEval() > 21:
                    print('Your cards total ', pHand.blackjackEval(), ', you went bust!')
                    exceed = False
                elif pHand.blackjackEval() == 21:
                    print('You hit Blackjack! You win!!!')
                    exceed = False
                else:
                    pass
            else:
                pass
            if dHand.blackjackEval() < 17:
                dHand.addCard(gameDeck.popCard())
                if dHand.blackjackEval() > 21:
                    print('Dealers cards total ', pHand.blackjackEval(), ', he went bust!')
                    exceed = False
                elif pHand.blackjackEval() == 21:
                    print('Dealer hit Blackjack! You Lose!!!')
                    exceed = False
        print('Your Cards:')
        pHand.printCards()
        print('totaling' , pHand.blackjackEval())
        print('Dealers Cards:')
        dHand.printCards()
        print('totaling' , dHand.blackjackEval())
    
    
blackjack()
    
def tex():
    gameDeck = Deck()
    gameDeck.populate()
    gameDeck.shuffle()
    p1Hand = Hand()
    p2Hand = Hand()
    table = Hand()
    p1 = 'Bashar'
    p1p = 10
    p1bet = 0
    p2 = 'Tuck'
    p2p = 10
    p2bet = 0

    #init deal
    for i in range(2):
        p1Hand.addCard(gameDeck.popCard())
        p2Hand.addCard(gameDeck.popCard())
    print("You have:", end = '')
    p1Hand.printCards()
    #init bet
    p1bet += int(input('How much would you like to bet?'))
    p2bet += random.randint(1, 3)
    p1p -= p1bet
    p2p -= p2bet
    print('Have: ', p1p, 'Betting: ', p1bet)
    #flop, turn, river
    for i in range(3):
        table.addCard(gameDeck.popCard())
    print("Cards on table: ")
    table.printCards()
    #flop bet
    p1bet += int(input('How much would you like to bet?'))
    p2bet += random.randint(1, 3)
    p1p -= p1bet
    p2p -= p2bet
    print('Have: ', p1p, 'Betting: ', p1bet)

#tex()

def war():
    gameDeck = Deck()
    gameDeck.populate()
    gameDeck.shuffle()
    p1Hand = Hand()
    p2Hand = Hand()
    numGames = int(input('How many games would you like to play: '))
    player1 = 'Jack'
    player2 = 'Jane'
    p1Wins = 0
    p2Wins = 0

    for i in range(numGames):
        p1Hand.addCard(gameDeck.popCard())
        p2Hand.addCard(gameDeck.popCard())

        print(player1 + ' has', end = ' ')
        p1Hand.printCards()
        print(player2 + ' has', end = ' ')
        p2Hand.printCards()
        print('\n')

        c1 = p1Hand.popCard()
        c2 = p2Hand.popCard()
        if c1.lessThan(c2):
            p2Wins += 1
        else:
            p1Wins += 1

    if p1Wins > p2Wins:
        print(player1 + ' Wins!!')
    elif p1Wins == p2Wins:
        print('Tie')
    else:
        print(player2 + ' Wins!!')

#war()
