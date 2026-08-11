class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in dictt:
                return [dictt[difference],i]
            dictt[nums[i]]=i
            
        return []
          

        