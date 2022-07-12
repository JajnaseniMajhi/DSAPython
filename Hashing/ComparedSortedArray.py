class Solution:

    # @param A : list of integers

    # @param B : list of list of integers

    # @return a list of integers

    def solve(self, A, B):

        nA = len(A)

        row = len(B)

        psa = [0]*nA

        psa[0]=A[0]

        posMap = {}

        for i in range(nA):

            if A[i] in posMap:

                posMap[A[i]].append(i)

            else:

                posMap[A[i]] = [i]



            if i!=0:

                psa[i]=psa[i-1]+A[i]



        ans = []

        for r in range(row):

            l1, r1, l2, r2 = B[r][0], B[r][1], B[r][2], B[r][3]

            if (r1-l1)!=(r2-l2):

                ans.append(0)

                continue

            if l1==0:

                sum_1 = psa[r1]

            else:

                sum_1 = psa[r1] - psa[l1-1]

            

            if l2==0:

                sum_2 = psa[r2]

            else:

                sum_2 = psa[r2] - psa[l2-1]



            if sum_1==sum_2:

                allPresent = True

                for i in range(l1, r1+1):

                    positions = posMap[A[l1]]

                    found = False

    # search whether the number is present in the given range [l2, r2]

                    for x in positions:

                        if x>=l2 and x<=r2:

                            found=True

                            break

                    if not found:

                        allPresent = False

                        break



                if allPresent:

                    ans.append(1)

                else:

                    ans.append(0)

            else:

                ans.append(0)



        return ans