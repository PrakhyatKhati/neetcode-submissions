class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # left number
        n = len(nums)
        left =[1]*n
        right =[1]*n
        output=[1]*n
        for i in range(1,n):
            left[i] = left[i-1]* nums[i-1]
            j = n-1-i
            right[j] = right[j+1]* nums[j+1] 


        for i in range(n):
            output[i] = left[i]* right[i]

        return output