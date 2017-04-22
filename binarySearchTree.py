#!/usr/bin/env python

tree = [[]]
#parent = 20
class Node:
    def __init__(self,parent,left,right):
        self.right = []
        self.left = []
        self.parent = parent
        
    def insertNode(self, parent,value):
        if value <parent:
            self.left.append(value)
        else:
            self.right.append(value)

    def removeNode(self, parent,value):
        if value<parent:
            self.left.pop(value)
        else:
            self.right.pop(value)

right = [30,40,50]
left = [10,20,25]
#tree = [parent.append(right)[parent.append(left)]]
node1 = Node(40,left,right)
node1.insertNode(30,27)
print node1.left



        

    
    
