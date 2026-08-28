class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference ={}
        output=[]
        for i,nu in enumerate(nums):
            diff = target-nu
            if diff in difference:
                return[difference[diff],i]
            difference[nu]=i
        return []
                


        