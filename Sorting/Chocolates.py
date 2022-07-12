from sys import maxsize
import sys


def solve(A,B):
    if B==0 or len(A)==0:
        return 0
    A.sort()
    minDiff= sys.maxsize
    for i in range(len(A)-B+1):
        if minDiff>(A[B+i-1]-A[i]):
            minDiff=A[B+i-1]-A[i]

    return minDiff


print(solve([3, 4, 1, 9, 56, 7, 9, 12],4))