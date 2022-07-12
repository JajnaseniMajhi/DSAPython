class solution:
    def seach(self,A,B):
        rows=len(A)
        cols=len(A[0])

        for i in range(rows):
            if A[i][cols-1]==B:
                return 1

            elif A[i][cols-1]>B:
                #bsearch
              result=  self.bSearch(A[i],i,cols,B)
              if result!=-1:
                  return 1
        return -1

    
    def bSearch(self,rowA,row,cols,B):
        l=0
        r=cols-1
        while l<=r:
            mid=(l+r)//2
            if rowA[mid]==B:
                return 1
            elif rowA[mid]<B:
                l=mid+1
            elif rowA[mid]>B:
                r=mid-1

        return -1


obj=solution()
print(obj.seach([ 
      [1, 3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]  
    ],58))