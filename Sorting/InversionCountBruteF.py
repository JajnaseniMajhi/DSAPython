from unittest import result


def solve(A):
    count=0
    result=[]
    for i in range(len(A)-1):
        for j in range(i+1,len(A),1):
            if A[i]>A[j]:
                count=count+1

    return count


print(solve([3,2,1]))
