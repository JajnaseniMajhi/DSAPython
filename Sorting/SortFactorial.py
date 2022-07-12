import functools


class solution:
    def factCount(self,num):
        count=0
        stepper=1
        while stepper * stepper<=num:
            if num % stepper==0:
                if stepper * stepper!=num:
                    count=count+2
                else:
                    count=count+1
            stepper=stepper+1

        return count



    def compare(self,a,b):
        if self.factCount(a)<self.factCount(b):
            return -1
        else:
            return 1

    def solve(self,A):
        return sorted(A,key= functools.cmp_to_key(self.compare))

obj= solution()
print (obj.solve([3,9,4,6,12,10,7]))
