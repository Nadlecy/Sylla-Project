"""
DD/MM/YYYY
25/11/2022

queue data structure implementation (Python)
by me again yes *I* did *ALL* of it
"""

class queue():
    def __init__(self, name, front=None, end=None):
        self.name = name
        self.front= front
        self.end = end
    
    def scroll(self):
        a = self.front
        if self.end == self.front:  #if this assertion ever applies
            self.end = self.front.nextCell #self.end will always just become None
        self.front = self.front.nextCell
        return a

    def thread(self,newCell):
        if self.front == None:
            self.front = newCell
            self.end = newCell
        else :
            self.end.nextCell = newCell
            self.end = newCell
    
    def frontName(self):
        return self.front.name

    def frontData(self):
        return self.front.data

class queueCell():
    def __init__(self,name,data,nextCell = None):
        self.name = name
        self.data = data
        self.next = nextCell