#adds a word to the dictionary with a counter frequency of 10

import os
import trie
import pickle
import sys

if len(sys.argv) == 2:
	#loads current dictionary
    afile=open("trie.pkl", "r")
    dictionary=pickle.load(afile)
    afile.close()
    
    #adds word and sets a favorable frequency
    for x in range(0, 10):
        trie.Trie.insert(dictionary, sys.argv[1])

    #removes old dictionary
    os.remove("trie.pkl")
    #creates new dictionary
    afile=open("trie.pkl", "w")
    pickle.dump(dictionary, afile)
    afile.close()
else:
	print("Error: need proper usage. Proper usage: ./add 'string to add'")

    
