

## We will implement method for LCS
def longestSubsequence(arr1,arr2):
    m=len(arr1)
    n=len(arr2)
    # Let's create a matrix
    matrix = [[0 for i in range(n+1)]for j in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if(arr1[i-1]==arr2[j-1]):
                matrix[i][j] = matrix[i-1][j-1]+1
            else:
                matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])
    return matrix[m][n]
## Lets take two arrays




array1 = ['A','B','C','F','G']
array2 = ['L','J','G','F','C','D','A','B']
array3 = ['P','M','L','G','D','A','B']
print(longestSubsequence(array1,array2))
print(longestSubsequence(array2,array3))

