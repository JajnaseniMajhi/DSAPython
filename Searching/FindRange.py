from unittest import result


class solution:
    def searchRange(self,A,B):
        l=0
        r=len(A)-1
        result=[]
        result.append(self.searchLeftIndex(A,B,l,r))
        result.append(self.searchRightIndex(A,B,l,r))
        return result

    
    def searchLeftIndex(self,A,B,l,r):
        result=-1
        while l<=r:
            mid=(l+r)//2
            if A[mid]==B:
                result=mid
                r=mid-1
            elif A[mid]<B:
                l=mid+1
            elif A[mid]>B:
                r=mid-1

        return result

    def searchRightIndex(self,A,B,l,r):
        result=-1
        while l<=r:
            mid=(l+r)//2
            if A[mid]==B:
                result=mid
                l=mid+1
            elif A[mid]<B:
                l=mid+1
            elif A[mid]>B:
                r=mid-1

        return result
                


obj=solution()
print(obj.searchRange([5, 7, 7, 8, 8, 10],21))
