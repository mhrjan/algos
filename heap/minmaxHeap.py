

from utils import getList,numEle

def min_heapify(A,k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] < A[k]:
        smallest = l
    else:
        smallest = k
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != k:
        A[k], A[smallest] = A[smallest], A[k]
        min_heapify(A, smallest)

def max_heapify(B,k):
    l = left(k)
    r = right(k)
    if l < len(B) and B[l] > B[k]:
        largest = l
    else:
        largest = k
    if r < len(B) and B[r] > B[largest]:
        largest = r
    if largest != k:
        B[k], B[largest] = B[largest], B[k]
        max_heapify(B, largest)

def left(k):
    return 2 * k + 1

def right(k):
    return 2 * k + 2

def build_min_max_heap(A,B):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        min_heapify(A,k)
        max_heapify(B,k)

A = getList.getList(numEle.numEle())
B=A.copy()
build_min_max_heap(A,B)
print("min Heap::",A)
print("max Heap::",B)            

