class solution:
    def merge(self,A,s,m,e):
        T=[None]*(e-s+1)
        p1=s
        p2=m+1
        p3=0
        while p1<=m and p2<=e:
            if A[p1]<A[p2]:
                T[p3]=A[p1]
                p1=p1+1
            # p3=p3+1
            else:
                T[p3]=A[p2]
                p2=p2+1
                # p3=p3+1
            p3=p3+1

        while p1<=m:
            T[p3]=A[p1]
            p3=p3+1
            p1=p1+1
        while p2<=e:
            T[p3]=A[p2]
            p2=p2+1
            p3=p3+1
        p3=0
        for i in range(s,e+1,1):
            A[i]=T[p3]
            p3=p3+1

    def mergesort(self,A,s,e):
        if s==e:
            return
        mid=(s+e)//2
        self.mergesort(A,s,mid)
        self.mergesort(A,mid+1,e)
        self.merge(A,s,mid,e)

    def solve(self,A):
        s=0
        e=len(A)-1
        self.mergesort(A,s,e)
        return A

obj= solution()
print(obj.solve([2,9,1,9,7]))


