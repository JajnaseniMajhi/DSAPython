import sys
from unittest import result
class solution:
    def solve(self,A,B,C):
        max=~sys.maxsize
        for i in range(len(C)):
            if C[i]> max:
                max=C[i]

        sum=0
        for i in range(len(C)):
            sum+=C[i]

        l=max *B
        r= sum *B
        result=0
        while l<=r:
            mid= (l+r)//2
            if self.getPaintersCount(C,A,mid,B)<=A:
                result=mid
                r= mid
            else:
                l= mid+1
        return l %10000003





    def getPaintersCount(self,C,A,mid,B):
        count=1
        total=0
        for i in range(len(C)):
            total= total+C[i] *B
            if total>=mid:
                count=count+1
                total=C[i]*B

        return count

obj= solution()
print(obj.solve(2,5,[1,10]))