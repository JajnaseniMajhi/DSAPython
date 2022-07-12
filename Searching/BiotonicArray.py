import re
from turtle import right


class solution:
    def findMax(self,A):
        l=0
        r=len(A)-1
        while l<=r:
            mid=(l+r)//2
            if A[mid]>A[mid-1] and A[mid]>A[mid+1]:
                return mid
            elif A[mid]>A[mid+1] and A[mid]<A[mid-1]:
                r=mid-1
            elif A[mid]>A[mid-1] and A[mid]<A[mid+1]:

                l=mid+1

        return mid


    def findLeft(self,A,maxIndex,B):
        #search left
        l=0
        r=maxIndex-1
        while l<=r:
            mid= (l+r)//2
            if A[mid]==B:
                return mid
            elif A[mid]<B:
                l=mid+1
            elif A[mid]>B:
                r= mid-1

        return -1


    def findRight(self,A,maxIndex,B):
        l=maxIndex+1
        r=len(A)-1
        while l<=r:
            mid= (l+r)//2
            if A[mid]==B:
                return mid
            elif A[mid]<B:
                r=mid-1
            elif A[mid]>B:
                l=mid+1
        return -1
    def solve(self,A,B):
        l=0
        r=len(A)-1
        maxIndex= self.findMax(A)
        if A[maxIndex]==B:
            return maxIndex

        leftResult= self.findLeft(A,maxIndex,B)
        if leftResult!=-1:
            return leftResult
        rightResult= self.findRight(A,maxIndex,B)
        if rightResult!=-1:
            return rightResult

        return -1





obj= solution()
print(obj.solve([1,2,4,5,-1,-4],-1))