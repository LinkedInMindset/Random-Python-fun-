
#Name: Jonathan Sands
#Date: 10/04/2020
#Honor Statement:
#YouTube: https://www.youtube.com/watch?v=BYCgnakOGb8

def main():

    '''My main function is just a while loop that's main function is to ask the user if he or she would like to continue'''
    
    continueMain = 'y'

    while continueMain == 'y':

        #Inputs
        shouldBeOne, numbers = input_()

        #function that contains the all processes
        cont, prime_or_not = loop(shouldBeOne, numbers)
        
        #Prints result
        print(cont + ' ' + prime_or_not)

        #Continue or not
        continueMain = input('Would you like to continue? (y/n)')


def input_():
    
    '''Manages the inputs and initialzation of variables/arrays'''

    #Input is taken
    x = input("Enter a positive integer to test: ")

    #The array to detect the 'Sad' loop is initialized
    array = []

    return x, array


def loop(shouldBeOne, numbers):
    
    '''loop functions as the parent function for all processes that determine the answer to the input number
    loop contains a while loop that continues to iterate until our steps reach the integer 1 or until there is a loop detected'''

    #isPrime determines whether the number isPrime
    prime_or_not = isPrime(int(shouldBeOne))

    cont = 'Continue'

    #Happy/Sad loop
    while cont == 'Continue':

        #turns the int into a string in order to break it apart and return an array of it's components squared
        squared = stringInts(shouldBeOne)

        #takes the squared values and checks to see if there are equal to 1, a repeating value, or just another number that needs to be iterated over
        numbers, shouldBeOne, cont = steps(squared, numbers)

    return cont, prime_or_not



def isPrime(number):
   
    '''Determines whether the input is prime'''

    #take 1 potential factor
    for i in range(2, number):

        #take a second potential factor
        for j in range(2, number):

            #If their product is that number, return non-prime
            if j * i == number:
                
                return 'non-prime'

            #If they are both equal to the last possible number then it is prime
            elif i == j == number - 1:
              
                return 'prime'



def stringInts(x):
    
    '''Function that's purpose is to return an array, squared, of the squared values of the input string, x'''

    #Determine the length of the number
    numStr = len(x)

    #Initialize the array of square values
    squared = []

    #loop over the input string, square and append the values to the squared array
    for i in range(numStr):

        squared.append(int(x[i])**2)

    return squared



def steps(squared, numbers):

    '''Function that chekcs to see if we have a loop, the desired answer, or just a new number to append '''

    #sum all values from the squared matrix
    sumSquared = sum(squared)

    #Checks to see if we found a happy number
    if sumSquared == 1:

        cont = 'Happy'
    
    #Checks to see if we found a sad loop
    elif sumSquared in numbers:

        cont = 'Sad'
    
    #append the number to the sad loop checker if neither of the previous were found
    else:

        numbers.append(sumSquared)

        cont = 'Continue'

    return numbers, str(sumSquared), cont

main()


