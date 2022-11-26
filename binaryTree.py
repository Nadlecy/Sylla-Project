"""
DD/MM/YYYY
date here

queue data structure implementation (Python)
by drumroll please,,, me! yes it's me again.
"""

class binaryTree():
    def __init__(self,cell,left=None,right=None):
        self.root=cell
        self.left=left
        self.right=right
    
    def rootData(self):
        pass

    def rightBranch(self):
        return self.right

    def leftBranch(self):
        return self.left

    def size(self): #(number of nodes)
        n = 1
        if self.leftBranch() != None:
            n += self.left.size()
        if self.rightBranch() != None:
            n += self.right.size()
        return n

    def height(self): #highest number of downward links from the initial root
        pass

class treeCell():
    def __init__(self,name,data):
        self.name=name
        self.data=data
    
    def cellName(self):
        return self.name

    def cellData(self):
        return self.data


test=binaryTree(treeCell("B1","funy data"),binaryTree(treeCell("B2","funy data"),(binaryTree(treeCell("B4","adada")))),binaryTree(treeCell("B3","funy data")))

hm=test.size()
print(hm)