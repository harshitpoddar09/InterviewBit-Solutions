import math
class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if x==0:
            return 0
        if n==0:
            return 1
        elif n<0:
            return (1/pow(x,-n,d))%d
        elif n%2==1:
            return (x*pow(x,n-1,d))%d
        return pow(x*x,n//2,d)%d
