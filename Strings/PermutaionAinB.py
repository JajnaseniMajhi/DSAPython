from operator import truediv
from unittest import result


class solution:
    def check(self, A,B):
        if A==B:
            return True
        else:
            return False
            B= list(B)

    def solve(self,A,B):
        if len(B)<len(A):
            return 0
        N= len(A)
        M=len(B)
        Adict={}
        windowDict={}
        result=0
        for ch in A:
            if ch in Adict:
                Adict[ch]+=1
            else:
                Adict[ch]=1
        windowSize=N
        for ch in range(N):
            if B[ch] in windowDict:
                windowDict[B[ch]]+=1
            else:
                windowDict[B[ch]]=1
            windowSize=windowSize-1
            if windowSize==0:
                if self.check(windowDict,Adict):
                    result=result+1

        # remove first element from window
        for ch in range(N,M):
            windowDict[B[ch-N]]-=1
            if windowDict[B[ch-N]]==0:
                windowDict.pop(B[ch-N])
            if B[ch] in windowDict:
                windowDict[B[ch]]+=1
            else:
                windowDict[B[ch]]=1

            if self.check(windowDict,Adict):
                    result=result+1

        return result


obj= solution()

print(obj.solve("aca","acaa"))


