#Scraper

import re
import trie
import pickle


def scrape (file): 
    f = open(file, 'r')
    strings=f.read()
    return re.findall('[a-z]+', strings.lower())
    
'''
The following code was used for experimentation

def words(text): 
    print(re.findall('[a-z]+', text.lower()))
    return re.findall('[a-z]+', text.lower()
    '''
        
def add_all(strings):
    t = trie.Trie(strings)
    return t
    

DICT = add_all(scrape("big.txt"))



#saves the dictionary in a file called DICT.pkl

afile=open("trie.pkl", "wb")
pickle.dump(DICT, afile, 2)
afile.close()

#uncomment for testing purposes
'''
def print_tests ():
    print("Prints whether 'this' 'computer' and 'bigbird' are part of DICT")
    print(trie.Trie.isRealWord(DICT, "hi"))
    print(trie.Trie.isRealWord(DICT, "this"))
    print(trie.Trie.isRealWord(DICT, "computer"))
    print(trie.Trie.isRealWord(DICT, "bigbird"))
    print("The word 'bigbird' is not in the dictionary. Calling insert on 'bigbird'...\n")
    trie.Trie.insert(DICT, "bigbird")
    print(trie.Trie.isRealWord(DICT, "bigbird"))
    

#print_tests()
'''