class binarySearch:
    def bsearch(self,A,B):
        l= 0
        r=len(A)-1
        result=-1

        while(l<=r):
            mid= (l+r)//2
            if A[mid]==B:
                return mid
            elif A[mid]<B:
                l=mid+1
                result=mid
            elif A[mid]>B:
                result=mid
                r=mid-1

        return result

obj= binarySearch()
print(obj.bsearch([3,5,6,7,8,9,14],11))

            
