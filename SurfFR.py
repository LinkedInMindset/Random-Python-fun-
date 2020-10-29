#Name: Jonathan Sands
#Date: 10/29/2020
#YouTube: https://www.youtube.com/watch?v=AgtOqlIdQAw
#HonorStatement: I have not given or received any unauthorized assistance on this assignment.

from html.parser import HTMLParser
from urllib.request import urlopen



class LinksParser(HTMLParser):
    
    '''Parser for links'''

    data = list()
    hrefs = list()
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        
    #Filtering bad hyperlinks
    def handle_starttag(self, startTag, attrs):
        
        if startTag != 'a':
            return
        
        #denote the start of an anchor
        if self.recording:
            self.recording += 1
            return
        
        for name, value in attrs:
            
            if value in self.hrefs:
                return

            #If the hyperlink is a pdf we ignore it
            if value[-3:] == 'pdf':
                return

            #if the hyperlink attrs has name href and the link has ('law.depaul.edu' or a '/' then we know it stays on the law webpage)
            elif name =='href' and ('law.depaul.edu' in value or value[0] == '/'):                                                  
                self.hrefs.append(value)                
                break
                
            else:
                return
            
            self.recording = 1
    
    #Denotes the end of a line
    def handle_endtag(self, endTag):
        if endTag == 'a' and self.recording:
            self.recording -= 1
    
    #If recording, append data to list
    def handle_data(self,data):
        if self.recording:
            self.data.append(data)

            
            
class TextParser(HTMLParser):
    
    '''Parser for text'''

    text = list()
    attributes = list()
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.record = True
        
    def handle_starttag(self, startTag, attrs):
        
        #return record = True if we are in one of these three anchors
        if startTag == 'p' or startTag == 'h2' or startTag == 'h3':
            self.record = True
    
    #Denote the end of an anchor
    def handle_endtag(self, endTag):
        if endTag == 'p' or endTag == 'h2' or endTag == 'h3':
            self.recording = False
    
    #if we are in a proper anchor, append the data to the list text
    def handle_data(self, data):
        if self.record == True:            
            self.text.append(data)

        #Filer out text with this registersod word, \r\n, or \n in it as it takes up a lot of room
        for i in range(len(self.text)):
            if 'registersod' in self.text[i] or '\r\n' in self.text[i] or '\n' in self.text[i]:
                self.text.remove(self.text[i])





def surfLinks(url, checked_links):
    
    '''Returns the words with the highest frequency count in the site'''
    
    #Initialize parserobject
    parser = LinksParser()
    
    #open link and read the hrefs in it
    response = urlopen(url)
    html = response.read()
    html = html.decode().lower()
    parser.feed(html)
    
    #iterate over href links
    for link in parser.hrefs:   
        
        #format link and check if it's been scanned
        if link[0] == '/':
            link = 'https://law.depaul.edu'+link
            
            #If it's been scanned, ignore it
            if link in checked_links:
                return

            #Else append the url to the list and check it for its hrefs
            else:
                print(link)
                checked_links.append(link)
                surfLinks(link, checked_links)
                
        #format link and repeat steps above        
        elif ' ' in link:
            
            link = link.replace(' ','%20')
            
            if link in checked_links:
                return
        
            else: 
                print(link)
                checked_links.append(link)
                surfLinks(link, checked_links)
        
        #Link already formated correctly, still repeat other steps from above
        else:
           
            if link in checked_links:
                return
        
            else: 
                print(link)
                checked_links.append(link)
                surfLinks(link, checked_links)
    
    return checked_links



def parse(url):
    
    '''Return a list of words/phrases used in the given url'''
    
    response = urlopen(url)
    html = response.read()
    html = html.decode().lower()
    
    #Initialize textparser
    parser = TextParser()
    parser.feed(html)
    
    #list of words and phrases
    return parser.text



def createWordList(textparser, wordlist):
    
    '''Add all lines from a parser.text list to one global string containing all words from all webpages'''
        
    for line in textparser:
        wordlist += ' '+line
    
    #return a string that we can split() to find all indepented words
    return wordlist


def unique(list1): 
  
    '''find unique words in the list and return those as a list'''

    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 

        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x)
            
    # print list 
    return unique_list



def countWords(wordlist):
    
    '''Add all the total words together'''

    wordfreq = list()
    wordlist = wordlist.split()
    
    #Determine the unique words
    uniqueWords = unique(wordlist)
    
    #For all unique words, grab their word count
    for w in uniqueWords:
        wordfreq.append(wordlist.count(w))
    
    #print the words counts
    print("Pairs\n" + str(list(sorted(zip(uniqueWords, wordfreq)))))


def main():

    '''Main function, takes the url for the law page and returns the word count'''
    
    #Initialize lists
    checked_links = list()
    wordlist = 'l'
    
    url = 'https://law.depaul.edu/about/pages/default.aspx'
    
    #Surf the links
    checked_links = surfLinks(url,checked_links)
    
    #DEMONSTRATIONAL PURPOSES TO SHOW THE WORD COUNTS
    #checked_links = ['https://law.depaul.edu/about/news/pages/croak-community-legal-clinic-three-part-webinar.aspx',
    #                'https://law.depaul.edu/about/news/pages/parentage-under-illinois-law.aspx',
    #                'https://law.depaul.edu/about/news/pages/annual-family-law-symposium-%e2%80%93-the-current-state-of-elder-law.aspx']

    for link in checked_links:
        
        #Parse the link for the text
        parsed = parse(link)
        
        #Append the parsed link's text to the wordlist
        wordlist = createWordList(parsed, wordlist)
    
    #Count words in wordlist
    countWords(wordlist)    

main()