'''
Going over creating classes and Objects in Python.
I'm glad I took the time to learn this language
mainly because the ease of use in wrting classes
'''

class myInfo:

    #the self. in python is like this in java
    def __init__(self, name, goalInLife, age):
        self.name=name
        self.goalInLife=goalInLife
        self.age=age

programmer=myInfo('Mohammed','too Much to write',22)

#now you've created an Object
#same thing as Java, TADAAAAAH! Hope this helps someone
print(programmer.name)
print(programmer.goalInLife)
print(programmer.age)
