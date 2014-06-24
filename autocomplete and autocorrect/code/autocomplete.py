#!/usr/bin/python

import sys
import trie
import node
import autocorrect

maxDistance = 1

# given a root node, finds the most probable (by language model) descendant
def descendant(root):
    tempCandidate = None
    
    if root.getEdge():
        for child in root.getEdge():
            d = descendant(root.edge[child])
            if tempCandidate is not None:
                tempCandidate = d if d.getWCounter() > tempCandidate.getWCounter() else tempCandidate
            else:
                tempCandidate = d
        if root.getIsWord() and root.getWCounter() > tempCandidate.getWCounter():
            tempCandidate = root
    else:
        tempCandidate = root if root.getIsWord() else None
    return tempCandidate

# given a root node, returns 
def childrenAtDepth(root, depth, lst):
    if depth == 0:
        lst.append(root)
    else:
        for nextLetter in root.edge:
            childrenAtDepth(root.edge[nextLetter], depth - 1, lst)

def updateNodes(query, trieDict, nodeCache, newChar):
    newNodes = []

    # for each previous active node, if edit distance + 1 is <= max distance, add to new nodes
    for node in nodeCache:
        n = trieDict.getNode(node[0])
        if node[2] + 1 <= maxDistance:
            newNodes.append((node[0], node[1], node[2]+1))
        # for each child of the node, if the associated character is different from the entered character,
        # and edit distance (of parent) + 1 <= max distance, also add to new nodes
        for nextLetter in n.edge:
            m = n.edge[nextLetter]
            if nextLetter != newChar:
                if node[2] + 1 <= maxDistance:
                    newNodes.append((m.getString(), m.getTCounter(), node[2]+1))
                    print(m.getString(), m.getTCounter(), node[2]+1)
            # if the associated character is the same, and edit distance (of parent) <= max distance, add to new nodes
            # also go through all its children to a depth of (maxDistance - parent's edit distance) and add these
            else:
                if node[2] <= maxDistance:
                    newNodes.append((m.getString(), m.getTCounter(), node[2]))
                    depth = maxDistance - node[2]
                    for i in range(1, depth + 1):
                        children = []
                        childrenAtDepth(m, i, children)
                        if len(children) != 0:
                            for child in children:
                                newNodes.append((child.getString(), child.getTCounter(), node[2] + i))
    return newNodes

# given a partial word query and a trie-based dictionary, returns the most probable node associated
# with a complete word using fuzzy search
def autocomplete(query, trieDict, nodeCache = None, newChar = ""):
    activeNodes = []
    activeDescendants = []
    lastRow = list(range(len(query) + 1))
    # if no active nodes cached, create list of active nodes within given distance
    # else update nodes
    if nodeCache is None or nodeCache == []:
        autocorrect.distance(query, maxDistance, trieDict.startNode, lastRow, False, activeNodes)
        activeNodes.append((trieDict.startNode.getString(), trieDict.startNode.getTCounter, 0))
    else:
        activeNodes = updateNodes(query, trieDict, nodeCache, newChar)
    if len(activeNodes) is not 0:
        # for each active node, find the descendant of each node
        for node in activeNodes:
            activeDescendants.append((descendant(trieDict.getNode(node[0])), node[2]))
        # sort by probability of each descendant divided by edit distance of its associated active node + 1; rough error model
        sactiveDescendants = sorted(activeDescendants, key = lambda x: x[0].getWCounter() / (x[1] + 1))
        return (sactiveDescendants[-1][0], activeNodes)
    else:
        return trieDict.startNode, None
        print("No suggestions.")

