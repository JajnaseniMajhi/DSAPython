import sys
sys.setrecursionlimit(10**6)

class solution:
    def quicksort(self,A,s,e):
        if s>=e:
            return
        pv= self.reArrange(A,s,e)
        self.quicksort(A,s,pv-1)
        self.quicksort(A,pv+1,e)

    
    def reArrange(self,A,s,e):
        l= s+1
        r=e

        while l<=r:
            if A[l]<=A[s]:
                l=l+1
            elif A[r]>A[s]:
                r=r-1

            else:
                temp=A[l]
                A[l]=A[r]
                A[r]=temp
                l=l+1
                r=r-1

        # put A[s] at correct position
        temp=A[l-1]
        A[l-1]=A[s]
        A[s]=temp

        return l-1

    def solve(self,A):
        s=0
        e=len(A)-1
        self.quicksort(A,s,e)
        return A


obj= solution()
print(obj.solve([4,5,7,16,34,23,16,25,3,4,5,1,2]))

