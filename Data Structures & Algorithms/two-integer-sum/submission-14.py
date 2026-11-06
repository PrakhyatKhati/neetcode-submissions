class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicct={}
        for i,value in enumerate(nums):
            difference = target-value
            
            if difference  in dicct:
                return[dicct[difference],i]
            dicct[value] =i
                


