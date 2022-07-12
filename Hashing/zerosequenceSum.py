import sys
from tracemalloc import start
from unittest import result
class solution:
    def solve(self,A):
        n = len(A)
        counter = {0: -1}
        total = 0
        maxLen = 0
        idx = -1
        for i in range(n):
            total += A[i]
            if total in counter:
                startIdx = counter[total] + 1
                endIdx = i
                if (endIdx-startIdx+1) > maxLen:
                    maxLen = endIdx-startIdx+1
                    idx = startIdx
            else:
                counter[total] = i

        return [] if idx == -1 else A[idx:idx+maxLen]

       


obj= solution()
print(obj.solve([ 1, 2, -2, 4, -4 ]))



