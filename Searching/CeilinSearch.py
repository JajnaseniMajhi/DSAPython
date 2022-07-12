class solution:
    def solve(self,A,B,C):
        l=0
        r=A-1
        result=-1
        while l<=r:
            mid= (l+r)//2
            if B[mid]==C:
                return B[mid]
            elif B[mid]>C:
                result= B[mid]
                r=mid-1
            
            elif B[mid]<C:
                l=mid+1

        return result


obj= solution()
print(obj.solve(11,[ -98, -95, -79, -68, -41, -40, -18, 8, 34, 49, 73 ],29))

