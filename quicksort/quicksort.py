from utils import getList,numEle


def quickSort(arr,l,h):
    if len(arr) == 1:
        return arr
    if(l<h):
        # find pivot
        j=partition(arr,l,h)
        quickSort(arr,l,j-1)
        quickSort(arr,j+1,h)

def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)





# get Input to be sorted
arr = getList.getList(numEle.numEle())
quickSort(arr,0,len(arr)-1)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])