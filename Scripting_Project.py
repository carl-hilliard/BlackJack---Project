"""
Carl Hilliard
Introduction to Scripting
April 12, 2022
Final Project: Blackjack Game
"""

## Rules for the Blackjack game:
"""
1) Each player should have a mimimum of $50. If a player has less than $50,
    they will be dropped from the game.
    
2) There should be a shoe of cards, which may contain anywhere from 4 to 8 decks of
    cards. Generally, 8 deck of cards. (Note: one deck of cards has 52 cards,
    you will have:
    13 black colored clubs,
    13 red colored diamonds,
    13 red colored hearts,
    13 black colored spades.)
    
3) The dealer will shuffle each deck of cards once. This shuffles all the cards in
    shoe once.
    
4) There will be one dealer and 1-6 players.

5) At the start of the game, each player will have $500-$5,000

6) Each player cannot sit out of the game for more than 3 rounds total.

7) Once dealer reaches 17, he/she will not be pulling anymore cards for himself.
"""

## The game:
"""
1) The dealer asks each player to bet. To play a hand, minimum bet is $25 for
    each player.
    
2) Round 1: Once the bets are put on the table, dealer pulls a card from the stack
    and deals it to the leftmost player. He/she will put out other card and deal
    it to the player sitting second to the left. He/she deals first round to all
    the players, starting from the left side and ending with the right side.
    
3) Next, dealer will deal for himself with a face-down card

4) Dealer will deal second round for all players just like #2. If any player
    reaches 21 with any of the combinations (Ace + Jack), (Ace + King),
    (Ace + Queen), or (Ace + 10), then the player is considered
    the winner (blackjack).
    
5) Dealer will deal a card for himself faceup. The dealer will check the bottom
    card and see if the combination of cards is 21.

6) If the dealer's combination of cards is 21, the dealer wins. Suppose a player
    with cards up has a total of 21, then he is also a winner. 21 can be a
    combination of (Ace + Jack), (Ace + King), (Ace + Queen), or (Ace + 10).

7) If the dealer does not win, then the games of Round 2.
"""
## Round 2:
"""
8) The face down card of the dealer will still be face down.

9) The dealer will ask each player if he wants to hit, double, split, or stand.
    a) If hit, a new card will be delt from the shoe
    b) If double, a single card will be delt with double money. No more cards are
        delt to a player who selects this option.
    c) If stand, no new card will be delt.
    d) Split option is only available if the two cards to the player are the same.

10) Then we go on to the next round. From third round, double and split will not
    be available. If a player reaches more than 21, then it's a bust and the player
    loses the game.

11) Once everyone stands or requires no more cards, then dealer would open
    the dealer's closed card.

12) Dealer will keep on taking a card until the total sum of cards reaches
    17 or higher.

13) Winner:
    a) If the dealer goes beyond 21, every player who is not bust(sum of the
        value of cards is higher than 21) is a winner.
    b) If the dealer is with range between 21 to 17, every player who had higher
        value than the dealer is winner.
    c) If a player has a value of 21, then he is a winner.
"""


## Note:
"""
## Kings, Queens, and Jacks are considered to have a value of 10. Aces are of value
## 11 or 1. The value of an ace is chosen by the player.
"""


## Payoff:
"""
## If a player gets a blackjack, then the payoff is 3:1
## If a player is a winner, then the payoff is 2:1
"""



## Explaining of logic for writing the code:
"""
Step #1:
    I will need to create a class for the player.
        The player class will have attributes for cards, and starting money.
        It will have a getTotalCards function.
        It will have a getTotalMoney function.
        It will have a function to return the value of each individual card.
        

    I will need to create a class for the cards.
        The cards will need to have an attribute for value, face, suit, and color.
        Ace cards will be a special case that can have value of 11 or of 1.
        There are 4 - 8 decks, with 52 cards per deck.

    I will need to use random in order to shuffle the shoe, that will be performed
    on the cards class.


Step #2:
    The player number will signify their position. Player 1 is leftmost, Player 2
    is second to the left, so on.

    How to implement a face down card? -

    Draw a card function

    If the card is an Ace - create a function to ask for 

"""



