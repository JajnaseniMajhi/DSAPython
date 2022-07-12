from unittest import result


class solution:
    def threeSum(self,A):
        A.sort()
        n=len(A)
        result=[]

        for i in range(n-2):
            if i>0 and A[i]==A[i-1]:
                continue
            p1=i+1
            p2=n-1
            while p1<p2:
                sum=A[p1]+A[p2]

                if sum>-A[i]:
                    p2=p2-1
                    
                elif sum<-A[i]:
                    p1=p1+1

                else:
                    triplet=[]
                    triplet.append(A[i])
                    triplet.append(A[p1])
                    triplet.append(A[p2])
                    result.append(triplet)
                    p1=p1+1
                    while p1<p2 and  A[p1]==A[p1-1]:
                        p1=p1+1

        
        return result


obj=solution()
print(obj.threeSum([-1,0,1,2,-1,4]))