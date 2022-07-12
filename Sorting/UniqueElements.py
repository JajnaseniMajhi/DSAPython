def solve(A):
    A=sorted(A)

    count=0
    for i in range(len(A)-1):
        if A[i]>=A[i+1]:
            count=count+ A[i]-A[i+1]+1
            A[i+1]=A[i+1]+A[i]-A[i+1]+1


    return count


print(solve([2, 4,4,4, 5]))