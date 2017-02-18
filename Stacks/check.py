'''
So this program is to just implement a simple
checker using stacks in python
reviewed
'''

#first I will make the stack

class Stack:
    def __init__(self):
        self.theStack = []
    def isEmpty(self):
        return self.theStack == []
    def push(self,objectToPush):
        self.theStack.append(objectToPush)
    def pop(self):
        return self.theStack.pop()
    def peek(self):
        return self.theStack[len(self.theStack)-1]
    def size(self):
        return len(self.theStack)

#simple stuff, just an avg stack lol
#now lets right the program
#purpise of this checker is to just check if the number of () are balanced
#balnced meaning for every ( there is a )
def parChecker(stringToCheck):
    s = Stack()
    balanced = True
    index = 0
    while index < len(stringToCheck) and balanced:
        symbol = stringToCheck[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('((()))'))

print(parChecker('(()'))
