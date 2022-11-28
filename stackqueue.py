"""
DD/MM/YYYY
28/11/2022

stack+queue data structure implementation (Python)
by ya boy yea tis me again wooo
"""

class staqueue():
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
    
    def frontName(self):
        return self.front.name

    def frontData(self):
        return self.front.data

    def endName(self):
        return self.end.name

    def endData(self):
        return self.end.data

class staqueueCell():
    def __init__(self,name,data,next=None):
        self.name=name
        self.data=data
        self.next=next
