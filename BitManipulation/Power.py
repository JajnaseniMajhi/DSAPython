import re


class solution:
    def power(self,A,B,C):
        if A==0:
            return 0
        if B==0:
            return 1
        
        result= self.power(A,B//2,C)
        # result= result %C

        if B%2==1:
            result= (result %C * result %C)%C * A

        else:
            result= (result %C * result %C)%C

        if result<0:
            result=result+C
        return result


obj= solution()
print (obj.power(-1,1,20))
