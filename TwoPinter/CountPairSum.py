class solution:
    def solve(self,A,B):

        
        p1=1
        p2=len(A)-2
        count=0
        while p1<p2:
            if A[p1]==A[p1-1]:
                p1=p1+1
            
            if A[p2]==A[p2+1]:
                p2=p2-1
                
            if A[p1]+A[p2]>B:
                p2=p2-1
            elif A[p1]+A[p2]<B:
                p1=p1+1
            else:
                count=count+1
                p1=p1+1

        return count

obj= solution()
print(obj.solve([1,2, 3,4, 4,4, 5],5))