## Import the random library. This will be used instead of actual players making decisions.
import random
from random import shuffle

# Use random to generate how many players will be entered into the game of blackjack.
numPlayers = 5
print("This table has", numPlayers, "players.")
print()

# Use random to generate the number of games that will be played. It will be a minimum of 10
numGames = random.randint(10, 20)
print("The number of games that will be played is: ", numGames)
print()




# THE CARD CLASS 
class Card:
    ## Define the constructor, the init method, passing in self, face, value, suit, and color
    def __init__(self, color, suit, value, face):
        ## Assign the private member variables to the values passed in to the init method
        self.color = color
        self.suit = suit
        self.value = value
        self.face = face

    ## define a print card function
    def print(self):
        print("Color:", self.color)
        print("Suit:", self.suit)
        print("Value:", self.value)
        print("Face:", self.face) #prints true if the card is a face card(jack, king, queen)

    ## Define a function to change the ace value

"""
card=Card("Red", "hearts", "7", bool(False))
card.print()
"""





"""
## THE PERSON CLASS: This will be a parent function, it's children will be the player class and the dealer class.
## It will only include variables and functions that belong to both the player class and the dealer class.
class Human:

    ## Define the constructor
    def __init__(self):
        ## Define a member variable for the human's current hand of cards
        self.__hand = []

        ## Define a member variable for the human's current score that is contained in his hand of cards
        self.__score = 0



    ## Define a get card function
    def getCard(self, card):
        self.__hand.append(card)


    ## Create a function to calculate the score
    def calculateScore(self):
        ## Increase self.score by the value of all the cards in the human's hand
        for card in self.__hand:
            self.__score += card.value
        ## Return the score
        return self.__score


    ## Create a function to print the cards contained in the current hand of the human
    def printHand(self):
        print(self.__hand)
        print()


    ## Create a function that returns the score
    def getScore(self):
        return self.__score



"""










## THE PLAYER CLASS: Create a human class and use inheritance for player and dealer
class Player():
    ## Define the constructor(the init method).
    def __init__(self):
        ## Randomize the players starting balance
        self.__balance = random.randint(500, 5000)

        ## Define the starting balance member variable
        self.__startingBalance = self.__balance

        ## Create an array of cards for the player
        self.__hand = []

        ## Create a score variable
        self.__score = 0

        ## Create a variable for the amount of rounds skipped
        self.__skippedRounds = 0

        ## Define a current bet variable
        self.__currentBet = 0



    ## Define the getCard function
    def getCard(self, card):
        ## append the new card to the player's hand
        self.__hand.append(card)


    ## Increase balance function
    ## This function will be called if a player wins money
    def increaseBalance(self, amount):
        ## Increase the balance by the amount the player won
        self.__balance = self.__balance + amount


    ## Decrease balance function
    def decreaseBalance(self, amount):
        ## Decrease the balance by the amount the player lost
        self.__balance = self.__balance - amount

    
    ## Create a function to get the score
    def calculateScore(self):
        ## increase self.score by the value of all the cards in the players hand
        for card in self.__hand:
            self.__score += card.value


    ## Increase rounds skipped
    def increaseRoundsSkipped(self):
        ## increments the rounds skipped variable for when a player bets nothing
        self.__skippedRounds += 1


    ## Define the printHand function
    def printHand(self):
        print(self.__hand)

    ## Define a print balance function
    def printBalance():
        print("The original balance of the player was $", self.__startingBalance)
        print("The current balance of the player is $", self.__balance)

    ## Define a setBet function
    def setBet(self, bet):
        self.__currentBet = bet
        ## Call the decreaseBalance function
        self.decreaseBalance(bet)


    ## Define a getBalance function
    def getBalance(self):
        ## return the balance
        return self.__balance


    ## Define a get turns skipped function
    def getRoundsSkipped(self):
        ## return the number of turns skipped
        return self.__skippedRounds


    ## Define a getBet function
    def getBet(self):
        return self.__currentBet


    ## Create a function that returns the score
    def getScore(self):
        return self.__score


    
    
                

    ## Will need balance as a member variable
    ## Will need array of cards as a member attribute
    ## Will need a variable to keep track of the amount of rounds skipped
    ## Will need to have score as a member variable
    ## The player will not be able to leave himself with less than $25 in the bank (no all in)




