from unittest import result


class soltion:
    def solve(self,A,B):
        hm={}
        result=[]
        for i in range(len(A)):
            if A[i] not in hm:
                hm[A[i]]=1
            else:
                hm[A[i]]+=1


        for j in range(len(B)):
            if B[j] in hm:
                result.append(B[j])
                hm.pop(B[j])

        for k in sorted(hm):
            count=0
            while count<hm[k]:
                result.append(k)
                count=count+1

        return result


obj=soltion()
print(obj.solve([ 12, 7 ],[ 7, 1, 6, 17, 2, 19, 10 ]))
                
