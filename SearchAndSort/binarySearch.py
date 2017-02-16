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

def IterativeBinarySearch(arr, left, right, x):
    while left <= right:
        middle = left + (right - left)//2

        if arr[middle] == x:
            return middle
        elif arr[middle] < x:
            left = middle + 1
        else:
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
