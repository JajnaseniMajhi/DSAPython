class solution:
    def sortColour(self,A):
        zeroCount=0
        oneCount=0
        twoCount=0
        for i in range(len(A)):
            if A[i]==0:
                zeroCount=zeroCount+1
            elif A[i]==1:
                oneCount=oneCount+1
            elif A[i]==2:
                twoCount=twoCount+1
        
        for i in range(len(A)):
            if zeroCount!=0:
                A[i]=0
                zeroCount=zeroCount-1
            elif oneCount!=0:
                A[i]=1
                oneCount=oneCount-1

            elif twoCount!=0:
                A[i]=2
                twoCount=twoCount-1

        return A


        