## THE DEALER CLASS
class Dealer():
    
    
    ## create a constructor (init function) to create a dealer object
    def __init__(self):
        ## Define a member variable for the dealer's hand of cards
        self.__hand = []

        ## Define a member variable for the dealer's score in his hand of cards
        self.__score = 0



    ## A get card function
    def getCard(self, card):
        self.__hand.append(card)


    ## Create a function to get the score
    def calculateScore(self):
        ## increase self.score by the value of all the cards in the players hand
        for card in self.__hand:
            self.__score += card.value


     ## Define theprintHand function
    def printHand(self):
        print(self.__hand)


    ## Create a function that returns the score
    def getScore(self):
        return self.__score





    
      
"""
Include a list, a dictionary and a try/except block
"""


# THE DECK
# Create a function that will fill the deck. The function will take an array as an argument
def fillDeck(deck):
    
    # Use an outer for loop that iterates 4 times (once for each suit)
    # Use an inner for loop that iterates 13 times (once for each value of card)

    # Create an array to hold the four suits of card
    suits = ["Diamonds", "Spades", "Hearts", "Clubs"]

    #Create an array to hold the values of the cards
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # The outer loop
    for suit in suits:
        # The inner loop
        for value in values:
            ## Assign the card a color, the color is based on the suit. Hearts and diamonds are red, clubs and spades are black
            if((suit == "Diamonds") or (suit == "Hearts")):
                color = "Red"
            else:
                color = "Black"
                
            ## If the value == 1, the card is an ace. Randomly reassign the value as either 1, or 11
            if(value == 1):
                rand = random.random()
                ## Make the ace have a value of 11
                if(rand > 0.5):
                    newValue = 11
                    card = Card(color, suit, newValue, False)
                    deck.append(card)
                ## Make the ace have a value of 1
                else:
                    card = Card(color, suit, value, False)
                    ## Append the card to the deck
                    deck.append(card)
                    
            ## If the card is a face value, it must have a value of 10, and the .face attribute of the class must be changed
            elif(value > 10):
                newValue = 10
                isFace = True
                card = Card(color, suit, newValue, isFace)
                ## Append the card to the deck
                deck.append(card)
            else:
                #use the card class and the for loops to create card objects
                card = Card(color, suit, value, False)
                deck.append(card)


# Create an array based stack to hold the first deck of cards
deck1 = []

## Call the function fillDeck
fillDeck(deck1)


print(len(deck1))
print("Before shuffle: ", deck1[0].suit)
shuffle(deck1) ## DO NOT USE THE SHUFFLE FUNCTION
print("After shuffle: ", deck1[0].suit)


## CREATE THE SHOE. It will be an array based stack
shoe = []

# Use a for loop to create the 8 decks
for i in range(8):
    deck = [] ## create a temporary deck
    fillDeck(deck) ## call the fillDeck function on the deck
    ## shuffle the deck
    shuffle(deck)
    print("Length of deck number", i, len(deck))
    for card in deck:
        shoe.append(card)
## Shuffle the shoe
shuffle(shoe)

print(len(shoe))
    


"""
print("Size: ", len(deck1))
for x in deck1:
    x.print()
    print()
"""




    ## ROUND ONE: TURN ONE
