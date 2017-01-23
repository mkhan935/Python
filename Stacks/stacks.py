#This is just a review on stacks in Python.
class Stack:
    def __init__(self):
        self.list=[] #as soon as the stack object is made, it has a list

    def IsEmpty(self):
         #print( self.items==[])  this is just to check if it is working properly.
         #returns false  if stack is not empty, true otherwise
         self.list == []

        #push take args ItemToPush
    def push(self,itemToPush): #takes the stack and pushes the item into the stack
        self.list.append(itemToPush)

    def pop(self):
        #pop the last value/the value on top
        return  self.list.pop()

    def size(self):  #len of list is returned
        return len(self.list)

    def printTheStack(self):  #prints the stack from top to bottom, as we are adding and pushing down
        for things in reversed(self.list):
            print(things)


theStack=Stack()
print(theStack.IsEmpty())

theStack.push("Apples")
theStack.push("WaterMelons")
print(theStack.size())
print()#blank line

theStack.printTheStack()

theStack.pop()
print()#blank line

theStack.printTheStack()