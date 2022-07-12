from multiprocessing import cpu_count


class solution:
    def solve(self,A,B):
        p1=0
        p2=1
        count=0
        A.sort()
        while p1 <p2 and p2<len(A):
            diff= A[p2]-A[p1]
            if diff==B:
                count=count+1
                p1=p1+1
                p2=p2+1
                while p1<p2 and p1>0 and A[p1]==A[p1-1]:
                    p1=p1+1
                while p2< len(A) and A[p2]==A[p2-1]:
                    p2=p2+1
            elif diff>B:
                p1=p1+1
                if p1==p2:
                    p2=p2+1
            elif diff<B:
                p2=p2+1
        return count

obj=solution()

print(obj.solve([1, 2],0))
