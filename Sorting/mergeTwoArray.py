class solution:
    def solve(self,A,B):
        m= len(A)
        n=len(B)
        C=[None]*(m+n)
        p1=0
        p2=0
        p3=0
        while p1<m and p2<n:
            if A[p1]<B[p2]:
                C[p3]=A[p1]
                p3=p3+1
                p1=p1+1
            else:
                C[p3]=B[p2]
                p3=p3+1
                p2=p2+1

        while p1<m:
            C[p3]=A[p1]
            p3=p3+1
            p1=p1+1

        while p2<n:
            C[p3]=B[p2]
            p3=p3+1
            p2=p2+1

        return C

obj= solution()
print(obj.solve([-1,1,2,4],[2,3,6],))
