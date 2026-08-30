class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numss=sorted(nums)
        current=0
        storage= []
        
        for i,value in enumerate(numss):
            current= value
            left=i+1
            right=len(numss)-1

            if i>0 and value == numss[i-1]:
                continue 
            while left<right:
        
                total=current+numss[left]+numss[right]
                if total == 0:
                    storage.append([current,numss[left],numss[right]])
                    left+=1
                    right-=1

                    while left<right and numss[left] == numss[left-1]:
                        left+=1
                    while left<right and numss[right] == numss[right+1]:
                        right-=1

                elif total > 0:
                    right-=1
                else :
                    left+=1

        return  storage 




        