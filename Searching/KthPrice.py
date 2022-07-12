class solution:
    def solve(self,A,B):
        A=list(A)
        A.sort()
        return A[B-1]