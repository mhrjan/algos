def linearSearch(arr,n,x):
    for i in range(n):
        if(arr[i]==x):
            return i
    return -1
x = int(input("Enter number of elements: "))
list1 = list(map(int,input("\nEnter the numbers: ").strip().split()))[:x]
key=int(input("\nPlease enter key to search for index"))
n=len(list1)
res=linearSearch(list1,n,key)
if(res==-1):
    print("Element not found")
else:
    print("element fournd at index:",res)