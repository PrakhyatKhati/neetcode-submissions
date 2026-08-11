class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if nums[i] in dictt:
                return [dictt[nums[i]],i]
            dictt[difference]=i

        return []
