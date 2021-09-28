class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        def ascendSearch(arr,lo,hi,key):
            while lo<=hi:
                mid=(lo+hi)//2
                if arr[mid]==key:
                    return mid
                elif arr[mid]>key:
                    hi=mid-1
                else:
                    lo=mid+1
            return -1
        
        def descendSearch(arr,lo,hi,key):
            while lo<=hi:
                mid=(lo+hi)//2
                if arr[mid]==key:
                    return mid
                elif arr[mid]<key:
                    hi=mid-1
                else:
                    lo=mid+1
            return -1
        
        def findBitonic(arr):
            lo=0
            hi=len(arr)-1
            while lo<=hi:
                mid=(lo+hi)//2
                if arr[mid]>arr[mid-1] and arr[mid+1]>arr[mid]:
                    lo=mid+1
                elif arr[mid]<arr[mid-1] and arr[mid+1]<arr[mid]:
                    hi=mid-1
                elif arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                    return mid
        
        bitonic=findBitonic(A)
        if B>A[bitonic]:
            return -1
        elif B==A[bitonic]:
            return bitonic
        else:
            a=ascendSearch(A,0,bitonic,B)
            if a!=-1:
                return a
            b=descendSearch(A,bitonic+1,len(A)-1,B)
            return b