from operator import le


class solution:
    
    def bSearch(self,A,B):
        l=0
        r=len(A)-1
        while l<=r:
            mid=(l+r)//2
            if A[mid]==B:
                return mid
            elif A[mid]>A[l]:
                if A[mid]>B>=A[l]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if  A[mid]<B<=A[r]:
                    l= mid+1
                else:
                    r=mid-1


        return -1

    def search(self,A,B):
        return self.bSearch(A,B)
        

obj= solution()
print(obj.search([4,5,6,7,1,2,3,4],3))



    
