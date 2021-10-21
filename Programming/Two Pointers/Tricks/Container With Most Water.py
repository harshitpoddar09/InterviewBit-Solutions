class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, height):
        area=0
        area_new=0
        i=0
        j=len(height)-1
        while i<j:
            if height[i]>height[j]:
                area_new=height[j]*(j-i)
                if area_new>area:
                    area=area_new
                j-=1
            else:
                area_new=height[i]*(j-i)
                if area_new>area:
                    area=area_new
                i+=1
        return area