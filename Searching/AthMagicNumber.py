from unittest import result


class solution:
    def solve(self,A,B,C):
        r= min(B,C)*A
        l=1
        result  =0
        LCM=(B*C)//self.findGCD(B,C)
        while l<=r:
            mid= (l+r)//2
            totalMagicNumbr=self.findMagicNumberCount(mid,B,C,LCM)
            if totalMagicNumbr>A:
                r=mid-1
                result=mid

            elif totalMagicNumbr<A:
                l=mid+1

            elif totalMagicNumbr==A:
                return mid
        

    def findMagicNumberCount(self,A,B,C,LCM):
        return (A//B)+(A//C)-(A//LCM)
    
    def findGCD(self,B,C):
        if C==0:
            return B

        return self.findGCD(C,B%C)


obj= solution()
print(obj.solve(1,2,3))