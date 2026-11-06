class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic={}
        
        # lets define a for loop to go across the string to add to the dictionary
        if len(s) != len(t):
            return False

        for i in s :
            dic[i]=dic.get(i,0)+1
            

        for j in t:
            dic[j]= dic.get(j,0)-1
            
    
        return all(val == 0 for val in dic.values())
                         
