from collections import Counter
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        a=Counter(A)
        b=Counter(B)
        c=Counter(C)
        ans=set()
        for key in a:
            if key in b:
                ans.add(key)
                b[key]-=1
                if b[key]==0:
                    del b[key]
            if key in c:
                ans.add(key)
                c[key]-=1
                if c[key]==0:
                    del c[key]
        for key in b:
            if key in a:
                ans.add(key)
                a[key]-=1
                if a[key]==0:
                    del a[key]
            if key in c:
                ans.add(key)
                c[key]-=1
                if c[key]==0:
                    del c[key]
        ans=list(ans)    
        return sorted(ans)