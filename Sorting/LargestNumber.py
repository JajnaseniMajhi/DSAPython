from filecmp import cmp
import functools


class solution:
   def compare(self,x,y):
        xy= str(x)+str(y)
        yz=str(y)+ str(x)

        if xy>yz:
            return -1
        if xy==yz:
            return 0
        if xy<yz:
            return 1

    def solve(self,A):
        result=sorted(A,key=functools.cmp_to_key(self.compare))

        return "".join([str(n) for n in result])


obj= solution()
print(obj.solve([2,3,12,6,9]))