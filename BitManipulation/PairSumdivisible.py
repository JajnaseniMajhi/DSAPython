def solve(A,B):
    count=0
    for i in range(len(A)):
        if ((A[i] %B)+(A[i+1]%B))%B==0:
            count+=count

    
