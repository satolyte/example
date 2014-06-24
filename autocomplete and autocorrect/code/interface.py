#!/usr/bin/python

from tkinter import *
import re
import autocorrect
import autocomplete
import functools
import pickle

DICT = pickle.load(open("trie.pkl", "rb"))

class MyApp:

    nodeCache = []
    
    def __init__(self, myParent):
        self.myContainer1 = Frame(myParent)
        self.myContainer1.pack()

        self.input = Entry(self.myContainer1)
        self.input.pack()
        self.input.bind("<KeyRelease>", self.keyHit)

        self.output = Entry(self.myContainer1)
        self.output.pack()

        autocorrect.distance("", 1, DICT.startNode, [0], False, self.nodeCache)
        self.nodeCache.append((DICT.startNode.getString(), DICT.startNode.getTCounter, 0))
        
    def keyHit(self, event):
        text = self.input.get()
        strings = re.findall(r"[\w']+", text)
        if len(strings) != 0 and event.keysym != "space":
            # strings = [strings] if len(strings) == 1 else strings
            print(strings[-1], self.nodeCache)
            result, nodes = autocomplete.autocomplete(strings[-1], DICT, self.nodeCache, event.keysym)
            self.nodeCache = nodes
            print(self.nodeCache)
            self.output.delete(0, len(self.output.get()))    
            strings[-1] = result.getString()
            self.output.insert(0, " ".join(strings))
        if event.keysym == "space": 
            self.nodeCache = None

root = Tk()
myapp = MyApp(root)
root.mainloop()