## The game will consist of between 10 and 20 rounds.
## All of these functions will need print functions 
"""
Face up / face down does not matter 
Define a function that does the first round only
    Everything for each round of the game will be containebd within this function
    Will be called for every round
    ## MOST OF THE LOGIC WILL GO HERE IN THIS FUNCTION
    
    Ask each player to bet
     call the setBet function for all players (DO NOT INCLUDE DEALER FOR THIS)

    After this, the dealer needs to deal a card to the first player. Then the second, so on.. then himself last(this card is facedown)

    Deal a second card to all the players
    When you deal each card to each player, check their score. If they hit 21, they win. Any player who hits 21 wins.
    Then the dealer deals a face up card to himself and the dealer will check if the combination of both cards in his hand is 21.
        If the dealer has 21, he wins
        If the dealer has 21, and at least 1 other player has 21, that player neither wins nor loses his bet. Every other player with !=21 loses.

        




Define a function that does a round ( a full game)
ROUND TWO:
    Ask each player to bet with setBet

    
    
    
    







And then you'll have a function that calls the round function numGames number of times
    This function will be called once



"""



## THE GAME FUNCTION:
## The rounds are contained and run within this function, through loops
## this function will need to be called numGames number of times. use another function for this



## Every player gets delt 2 cards
## If a player hits blackjack, they win.
## If the dealer hits blackjack, the dealer wins.
## If no one hits blackjack, then the decisions will start.
## A player should be able to hit, double, split or stand
## Split and double are only available for one round, during the first decision point.
## Each time that a player gets a card, you have to check their score to see if they win or bust or whatever
## The dealer keeps taking a card until he reaches 17 or higher, and then he will stand every time.

## If a player gets a blackjack, let the other players finish their decisions, then the round stops.

## Check the score after the last player has gone through the loop, 

## If the dealer busts, every player who doesn't bust wins.
## If the dealer is between 21 and 17, every player who has a higher value then the dealer without busting wins. 




