import sys

from pkg_resources import resource_stream
class solution:
    def minimize(self,A,B,C):
        a=len(A)
        b=len(B)
        c=len(C)

        result= sys.maxsize

        p1=0
        p2=0
        p3=0
        resA=0
        resB=0
        resC=0

        while p1<a and p2<b and p3 <c:
            minValue=min(A[p1],min(B[p2],C[p3]))
            maxValue= max(A[p1],max(B[p2],C[p3]))

            if result> maxValue-minValue:
                result= maxValue-minValue
                resA=p1
                resB=p2
                resC=p3
            if result==0:
                break

            if minValue==A[p1]:
                p1=p1+1
            elif minValue==B[p2]:
                p2=p2+1
            elif minValue==C[p3]:
                p3=p3+1

        return min(A[resA],min(B[resB],C[resC]))


obj= solution()
print(obj.minimize([ 1, 4, 5, 8, 10 ],[ 6, 9, 15 ],[ 2, 3, 6, 6 ]))