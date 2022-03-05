import math

def binary(arr,l,h,x):
    if(h>=l):
        mid = (h+l)//2
        if arr[mid]==x:
            return mid
        elif x<arr[mid]:
            return binary(arr,l,mid-1,x)
        elif x>arr[mid]:
            return binary(arr,mid+1,h,x)
    else:
        return -1


x = int(input("Enter number of elements: "))
arr = list(map(int,input("\nEnter the numbers: ").strip().split()))[:x]
key=int(input("\nPlease enter key to search for index"))
h=len(arr)-1
res=binary(arr,0,h,key)
if(res==-1):
    print("Element not found")
else:
    print("element fournd at index:",res)