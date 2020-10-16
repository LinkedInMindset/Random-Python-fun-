#Name: Jonathan Sands
#Date: 10/05/2020
#Honor Statement: I have not given or received any unauthorized assistance on this assignment
#YouTube: https://www.youtube.com/watch?v=glzu86vFxo0


def main():

    '''loop over 100 numbers to test if they meet the goldbach conjecture'''

    number = 4
    
    #Tests for numbers less than 100
    while number <= 100:

        #list of coprime numbers less than the number
        primeArray = coprimeList(number)
    
        #Determine which numbers from the list add to the number
        i, j = add(number, primeArray)

        #prints the equation
        printEquation(i, j, number)

        #goes to the next even number
        number += 2


def coprimeList(number):

    '''Creates and returns a list of coprime values less than our number'''

    #initializes the array and appends our first possible numer, 2
    primeArray = []
    primeArray.append(2)

    #loops over all possible numbers
    for i in range(2, number + 1):

        #initialize j
        j = 2


        while j < i:

            #determines is i is coprime to j
            x = coprime(i, j)

            #if it isn't we break
            if x == 0:

                break

            #if we need to check the next number
            elif x == 1:

                j+=1
            
            #if we've reach the end and haven't found factors, it is coprime, we append it to the list
            else:

                primeArray.append(x)

                j+=1

    return primeArray
        

def coprime(a, b):

    '''Determines if two numbers are coprime'''

    #returns 0 if they are not
    if (a % b == 0):

            return 0
    
    #returns a if they are coprime 
    elif a == b + 1 and a % b != 0:

            return a
    
    #if we need to keep checking return 1
    else:

        return 1


def add(number, array):

    '''Determines if the adding condition of the Goldbach conjecture is met'''

    for i in array:

        for j in array:

            if i + j == number:

                return i, j


def printEquation(i, j, number):

    '''Prints the equation'''

    #turns values into strings
    i = str(i)
    j = str(j)
    number = str(number)

    #prints
    print( i + " + " + j + " = " + number)


main()

input('press ENTER to exit')