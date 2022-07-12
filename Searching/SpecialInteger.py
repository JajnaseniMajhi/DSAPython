from cgitb import reset
from operator import truediv


class solution:
    def solve(self,A,B):
        l=1
        r=len(A)
        result=0
        while l<=r:
            mid=(l+r)//2
            #check this window
            if self.checkForWindowSize(A,B,mid):
                l= mid+1
                result=mid

            else:
                r=mid-1

        return result
    
    def checkForWindowSize(self,A,B,K):
        subArraySum=0
        for i in range(K):
            subArraySum=subArraySum+A[i]
        
        if subArraySum>B:
            return False

        for j in range(K,len(A)):
            subArraySum=subArraySum-A[j-K]
            subArraySum=subArraySum+A[j]
            if subArraySum>B:
                return False
        return True

obj= solution()
print(obj.solve([1, 2, 3, 4, 5],10))