#!/usr/bin/python

import sys
import autocomplete
import pickle

if len(sys.argv) == 2:
    afile=open("trie.pkl", "rb")
    dictionary=pickle.load(afile)
    afile.close()
    result, nodes = autocomplete.autocomplete(sys.argv[1],dictionary)
    print(result.getString())
else:
	print("Error: need proper usage. Proper usage: ./acomplete 'string to complete'")
