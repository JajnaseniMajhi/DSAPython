from operator import length_hint
from re import sub
from unittest import result


class solution:
    def solve(self,A):
        substr={}
        result=0
        if len(A)==1:
            return 1

        A=list(A)
        startIndex=0
        for i in range(len(A)):
            if A[i] in substr:
                startIndex=max(startIndex, substr[A[i]]+1)
            result= max(result,i-startIndex+1)
            
            substr[A[i]]=i

        return result
obj= solution()

print(obj.solve("dadbc"))