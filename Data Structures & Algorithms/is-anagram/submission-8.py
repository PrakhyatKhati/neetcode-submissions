class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictionary = {}
        for x in s :

            dictionary[x]=dictionary.get(x,0)+1
            
        for y in t:
            if y  not in dictionary or dictionary[y] ==0:
                return False
            dictionary[y]-=1

        return True