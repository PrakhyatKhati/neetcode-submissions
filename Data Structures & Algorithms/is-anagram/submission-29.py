class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # lets create a dictionary and then loop throught the other string to see if its anagram of not
        
        # first thing first to be anagram we ned to get the length same 

        if len(s) != len(t):
            return False

        
        dictionary ={}
        for ch in s:
            dictionary[ch]= dictionary.get(ch,0)+1
        

        # lets loop through the new string

        for ch in t :
            dictionary[ch]= dictionary.get(ch,0) -1 
            if dictionary[ch] < 0:
                return False
        return True
        