class solution:
    def solve(self,A):
        max_odd = '!'
        max_even = '!'

        min_odd = '~'
        min_even = '~'
        for i in A:
            if ord(i) %2==0:
                max_even= max(max_even,i)
                min_even=min(min_even,i)
            else:
                min_odd= min(min_odd,i)
                max_odd=max(max_odd,i)

        if ord(max_even)-ord(min_odd)>1:
            return 1
        if ord(max_odd)-ord(min_even)>1:
            return 1

        return 0


        

obj= solution()

print(obj.solve([1,2,3,4]))

    