## define the start game function
def startGame(numGames):


    print("The game has started")
    
    ## use a for loop and give every player their first card, if they have enough money and they have skipped less than 3 rounds.
    ## Create an array of players, which will not include the dealer
    arrPlayers = []

    ## Create the table, which will include the dealer
    table = []



    ## Create the correct number of players.
    for i in range (numPlayers):
        ## Call the constructor (init function)
        player = Player()

        ## Add the player to the array of players
        arrPlayers.append(player)
        ## add the player to the table
        table.append(player)

    ## Add the dealer to the table, he will be last
    dealer = Dealer()
    table.append(dealer)

    ## Call the function that will allow the players to make bets
    playersWithBets = []
    playersWithBets = takingAllBets(arrPlayers)

    ## Have the dealer give everyone (including the dealer) two cards to start the game
    for i in arrPlayers:
        card = shoe.pop()
        i.getCard(card)
        i.getCard(card)

    ## give the dealer his cards
    card = shoe.pop()
    dealer.getCard(card)
    dealer.getCard(card)
    
        
        ##i.printHand()
    print("Bet Amount:", i.getBet())

    ## check to see if any of the players went over 21
    playerBust(arrPlayers)

    ## use a loop to check the player's score
    for i in arrPlayers:
        rando = random.random()
        
        card = shoe.pop()
        i.calculateScore()
        temp = i.getScore()
        ## use an if statement to form some decisions for the players
        if(temp <= 14): ## the player will always hit if his score is <=14
            i.getCard(card)
        ## else use randomly generated numbers to make decisions based on score
        ## if the score is 15, they have a 90% chance to hit
        elif(temp == 15):
            if(rando >= 0.11): ## 90% chance for the player to hit (take a card)
                i.getCard(card)
        ## if the score is 16, they have a 70% chance to hit
        elif(temp == 16):
            if(rando >= 0.3):
                i.getCard(card)
            else: ## otherwise they double
                i.getCard(card)
                tempBet = i.getBet()
                i.setBet(tempBet *2)
                
        ## if the score is 17, they have a 60% chance to hit
        elif(temp == 17):
            if(rando >= 0.4):
                i.getCard(card)
            else: ## otherwise they double
                i.getCard(card)
                tempBet = i.getBet()
                i.setBet(tempBet *2) ## double their bet
        ## if the score is 18, they have a 50% chance to hit
        elif(temp == 18):
            if(rando >= 0.8):
                i.getCard(card)
            else: ## otherwise they double
                i.getCard(card)
                tempBet = i.getBet()
                i.setBet(tempBet *2)
        ## if the score is 19, they have a 5% chance to hit
        elif(temp == 19):
            if(rando >= 0.94):
               i.getCard(card)
            else: ## otherwise they double
                i.getCard(card)
                tempBet = i.getBet()
                i.setBet(tempBet *2)
        ## if the score is 20, they have a 2% chance to hit
        elif(temp == 20):
            if(rando >= 0.98):
                i.getCard(card)
            else: ## otherwise they double
                i.getCard(card)
                tempBet = i.getBet()
                i.setBet(tempBet *2)
        ## i.printHand()
                
    ## Check to see if ANY player has 21 points. If someone does, then pay out bets.
    ##for i in players
    for i in arrPlayers:
        ## check if they have 21
        i.calculateScore()
        tempScore = i.getScore()
        tempBet = i.getBet()
        if(tempScore == 21):
            i.increaseBalance(tempBet *3)
            print("The player has a blackjack!")




    ## Check to see if any players beat the dealer without getting 21
    dealer.calculateScore()
    dealerScore = dealer.getScore()
    if(dealerScore < 17):
        dealer.getCard(card)
    ## compare the dealer's score to all the players score
    ## if the player's score is higher than the dealer and is less than 21, the payoff is 2:1
    ## if a player tied the dealer, the hand is a wash, and the bet is neither lost nor earned
    ## THIS IS THE SCENARIO IF THE DEALER HAS NOT EXCEEDED 21
    elif(dealerScore < 21):
        for i in arrPlayers:
            ## compare their score to the dealer
            i.calculateScore()
            tempScore = i.getScore()
            tempBet = i.getBet()

            if((tempScore < 21) and (tempScore > dealerScore)):
                i.increaseBalance(tempBet *2)
            elif((tempScore == dealerScore)):
                i.increaseBalance(tempBet)
            else:
                print("The player lost to the dealer")
            
    else: ## THIS IS THE SCENARIO IF THE DEALER HAS BUST
        for i in arrPlayers:
            ## compare their score to the dealer
            i.calculateScore()
            tempScore = i.getScore()
            tempBet = i.getBet()

            if(tempBet < 21):
                i.increaseBalance(tempBet *2)
                print("The player beat the dealer!")
                





## Define a function to play a "game"
def playGame(playersWithBets):
    return 0





## Define a function to check the score of every player
def playerBust(arrPlayers):
    ## use a loop to check the players scores
    for player in arrPlayers:
        if(player.getScore() > 21):
            player.decreaseBalance(player.getBet)
            




   
