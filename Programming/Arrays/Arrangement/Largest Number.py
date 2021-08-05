from functools import cmp_to_key
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = map(str, A)
        key = cmp_to_key(lambda a,b: 1 if a+b >= b+a else -1)
        ans = ''.join(sorted(A, key= key, reverse=True))
        while ans and ans[0]=='0':
            ans=ans[1:]
        if ans:
            return ans
        else:
            return '0'