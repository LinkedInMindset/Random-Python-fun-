#Name: Jonathan Sands
#Date: 10/19/2020
#Honor Statement:“I have not given or received any unauthorized assistance on this assignment.”
#YouTube:https://www.youtube.com/watch?v=AW5bNzj8uyw




import random


class SixSidedDie():

    '''Class for six sided dice'''

    #Initialize to sides and face value = 1
    def __init__(self, sides = 6):

        self.sides = sides
        self.faceValue = 1

    #Create roll function that rolls the dice and returns the face value
    def roll(self):    

        self.faceValue = random.randint(1, self.sides)
        
        return self.faceValue

    #Create a function that prints the face value
    def getFaceValue(self):

        print('{}'.format(self.faceValue))

    #create the __repr__ function for the class that displays the facevalue and object class
    def __repr__(self):

        return 'SixSidedDie({})'.format(self.faceValue)



class TenSidedDie(SixSidedDie):

    '''Class for 10 sided dice, subclass of SixSidedDie'''

    #Initialize the number of sides and face value
    def __init__(self, sides = 10):

        self.sides = sides
        self.faceValue = 1

    #Create the __repr__ function for the class
    def __repr__(self):

        return 'TenSidedDie({})'.format(self.faceValue)



class TwentySidedDie(SixSidedDie):

    '''Class for 20 sided dice, subclass of SixSidedDice'''

    #Initialize the number of sides and face value
    def __init__(self, sides = 20):

        self.sides = sides
        self.faceValue = 1

    #Define the __repr__ format
    def __repr__(self):

        return 'TwentySidedDie({})'.format(self.faceValue)



class Cup():

    '''Create the cup class which has the ability to hold multiple dice of various types'''

    #Initialize the number of various types of dice in the cup
    def __init__(self, sixdie = 1, tendie = 1, twentydie = 1):

        #Initialize an array of all current face values
        self.dice = []

        self.numsix = sixdie
        self.numten = tendie
        self.numtwenty = twentydie

        self.sixdie = SixSidedDie()
        self.tendie = TenSidedDie()
        self.twentydie = TwentySidedDie()

    #Create a roll function that rolls each die, returns the array of face values
    def roll(self):

        for i in range(self.numsix):

            self.dice.append(self.sixdie.roll())

        for i in range(self.numten):

            self.dice.append(self.tendie.roll())

        for i in range(self.numtwenty):

            self.dice.append(self.twentydie.roll())
        
        
        return self.dice
            
    #Define the function that sums the face values
    def sum(self):
         
        return (sum(self.dice))

    #Define the repr formating function
    def __repr__(self):

        return 'Cup(SixSidedDie({}), TenSidedDie({}), TwentySidedDie({}))'.format(self.dice[0:self.numsix], self.dice[self.numsix:self.numsix + self.numten], self.dice[self.numsix + self.numten:])









def main():

    #Take the users name, initialize their balance and determine whether they would like to play the game
    Name, balance, gamequestion = Greeting()

    #Start the game, if applicable
    while gamequestion =='Yes':

        #Check the users balance
        checkBalance(balance)

        #Find the target number
        goal = generateGoal()

        #Take the users bet and subtract it from their current balance
        bet, balance = betAmount(balance)

        #Take how many dice the user would like to use
        sixSide, tenSide, twentySide = howManyDice()

        #Get the roll and sum it up
        sum = createCup(sixSide, tenSide, twentySide)

        #Determine whether the user won anything and adjust balance accordingly
        balance = didWeWin(balance, sum, goal, bet)

        #Prompt user to play the game again
        gamequestion = input('Would you like to play again')



def Greeting():

    '''Introduce the game to user. Initialize balance, user name, and confirm their desire to play the game'''

    name = input('Enter your name.')

    balance = 100

    print('\nHello ' + name + ', this is the cups and dice game. \nThe game involves rolling an amount of six, ten, and/or twenty sided dice to get a randomly generated goal. \nIf your dice land on the number, you get 10x your bet. \nWithin 3 and you get 5x and finally within 10 you get 2x.')

    gamequestion = input('\nWould you like to play the game?')

    #return user name, balance and game question
    return name, balance, gamequestion


def checkBalance(balance):
    
    '''Make sure you have money'''

    if balance == 0:
        
        print('You have no money!')


def generateGoal():

    '''Random number between 1 and 100'''

    goal = random.randint(1,100)

    print('\nYour target is {}'.format(goal))

    #Return the target roll
    return goal


def betAmount(balance):

    '''Specify bet amount'''

    print('\nYour current balance is {}'.format(balance))

    bet = int(input('\nEnter the amount you would like to bet, from 1 - 100.'))

    if balance >= bet > 0:

        balance  -= bet

        #return the bet and new balance
        return bet, balance    

    else:
        
        print('Invalid bet')


def howManyDice():

    '''Specify the amount of the different types of dice you would like to use'''

    sixside = int(input('How many 6 sided dice would you like to use'))

    tenside = int(input('How many 10 sided dice would you like to use'))

    twentyside = int(input('How many 20 sided dice would you like to use'))

    #return the number of 6, 10, and 20 sided die
    return sixside, tenside, twentyside


def createCup(sixside, tenside, twentyside):

    '''create the cup which holds the dice'''

    c = Cup(sixside, tenside, twentyside)

    c.roll()

    sum = c.sum()

    print('\n{}'.format(sum))

    #return the sum of all facevalues
    return sum

def didWeWin(balance, sum, goal, bet):

    '''Determine whether or not the user won anything and adjust balance accordingly'''

    #Best case scenario, 10x winnings
    if sum == goal:
        
        print('\nYou hit the nail on the head! x10')
        balance += bet * 10
    
    #Second best case, 3x winnings
    elif goal in range(sum - 3, sum + 3):

        print('\nSo close! x3')

        balance += bet * 5
    
    #Third best case, 2x winnings
    elif goal in range(sum - 10,sum + 10):

        print('\nI feel bad making you leave with nothing. x2')
        balance += bet * 2
    
    #You lose :(
    else:

        print("You're really bad at this")

    return balance

main()


