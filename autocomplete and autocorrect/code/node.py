# trie Node
class Node():

# Constructor for node
  def __init__(self,string):
    self.string=string
    self.edge = {} 
    self.tcounter = 0
    self.wcounter = 0
    self.isWord = False
    
# Get is real word
  def getIsWord(self):
    return self.isWord

# Set is real word
  def setIsWord(self, bool):
    self.isWord = bool

# Get traversal frequency counter for a node
  def getTCounter(self):
    return self.tcounter

# Set traversal frequency counter for a node
  def setTCounter(self, count):
    self.tcounter = count

# Increment traversal frequency counter for a node
  def incTCounter(self):
    self.tcounter += 1

# Get word frequency counter for a node
  def getWCounter(self):
    return self.wcounter

# Set word frequency counter for a node
  def setWCounter(self, count):
    self.wcounter = count

# Increment word frequency counter for a node
  def incWCounter(self):
    self.wcounter += 1
    
# Get string of node
  def getString(self):
    return self.string

# Get edge of node
  def getEdge(self):
    return self.edge

# Set next node
  def setNext(self,char,node):
    self.edge[char]=node

# Get next node
  def getNext(self,char):
    if (char in self.edge):
      return self.edge[char]

# Print trie starting from this node
  def printChildren(self, inclPartials):
    if self.isWord or inclPartials:
      print(self.string, ': tcount(', self.tcounter, ') and wcount(', self.wcounter, ')')
    if self.edge is not None:
      for child in self.edge:
        self.edge[child].printChildren(inclPartials)