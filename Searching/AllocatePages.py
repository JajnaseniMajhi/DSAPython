class solution:
    def books(self,A,B):
        sum=0
        for i in range(len(A)):
            sum=sum+A[i]

        r=sum
        result=0
        l=0

        while l<=r:
            mid=(l+r)//2
            if self.checkAllocation(mid,A,B):
                r=mid-1
                result=mid

            else:
                l=mid+1

        return result


    def checkAllocation(self,mid,A,B):
        pages=0
        count=0
        for i in range(len(A)):
            if pages+A[i]>mid:
                count=count+1
                pages=A[i]

            else:
                pages=pages+A[i]

           
        
        if pages!=0:
            count=count+1
        if count>B:
            return False
        else:

            return True

obj=solution()
print(obj.books([ 97, 26, 12, 67, 10, 33, 79, 49, 79, 21, 67, 72, 93, 36, 85, 45, 28, 91, 94, 57, 1, 53, 8, 44, 68, 90, 24 ],26))

        