## Define the function that will allow the players to take bets
def takingAllBets(arrPlayers1):

    ## use a loop to get the bets from the players
    for player in arrPlayers1:
        print("The size of arrPlayers:", len(arrPlayers1))
        ## use the random function to assign bets
        rand = random.random()
        """
        ## Make sure the player has not already skipped too many turns
        if(player.getTurnsSkipped >= 3):
            ## The player cannot play anymore
            player.bet = 0
            player.setBet(bet)
        """

       
        tempSkipped = player.getRoundsSkipped()
        
        print("Number of turns skipped", tempSkipped)
        print("Player balance: ", player.getBalance())
        tempBalance = player.getBalance()

        ## Write an if statement to remove a player from the game if they have already skipped3 rounds
        if(tempSkipped >= 3):
            arrPlayers1.remove(player) ## this will prevent them from taking cards from the shoe and betting in the future
        
        ## if rand is less than 0.1, they will skip the turn
        ## for static values, use a temp variable instead of repeated calls
        if((rand <= 0.10) or (tempSkipped >= 3) or (player.getBalance() < 51)): 
            bet = 0 
            ## pass bet into the current player bet
            player.setBet(bet)

            ## increment the skipped turns
            player.increaseRoundsSkipped()





        elif(rand >= 0.11 and rand < 0.25):
            bet = (rand * 1000) ## Randomize the bet value 
            ## check to make sure the player has enough money to bet
            if(bet >= (tempBalance -50)):
                print("Player is running low on money. Current balance is:", player.printBalance)
                bet = 26
            ## pass bet into the current player bet
            player.setBet(bet)

        elif(rand >= 0.26 and rand < 0.45):
            # make bet = rand * 100
            bet = ((rand * 100) + (rand * 100))
            ## check to make sure the player has enough money to bet
            if(bet >= (player.getBalance() -50)):
                print("Player is running low on money. Current balance is:", player.printBalance)
            ## pass bet into the current player bet
            player.setBet(bet)

        elif(rand >= 0.46 and rand < 0.64):
            bet = ((rand * 100) + (rand * 100))
            ## check to make sure the player has enough money to bet
            if(bet >= (player.getBalance() -50)):
                print("Player is running low on money. Current balance is:", player.printBalance)
                bet = 26
            ## pass bet into the current player bet
            player.setBet(bet)

        elif(rand >= 0.65 and rand <0.9):
            bet = ((rand * 100) + (rand * 100))
            ## check to make sure the player has enough money to bet
            if(bet >= (player.getBalance() -50)):
                print("Player is running low on money. Current balance is:", player.printBalance)
                bet = 26
            ## pass bet into the current player bet
            player.setBet(bet)

        elif(rand >= 0.91 and rand < 0.98):
            bet = ((rand * 100) + (rand * 100))
            ## check to make sure the player has enough money to bet
            if(bet >= (player.getBalance() -50)):
                print("Player is running low on money. Current balance is:", player.printBalance)
                bet = 26
            ## pass bet into the current player bet
            player.setBet(bet)

        elif(rand >= 0.99):
            bet = player.balance - 100
            ## check to make sure the player has enough money to bet
            if(bet >= (player.getBalance() -50)):
                print("Player is running low on money. Current balance is:", player.printBalance)
                bet = 26
            ## pass bet into the current player bet
            player.setBet(bet)

        return arrPlayers1

    

## Define the main and call some stuff
def main():
    ## call the startGames function
    startGame(numGames)


## call the main
main()
    




## Explanation of Code and flowchart:
"""
I took an OOP approach to this project. The first thing that I did was create classes for cards, the dealer, and the player.
There would be an array of players (not including the dealer) and an array for the table (including the dealer).
All decisions would be randomized.

Then, I created the shoe using a stack data structure of objects from the card class that I had previously defined.

Before the start of each round, I make sure to check that the players have not skipped more than 3 rounds (which is a condition for quitting the game),
and that they have enough money to keep betting.
Both the number of rounds skipped and the amount of money are attributes of the player class.

The first thing to happen during the game, is that the players will be dealt two cards each, from left to right.
Based on their score, they have a chance to hit, a chance to stand, and a chance to double on the third turn.

The bets are assigned randomly.
The decisions are made randomly.
The number of rounds in the game is random
The starting balances are assigned randomly.

The score, suit, face, and color of each card is an attribute of the card class.

If the dealer has less than 17, he will continue to hit, until he either has between 17 and 20, has a blackjack, or busts.

The round will end and bets will be paid after EITHER:
1) a player(s) gets a blackjack
2) The dealer has at least 17, and all the players have at least 14

This will cause the bets to be paid out.
The bets are dependent on a randomly generated number, and are an attribute of the player class.

If a player ties the dealer, his bet is neither won nor lost. It is a wash.

All variables for all classes are private.
Accessor functions (getters) and mutator functions (setters) are used to modify and compare the values contained
within the private member variables in classes.

Because I used an OOP approach, I tried to complete as much of the project as possible by using classes and functions. Loops were
used much less, and I feel like this approach made my code much more efficient, but also much more difficult to write, read, de-bug, and understand.
"""




















    
    
