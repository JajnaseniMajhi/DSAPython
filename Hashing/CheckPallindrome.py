from tkinter import SOLID


class solution:
    def solve(self,A):
        charArray= list(A)
        mapList={}
        for i in range(len(charArray)):
            if charArray[i] in mapList:
                mapList[charArray[i]]=mapList[charArray[i]]+1
            else:
                mapList[charArray[i]]=1
        uniqueCount=0
        for j in mapList:
            if mapList[j]%2!=0:
                uniqueCount+=1
                if uniqueCount>1:
                    return 0

        return 1

obj= solution()
print(obj.solve("lalttppyadd"))


        