from collections import Counter
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        new=Counter(A)
        flag=0
        for key in new:
            if new[key]%2==0:
                continue
            else:
                if flag==0:
                    flag=1
                else:
                    return 0
        return 1