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

testArr = [ 1, 2, 5, 15, 26 ]
x=15
results = binarySearch(testArr,0,len(testArr)-1,x)

if results != -1:
    print ("Element is at index: %d " % results)
else:
    print ("Element does not exist in array")
