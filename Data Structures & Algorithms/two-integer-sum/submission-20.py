class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference ={}
        for i, value in enumerate(nums):
            differ = target - value

            if differ in difference :
                return [difference[differ],i]
            difference[value] = i 
                
                 