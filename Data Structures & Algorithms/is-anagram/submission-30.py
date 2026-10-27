class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # this is a dictionary

        if len(s) != len(t):
            return False

        counter ={}
        for num in s:
            counter[num] = counter.get(num,0)+1
            
        for num in t :
            if num not in counter or counter[num] == 0:
                return False
            counter[num] -=1 

        return True

          
        
