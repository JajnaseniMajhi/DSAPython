from math import prod


class solution:
    def solve(self,A):
        product=set()
        input=[]
        while A>0:
           
            digit=A%10
            input.append(digit)
            A=A//10
            if digit not in product:
                product.add(digit)
            else:
                return 0

        for i in range(len(input)-1):
            tempPr=input[i]
            for j in range(i+1,len(input)):
                tempPr= tempPr * input[j]
                if tempPr not in product:
                    product.add(tempPr)
                else:
                    return 0

        return 1

obj =solution()
print(obj.solve(236))
                    