# Python program for implementation of Quicksort
#gotta come back and review this, this weekend
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def divideItUp(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low , high):

        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )


# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quick(arr,low,high):
    if low < high:

        # positioni is partitioning index, arr[p] is now
        # at right place
        positioni = divideItUp(arr,low,high)

        # Separately sort elements before
        # partition and after partition
        quick(arr, low, positioni-1)
        quick(arr, positioni+1, high)

# Driver code to test above
Testarr = [123,32,43,1,3,56,4]
n = len(Testarr)
quick(Testarr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %Testarr[i]),
