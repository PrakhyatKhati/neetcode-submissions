class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # lets create a dictionary first
        count_s = {}
        for ch in s :
            count_s[ch]= count_s.get(ch,0)+1
        
        # lets count t
        count_t={}
        for ch in t:
            count_t[ch] = count_t.get(ch,0)+1

        return count_s ==count_t
