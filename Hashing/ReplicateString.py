class solution:
    def solve(self,A,B):
        charArray= list(B)
        # if len(charArray)==2:
        #     return 1

        mapCount= {}

        for i in range(len(charArray)):
            if charArray[i] in mapCount:
                mapCount[charArray[i]]+=1

            else:
                mapCount[charArray[i]]=1


        for key in mapCount:
            if mapCount[key]%A==0:
                continue
            else:
                return 0

        return 1


obj= solution()
print(obj.solve(2,"bbaabb"))