class solution:
    def solve(self,A):
        l=0
        r=A
        result=0
        while l<=r:
            mid=(l+r)//2
            if mid * mid ==A:
                return mid
            elif mid * mid <A:
                result=mid
                l=mid+1

            elif mid * mid >A:
                r= mid-1


        return result

obj= solution()
print(obj.solve(31))