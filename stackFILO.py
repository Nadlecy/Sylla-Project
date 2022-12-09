"""
DD/MM/YYYY
25/11/2022

stack data structure implementation (Python)
by, well uhhh me i did that :]
"""

class stack():
    def __init__(self, name, top = None):
        self.name = name
        self.top = top
    
    def depile(self):
        a = self.top
        self.top = self.top.next
        return a
    
    def pile(self,newCell):
        newCell.next = self.top
        self.top=newCell
    
    def top(self):
        return self.top
        

class stackCell():
    def __init__(self,name,data,nextCell = None):
        self.name = name
        self.data = data
        self.next = nextCell
        
    def cellName(self):
        return self.name
    
    def cellData(self):
        return self.data