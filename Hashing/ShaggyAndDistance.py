import sys
class solution:
    def solve(self,A):
        size= len(A)
        mapList={}
        result=sys.maxsize
        for i in range(size):
            if A[i] in mapList:
                diff=abs(i-mapList.get(A[i]))
                result= min(result,diff)
                mapList[A[i]]=i

            else:
                mapList[A[i]]=i

        return result

obj=solution()
print(obj.solve([7, 1, 3, 4, 1, 7]))


        