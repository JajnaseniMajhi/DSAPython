from unittest import result


class solution:
    def grayCode(self,A):
        result =[]

        if A==1:
            result.append("0")
            result.append("1")
            return result
        grayCodeList = self.grayCode(A-1)

        for i in range(len(grayCodeList)):
            result.append("0"+ grayCodeList[i])

        for i in range(len(grayCodeList),-1,-1):
            result.append("1"+ grayCodeList[i])

obj=solution()
print(obj.grayCode(2))