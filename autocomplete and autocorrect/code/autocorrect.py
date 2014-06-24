#!/usr/bin/python

import sys
import trie
import node

maxDistance = 2

# traverses trie and calculates distance on each word
# appends a list of tuples (words/prefixes within given distance,
# their probability, and edit distance) to given list
def distance(userWord, dist, rootNode, lastRow, isWholeWord, returnList):
    for nextLetter in rootNode.edge:
        currentRow = [None] * (len(userWord) + 1)
	# if at currentRow[0], initialize value as lastRow[0] + 1
        currentRow[0] = lastRow[0] + 1
        trieWord = rootNode.edge[nextLetter].getString()
	# for each letter in userWord, letter j, go to currentRow[j]
        for i in range(1, (len(userWord) + 1)):
            if userWord[i - 1] == nextLetter:
                cost = 0
            else: cost = 1
	    # currentRow[i] = min of (box to left + 1, box above + 1, 
		# and box to top diagonal left + cost)
            currentRow[i] = min((currentRow[i-1] + 1), (lastRow[i] + 1), (lastRow[i-1] + cost))
        # if is word OR the function caller is not looking for whole words, append
        if rootNode.edge[nextLetter].getIsWord() or (not isWholeWord): 
            if currentRow[-1] <= dist:
                counter=rootNode.edge[nextLetter].getWCounter()
                #Baye's theorem: multiply the counter by a form of the reciprocal of the edit distance
                probability=counter*(1/(1+currentRow[-1]))
                returnList.append((trieWord, counter, currentRow[-1], probability))
        # get new trie. IF NEXT NODE EXISTS
        newTrie = rootNode.edge[nextLetter]
        # recursively run function again. IF NEXT NODE EXISTS
        distance(userWord, dist, newTrie, currentRow, isWholeWord, returnList)

# calculates most probable word out of words within given distance
# fed a (word, counter) list
# returns word
def mostProbable(returnList):
  sortedList = sorted(returnList, key=lambda x: x[3], reverse=True)
  if sortedList:
      return sortedList[0][0]
  else:
      return ""

# compiler function - autocorrect
def autocorrect(query, trieDict):
    returnList = []

    # initialize first row, from 0 to len(userWord)
    lastRow = list(range(len(query) + 1))
    distance(query, maxDistance, trieDict.startNode, lastRow, True, returnList)
    return mostProbable(returnList)


