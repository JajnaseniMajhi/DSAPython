from unittest import result


class solution:
    def solve(self,A,B):
        if len(A)<B:
            return []
        window={}
        count=0
        result=[]
        for i in range(B):
            if A[i] in window:
                window[A[i]]=window[A[i]]+1
            else:
                window[A[i]]=1

        result.append(len(window))
        startIndex=0
        for i in range(B,len(A)):
            if A[i] in window:
                window[A[i]]=window[A[i]]+1
                
            else:
                    window[A[i]]=1

            if A[startIndex] in window:
                window[A[startIndex]]= window[A[startIndex]]-1
                if window[A[startIndex]]==0:
                    window.pop(A[startIndex])
            result.append(len(window))
            startIndex= startIndex+1
        return result

obj=solution()
print(obj.solve([ 31, 51, 31, 51, 31, 31, 31, 31, 31, 31, 51, 31, 31 ],3))


