import sys


class solution:
    def solve(self,A,B):
        l=sys.maxsize
        r=~sys.maxsize
        for i in range(len(A)):
            l=min(l,A[i])
            r=max(r,A[i])
        result=-1
        while l<=r:
            mid=(l+r)//2

            count= self.count(A,mid)
            if count<B:
                l= mid+1
            
            else:
                r=mid-1
                result=mid

        return result
            
    def count(self,A,mid):
        count=0
        for i in range(len(A)):
            if A[i]<=mid:
                count=count+1
        return count

obj= solution()
print(obj.solve([1, 4, 5, 3, 19, 3],3))