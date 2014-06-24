#!/usr/bin/python

import sys
import autocorrect
import pickle

if len(sys.argv) == 2:
    afile=open("trie.pkl", "rb")
    dictionary=pickle.load(afile)
    afile.close()
    print(autocorrect.autocorrect(sys.argv[1],dictionary))
else:
	print("Error: need proper usage. Proper usage: ./acorrect.py 'string to correct'")
