import sys

class solution:
    def solve(self,A,B):
        A.sort()
        l=self.findMin(A)
        r=A[len(A)-1]-A[0]
        return self.findMAxDistance(A,l,r,B)

    def findMAxDistance(self,A,l,r,B):
        ans=l
        while l<=r:
            mid=(l+r)//2
            if self.checkifPossible(mid,B,A):
                l=mid+1
                ans=mid
            else:
                r=mid-1

        return ans

    # def findMax(self,A):
    #     maximim=~sys.maxsize
    #     for i in range(len(A)):
    #         if maximim<A[i]:
    #             maximim=A[i]


    #     return maximim

    
    def findMin(self,A):
        min=sys.maxsize
        for i in range(len(A)-1):
            if min>A[i+1]-A[i]:
                min=A[i+1]-A[i]

        return min

    def checkifPossible(self,mid,B,A):
        lastPlaced=A[0]
        count=1
        for i in range(1,len(A)):
            if A[i]-lastPlaced>=mid:
                lastPlaced=A[i]
                count=count+1
            if count==B:
                return True

        return False
        



obj=solution()
print(obj.solve([ 5, 17, 100, 11 ],2))

