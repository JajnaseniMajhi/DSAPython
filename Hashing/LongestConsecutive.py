from itertools import count
from unittest import result


class solution:
    def longestConsecutive(self,A):
        tempSet= set()
        result=0
        for i in range(len(A)):
            if A[i] not in tempSet:
                tempSet.add(A[i])
        
        for j in range(len(A)):
            if A[j]-1 in tempSet:
                continue
            else:
                count=1
                val=A[j]+1
                while val in tempSet:
                    count=count+1
                    val= val+1
                result= max(count,result) 
        return result

obj= solution()
print(obj.longestConsecutive([100, 4, 200, 1, 3, 2]))  