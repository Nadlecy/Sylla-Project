"""
DD/MM/YYYY
28/11/2022

stack+queue data structure implementation (Python)
by ya boy yea tis me again wooo
"""

class queuestack():
    def __init__(self,name,front=None,end=None):
        self.name=name
        self.front=front
        self.end=end
    
    def thread(self,newCell):
        if self.front == None:
            self.front = newCell
            self.end = newCell
        else :
            self.end.nextCell = newCell
            self.end = newCell
    
    def frontRemove(self):
        a = self.front
        if self.end == self.front:  #if this assertion ever applies
            self.end = self.front.nextCell #self.end will always just become None
        self.front = self.front.nextCell
        return a #this also returns the cell you remove if you wanna use it for something else
    
    def endRemove(self):
        a = self.end
        if self.end == self.front:
            self.front = self.end.previous 
        self.end = self.end.previous
        return a #this also returns the cell you remove if you wanna use it for something else

    def front(self):
        return self.front

    def end(self):
        return self.end

class queuestackCell():
    def __init__(self,name,data,previous=None,next=None):
        self.name=name
        self.data=data
        self.next=next
        self.previous=previous
    
    def cellName(self):
        return self.name
    
    def cellData(self):
        return self.data
