#Name: Jonathan Sands
#Date: 10/26/2020
#Honor Statement: I have not given or received any unauthorized assistance on this assignment.
#YouTube: https://www.youtube.com/watch?v=tCEitoPIur0


def main():

    #initialize palindrom list
    palindromList = []

    #set start and end dates
    end = '01/01/2100'
    start = '01/01/2000'

    #split the start and end dates
    x, y = splitInitial(start, end)
    
    #Narrow the search based on the century
    month = narrowSearch(x)
    
    #If we haven't reached the end date
    while x != y:

        #If the month is equal to the month we specified
        if x[1] == month:

            if checkPalindrom(x) == True:

                #Append the date to th list if it's a palindrom
                palindromList.append(x[:])
        

        x = advanceDate(x)

    #Write the list to the file
    writeToFile(palindromList)


def narrowSearch(start):

    '''Attempt to narrow the dates checked'''

    #Possible Palindrom dates are dates where the month corresponds to the reverse order of the first 2 digits of the year
    yearFirstDigits = start[2][:2][::-1]

    return yearFirstDigits


def splitDate(x):

    '''Reverses the current date'''

    year = (x[0] + x[1])[::-1]

    day = x[2][2:][::-1]

    month = x[2][:2][::-1]
    
    newDate = [day, month, year]
   
    return newDate 



def checkPalindrom(x):

    '''Checks to see if the current date is a palidrom date'''

    newDate = splitDate(x)
    
    #If it is a palindrom return True
    if newDate == x:

        return True

    else:

        return False



def advanceDate(x):

    '''Go to the next day'''

    #Specs for 30 day months
    if x[1] == '09' or x[1] == '04' or x[1] =='06' or x[1] == '11':


        if int(x[0]) < 30:

            x[0] = "%02d"%(int(x[0]) + 1)


        elif int(x[0]) == 30:

            x[0] = '01'
            x[1] = "%02d"%(int(x[1]) + 1)

    #Specs for december 31st, ie the last calender year day
    elif x[1] == '12' and x[0] == '31':

        x[1] = '01'
        x[0] = '01'
        x[2] = str(int(x[2]) + 1)

    #Specs for february
    elif x[1] == '02':


        if int(x[0]) < 28:

            x[0] = "%02d"%(int(x[0]) + 1)


        elif int(x[0]) == 28:

            x[0] = '01'
            x[1] = "%02d"%(int(x[1]) + 1)

    #Specs for 31 day months
    else:

        if int(x[0]) < 31:

            x[0] = "%02d"%(int(x[0]) + 1)


        elif int(x[0]) == 31:

            x[0] = '01'
            x[1] = "%02d"%(int(x[1]) + 1)

    return x


def splitInitial(start, end):

    '''Splitting the initial date'''

    table = str.maketrans('/', ' ')

    x = start.translate(table).split()

    y = end.translate(table).split()

    return x, y


def writeToFile(palindromlist):

    '''Create a file and write the list to that file'''

    file = open("Palindromlist.txt", "w+")
    
    for item in range(len(palindromlist)):

        file.write("{}/{}/{}\n".format(palindromlist[item][0],palindromlist[item][1],palindromlist[item][2]))

    file.close()

main()



