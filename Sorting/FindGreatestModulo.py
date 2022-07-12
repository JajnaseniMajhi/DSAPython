class solution:
    def merge(self,A,s,mid,e):
        p1=s
        p2=mid+1
        p3=0
        T=[None]*(e-s+1)

        while p1<=mid and p2<=e:
            if A[p1]<A[p2]:
                T[p3]=A[p1]
                p1=p1+1
            else:
                T[p3]=A[p2]
                p2=p2+1
            p3=p3+1

        while p1<=mid:
            T[p3]=A[p1]
            p3=p3+1
            p1=p1+1

        while p2<=e:
            T[p3]=A[p2]
            p3=p3+1
            p2=p2+1
        p3=0
        for i in range(s,e+1,1):
            A[i]=T[p3]
            p3=p3+1


    def mergeSort(self,A,s,e):
        if s==e:
            return
        mid= (s+e)//2
        self.mergeSort(A,s,mid)
        self.mergeSort(A,mid+1,e)
        self.merge(A,s,mid,e)

    def solve(self,A):
        s=0
        e=len(A)-1
        A=list(A)
        self.mergeSort(A,s,e)
        # Find greated modulo
        lastEle= A[e]
        for i in range(e-1,-1,-1):
            if lastEle>A[i]:
                return A[i]% lastEle

        return 0

obj= solution()
print(obj.solve([9,9,9,9,9]))

