#recursive in python

def binarySearch(arr, left, right, x):
    if right >= left:
        middle = left + (right -1)//2 #python 3 / creates a float, // creates int
        if arr[middle] == x:
            return middle
        elif arr[middle] > x:
            return binarySearch(arr,left,middle-1,x)
        else:
            return binarySearch(arr,middle+1,right,x)
    else:
        return -1

def IterativeBinarySearch(arr, left, right, x): #this is my Review of IterativeSearch
    while left <= right: #while there is a left side of the array thats < = to the right
        middle = left + (right - left)//2 #create a middle

        if arr[middle] == x:  #check if middle == x
            return middle
        elif arr[middle] < x:  #if middle is < x than that means x is between middle+1 and right
            left = middle + 1
        else:                    #if middle is > x than that means x is between left and middle
            right = middle + 1
    return -1

testArr = [ 1, 2, 5, 15, 26 ]
x=15
y=2
results = binarySearch(testArr,0,len(testArr)-1,x)
Iresults = IterativeBinarySearch(testArr,0, len(testArr)-1,y)
if results != -1:
    print ("Element is at index: %d " % results)
else:
    print ("Element does not exist in array")
if Iresults != -1:
    print("Element is at index: %d " % Iresults)
else:
    print("Element does not exist in array")
