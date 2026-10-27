class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter ={}

        for ch in s :
            counter[ch] = counter.get(ch,0)+1
        
        for ch in t :
            counter[ch] = counter.get(ch,0)-1

        for value in counter.values():
            if value !=0:
                return False

        return True