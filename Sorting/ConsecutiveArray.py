from lib2to3.pgen2.token import EQUAL


def solve(A):
  A=list(A)
  A.sort()
  for i in range(len(A)-1):
      if A[i+1]-A[i] != 1:
          return 0

  return 1


  print(solve([1,32,5]))

