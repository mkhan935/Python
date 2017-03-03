#must go over in a week
#simple review of insertionSort
def insertionSort(arrToPassIn):
    for i in range(1, len(arrToPassIn)):
        key = arrToPassIn[i]

        j=i-1
        while j>=0 and key <arrToPassIn[j]:
            arrToPassIn[j+1]=arrToPassIn[j]
            j-=1
        arrToPassIn[j+1]=key


testArr = [12,11,13,5,6]
insertionSort(testArr)
print("sorted array: ")
for item in range(len(testArr)):
    print(testArr[item])
