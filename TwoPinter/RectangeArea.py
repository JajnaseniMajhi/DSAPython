class solution:
    def solve(self,A,B):
        p1=0
        p2=len(A)-1
        count=0
        mod=1000000007

        while p1<=p2:
            rectArea=A[p1]* A[p2]
            if rectArea<B:
                count=count+2*(p2-p1)+1
                p1=p1+1
            else:
                p2=p2-1
        return count % mod

obj=solution()

print(obj.solve([ 1,2,3,4,5 ],5))

