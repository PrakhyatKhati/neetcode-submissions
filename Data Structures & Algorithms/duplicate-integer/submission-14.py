class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ## containes duplicate huh 
        #okay lets do it .. .. .. .. ..
        sett = set()
        for num in nums:
            if num in sett:
                return True
            sett.add(num)
        return False 