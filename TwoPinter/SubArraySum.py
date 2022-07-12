from cgitb import reset
from operator import truediv
from unittest import result


class solution:
  def solve(self,A,B):
        p1=0
        p2=0
        n=len(A)
        sum=0
        result=[]
        while p2<n and p1<n:
            if sum<B:
                sum=sum+A[p2]
                p2=p2+1

            if sum>B:
                sum=sum-A[p1]
                p1=p1+1

            
            if sum==B:
                return A[p1:p2]
        return [-1]

        # n = len(A)
        # l, r = 0, 0
        # sub_sum = 0
        # while r < n and l < n:
        #     if sub_sum < B:
        #         sub_sum += A[r]
        #         r += 1
        #     if sub_sum > B:
        #         sub_sum -= A[l]
        #         l += 1
        #     if sub_sum == B:
        #         return A[l:r]

        # return [-1]

obj= solution()
print(obj.solve( [  1, 1000000000  ],1000000000))