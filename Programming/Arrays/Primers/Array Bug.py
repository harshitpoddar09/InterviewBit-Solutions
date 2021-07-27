class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers
    def rotateArray(self, a, b):
        ret = []
        a+=a
        b=b%(len(a)//2)
        for i in xrange(len(a)//2):
            ret.append(a[i + b])
        return ret
