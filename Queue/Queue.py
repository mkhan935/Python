class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self,item):
        self.items.insert(0,item) #beginning of q

    def dequeue(self):
        return self.items.pop() #pop the first thing that entered


myObj = Queue()
myObj.enqueue(10) #int
myObj.enqueue('Python rules C# drools') #string
myObj.enqueue(True) #bool
print(myObj.size())
print(myObj.dequeue()) #int
print(myObj.dequeue()) #String
print(myObj.dequeue()) #bool
