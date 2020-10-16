
#Name: Jonathan Sands
#Date: 10/08/2020
#Honor Statement: I have not given or received any unauthorized assistance on this assignment
#YouTube: https://www.youtube.com/watch?v=cw9L4mo-QzU

import random


def main():

    '''My main function that holds all of my helper functions...
    Prints a statement out determining which, if any, items from a list sum to a specified sum...
    Employs binary search'''


    cont = 'Yes'
    while cont == 'Yes':

        #take desired inputs as integers
        length, sum = getInputs()

        #Creates a sorted list of a specified length
        list = createList(length)

        #Conducts binary search to return to numbers that sum to the sum, or two strings indicating there are none
        i, j = binarySearch(list, length, sum)

        printStatement(i, j, sum)

        cont = input('Would you like to run the test again? (Yes/No)')



def getInputs():

    '''Prompts the user for a set of inputs and returns them as ints'''


    length = int(input('What length would you like your list to be?'))
    sum = int(input('What would you like to test for the sum?'))

    return length, sum



def createList(length):

    '''Create a sorted list of random values between 0 and 100'''


    #create the list
    list = random.sample(range(0, 100), length)

    #sort the list
    list.sort()

    print(list)
  
    return list 



def binarySearch(list, length, sum):

    '''Conducts binary search over a sorted list to detect values of the list that sum to the given input'''


    #initialize return variables
    x = 'empty'
    y = 'empty'

    #loop over the list (provides the n to the n log(n) complexity)
    for i in list:

        #initialize the low and high points
        low = 0

        high = length - 1

        #loop which breaks down the size of our list we are testing (provides the log(n))
        while low <= high:
            
            #set the midpoint
            mid = (low + high) // 2

            #get the mid item from the list
            item = list[mid]

            #check to see if it sums to our sum
            if sum == i + item:

                x = i
                y = item

                return x, y

            #if it's greater then the sum, decrease the high
            elif sum < i + item:

                high = mid - 1
                
            #if it's less than the sum, increase the low
            elif sum > i + item:

                low = mid + 1
    
    return x, y

            

def printStatement(i, j, sum):

    '''Prints the final equation'''


    #if x and y remain unchaged in the binarySearch function we did not find a solution
    if i == 'empty' and j == 'empty':

        print('No list objects add to ' + str(sum))

    #else print the solution
    else:

        print( str(i) + ' + ' + str(j) + ' = ' + str(sum))


main()