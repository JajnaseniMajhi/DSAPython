class solution:
    def solve(self,A):
        pfs= set()
        pfsum=0
        for i in range(len(A)):
            pfsum= pfsum+A[i]
            if pfsum==0 or pfs.__contains__(pfsum):
                return 1
            else:
                pfs.add(pfsum)

        return 0


obj= solution()
print(obj.solve([1,2,-2]))
