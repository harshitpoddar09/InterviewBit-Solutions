class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        A=A.lower()
        new=''
        for i in A:
            if i.isalnum():
                new+=i
        if new==new[::-1]:
            return 1
        return 0