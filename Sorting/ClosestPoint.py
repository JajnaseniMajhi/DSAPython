import functools
import re


import functools

class solution:

    def compare(self,x,y):
        result1=x[0]* x[0]+x[1]*x[1]
        result2=y[0]* y[0]+ y[1]* y[1]

        if result1>result2:
            return 1
        else:
            return -1


    def solve(self,A,B):
        res=[]
        if len(A)==0:
            return 0

        A=sorted(A,key=functools.cmp_to_key(self.compare))

        for i in range(B):
            res.append(A[i])

        return res

obj= solution()
print(obj.solve([ 
       [1, 3],
       [-2, 2] 
     ],1))


