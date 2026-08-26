class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        output=[1]*n

        left = 0
        right = n-1
        left_product=1
        right_product  =1 
        while left<n:
            output[left]*=left_product # output[left]=output[left]*left_product
            left_product*= nums[left]
         #   print(output)
            output[right]*=right_product
            right_product*=nums[right]
        #print(output)
            right-=1
            left+=1
        #print(output)

        return output
        


        