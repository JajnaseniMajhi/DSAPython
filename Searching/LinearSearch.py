import re


def solve(A,k):
    for i in range(len(A)):
        if A[i]==k:
            return i
    
        if A[i]>k:
            if i==0:
                return 0
            else:
                return i-1

    return  len(A)


print(solve([3,4,5,7,9,12],14))
