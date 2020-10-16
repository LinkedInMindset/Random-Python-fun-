#Name: Jonathan Sands
#Data Due: 09/28/2020
#Honor Statement: I have not given or received any unauthorized assistance on this assignment
#Youtube: https://www.youtube.com/watch?v=YaqrZC4VEeg




def main():

    #Calls all helper functions that lead to prinitng a stem and leaf diagram
    #Contains a while loop to help prompt the user if they would like to continue with other datasets

    #Greetings and description to the user
    printIntro()

    #Initialize continue variable
    cont = 'Yes'

    #Initialize path (unique to one's own pc)
    path = "D:/DePaul/DSC 430/"

    while cont == 'Yes':

        #Return file input, 1, 2 or 3 (I included several modified versions (4,5) in my video
        x = getInputs()

        #Returns the an array of points of the selected dataset
        array = fetchData(x, path)

        #Constructs the dataset
        construct(array)

        #Prompts the user to see if they would like to continue
        cont = input('Would you like to run the software again? (Yes/No)')



def printIntro():

    #Intro, not much else to say

    print('Hello. This is a program that will create a stem and leaf plot')
    print('based on the value you input in the next prompt. The code will')
    print('prompt you at the end to continue or discontinue. If you would')
    print('like to continue type "Yes", otherwise type "No".')


def getInputs():

    #Prompts user for 1/2/3 value input

    x = input('What data set would you like to create a stem and leaf plot for? (1/2/3)')

    return x


def fetchData(x, path):

    #Takes the input value 'x' and concats it to the location of my dataset in my computer to return
    #the dataset as a sorted array

    #File location
    filename = path + "StemAndLeaf" +x+ ".txt"

    #Read file
    infile = open(filename, "r")
    lineList = infile.readlines()
    infile.close()

    #place read file into an array
    array = []

    for i in range (0, len(lineList)):

        x = int(lineList[i].strip())

        array.append(x)
    
    #Sort array in ascending order
    array.sort()

    #return sorted array
    return array


def fixing_missing_values(x, y):

    #Compensates for stems that do not have and leaves, it adds them to the plot but leaves the
    #leaf section blank

    while int(y) - int(x) > 1:

        missing = int(x) + 1

        print(str(missing) + "      |     ")      

        x = missing



def construct(array):
    
    #Takes the sorted array and constructs a stem and leaf plot, stems and leaves are selected based on 
    #divisibility by 10. This may lead to an error later on, if a data set has a large range, it could
    # prove difficult to read not useful

    #Initialize stems and leaves
    stem0 = str(array[0] // 10)
    leaves = []

    for i in range(len(array)):

        stem = str(array[i] // 10)

        #add leaves to leaves array
        if stem == stem0:
            leaves.append(array[i] % 10)      

        #if we encounter a new stem, print the current stem with it's leaves and move to the next stem
        elif stem != stem0:

            print(stem0 + "      |      ",  leaves)

            fixing_missing_values(stem0, stem)
       
            stem0 = stem
            leaves = []

            leaves.append(array[i] % 10)

main()

