def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

myTest = []
for value in range(10):
    myTest.append(value)

print(search(myTest,5)) 
