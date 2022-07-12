from unittest import result


class solution:
    def solve(self,A,B):
        mapSet={}
        result=[]
        for i in range(len(B)):
            if B[i] in mapSet:
                mapSet[B[i]]+=1
            else:
                mapSet[B[i]]=1


        for j in range(len(A)):
            if A[j] in mapSet:
                result.append(A[j])
                mapSet[A[j]]-=1
                if mapSet[A[j]]==0:
                    mapSet.pop(A[j])

        
        return result


obj= solution()
print(obj.solve([1, 2, 2, 1],[2, 3, 1, 2]))