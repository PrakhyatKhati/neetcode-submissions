class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        x=0
        y=len(heights)-1
        while(x<y):
            length=min(heights[x],heights[y])
            width=y-x
            area=max(area,length*width)
            if(heights[x]>=heights[y]):
                y-=1
            else:
                x+=1
           
        return area