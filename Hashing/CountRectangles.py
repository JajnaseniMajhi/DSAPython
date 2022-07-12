class solution:
    def solve(self,A,B):
        pairPoints= set()

        for i in range(len(A)):
            pairPoints.add((A[i],B[i]))

        count=0

        for i in range(len(A)):
            for j in range(i+1,len(A)):
                x1=A[i]
                x2=A[j]
                y1=B[i]
                y2=B[j]

                if x1!=x2 and y1!=y2:
                    if (x1,y2) in pairPoints and (x2,y1) in pairPoints:
                        count=count+1


        return count//2

        