def bubbleSort(someArray):
    n = len(someArray)

    for i in range(n):
        for j in range(0,n-i-1):
            if someArray[j] > someArray[j+1]:
                someArray[j], someArray[j+1] = someArray[j+1],someArray[j]

testArr = [64,34,25,12,22,11,90]

bubbleSort(testArr)

print("Array sorted is:")
for i in range(len(testArr)):
    print("%d" %testArr[i])
