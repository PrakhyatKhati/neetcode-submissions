class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        max_water=0
        left=0
        right=n-1

        while left <right :
            
            width = abs(left-right)
            height = min(heights[left],heights[right])
            area = width*height
            max_water= max(max_water,area)
            if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1
            
        # for i in range(n):
        #     for j in range(i+1,n):
        #         width=j-i
        #         h= min(heights[i],heights[j])
        #         area = width*h
        #         max_water= max(max_water,area)
            
        return max_water
        

        