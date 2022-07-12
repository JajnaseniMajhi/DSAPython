from cgitb import reset
from unittest import result


class solution:
    def solve(self,A,B):
        subArray1={}
        result=[]
        for i in range(len(B)):
            j= B[i][0]
            while j<=B[i][1]:
                if A[j] in subArray1:
                    subArray1[A[j]]+=1

                else:
                    subArray1[A[j]]=1
                j=j+1

                

            k= B[i][2]
            status=True
            while k<=B[i][3]:
                if A[k] in subArray1:
                    subArray1[A[k]]-=1
                    if subArray1[A[k]]==0:
                        subArray1.pop(A[k])

                else:
                   status=False
                k= k+1
            if len(subArray1)==0 and status==True:
                result.append(1)
            else:
                result.append(0)

        return result


obj= solution()
print(obj.solve( [ 100000, 100000, 100000, 100000, 100000 ],[ 
       [1, 3, 0, 0],
        [2, 4, 1, 1]
     ]))