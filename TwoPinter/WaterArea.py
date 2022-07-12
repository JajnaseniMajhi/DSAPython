from unittest import result


class solution:
    def maxArea(self,A):
        p1=0
        p2=len(A)-1
        result=0
        while p1<p2:
            result=max(result,min(A[p1],A[p2]) * (p2-p1))

            if A[p1]<A[p2]:
                p1=p1+1
            elif A[p1]>A[p2]:
                p2=p2-1

            elif A[p1]==A[p2]:
                p1=p1+1

        return result

obj= solution()
print(obj.maxArea([1]))


           