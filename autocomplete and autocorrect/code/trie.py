from node import Node
# the trie
class Trie():

# Constructor
  def __init__(self,words):
    self.startNode=Node("")
    for word in words:
      self.insert(word)
        
# test membership includes substrings of words
# that are not real words
  def isMember(self,string):
    currNode=self.startNode
    if string == "":
        return True
    for letter in string:
      if(not currNode.getNext(letter)):
        return False
      else:
        currNode=currNode.getNext(letter)
    return True

# test if word is a real word (word that was inserted or initialized)
  def isRealWord(self,word):
    if (self.isMember(word)):
      return self.getNode(word).getIsWord()
    else:
      return False
          
  # returns the node searched or an empty node not in the trie
  # containing string "Node Not Found"
  def getNode(self,word):
    if (self.isMember(word)):
      if word == "":
        return self.startNode
      currNode=self.startNode
      counter = 0
      for letter in word:
        currNode=currNode.getNext(letter)
        if (counter == len(word)-1):
            return currNode
        counter = counter + 1
    else:
      return Node("Node Not Found")

  # insert a word into the trie
  def insert(self,word):
    currNode=self.startNode
    self.startNode.incTCounter()
    for char in word:
      prevNode=currNode
      if(not prevNode.getNext(char)):
        currNode=Node(prevNode.getString()+char)
        currNode.setTCounter(1)
        prevNode.setNext(char,currNode)
      else:
        currNode=prevNode.getNext(char)
        currNode.incTCounter()
    currNode.setIsWord(True)
    currNode.incWCounter()
        
  # update frequency of a word if in trie
  # returns true on success / false if word not found
  def setFreqKey(self,word, freq):
    if (self.isMember(word)):
      currNode=self.startNode
      for char in word:
        currNode=currNode.getNext(char)
        currNode.setCounter(currNode.getWCounter() + freq)
      return True
    else:
      return False
      
  def setFreq(self,word,freq):
    if (self.setFreqKey(word, freq)):
      return self.setFreqKey(word[:-1], -1*freq)
    else: 
      return False
      
  
  # return a list of (letter,frequency) tuples [(letter, freq), ...]
  def getFreq(self,word):
    currNode=self.startNode
    freqList = []
    for char in word:
      currNode=currNode.getNext(char)
      freqList.append((currNode.getString(), currNode.getCounter()))
    return freqList
    
