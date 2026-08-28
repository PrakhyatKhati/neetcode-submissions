class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1

        while l<r:
            while l<r and not self.isalnumm(s[l]):
                l+=1
            while l<r and not self.isalnumm(s[r]):
                r-=1
        
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1

        return True


    def isalnumm(self,c):   
# Now we have seen there is a method called isalnum() to see if the crachet is alphanumeri
# but lets build our own version
        return(ord('A')<=ord(c)<=ord('Z') or 
            ord('a')<=ord(c)<=ord('z') or 
            ord('0')<=ord(c)<=ord('9'))




