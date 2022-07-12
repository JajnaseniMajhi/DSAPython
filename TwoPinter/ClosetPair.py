import sys


class solution:
    def solve(self,A,B,C):
        p1=0
        m= len(A)
        n=len(B)
        p2= n-1
        result=[]
        diff=sys.maxsize
        rl=0
        rr=0
        while p1<m and p2>=0:
            if diff > abs(A[p1]+B[p2]-C):
                diff= abs(A[p1]+B[p2]-C)
                rl=p1
                rr=p2
            elif abs(A[p1]+B[p2]-C)==diff:
                if p1<rl:
                    rl=p1
                    rr=p2
                    diff= abs(A[p1]+B[p2]-C)
                elif p1==rl and p2<rr:
                    rr=p2
                    rl=p1
                    diff=abs(A[p1]+B[p2]-C)
           
            if A[p1]+B[p2]>C:
                p2=p2-1
            else:
                p1=p1+1
            
        result.append(A[rl])
        result.append(B[rr])
        return result

obj= solution()
print(obj.solve( [ 5, 10, 20 ],[ 1, 2, 30 ],13))



            
