from tkinter.tix import TList


class solution:
    def solve(self, A,B):
        tList= list(A)
        for i in range(B):
            min= tList[i]
            index=i
            for j in range(i, len(A)):
                if tList[j]<min:
                    min=tList[j]
                    index=j

            temp=tList[i]
            tList[i]=tList[index]
            tList[index]=temp

        return min

obj= solution()

print(obj.solve([2,3,1,4,6,2,3],4))