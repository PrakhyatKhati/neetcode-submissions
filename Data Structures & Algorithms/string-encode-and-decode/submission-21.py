class Solution:

    def encode(self, strs: List[str]) -> str:
        
        # first we need to decode - and we are planning to use   lenght+#+the string
        res =""
        for s in strs:
            res += str(len(s))+"$"+s
        return res

    def decode(self, s: str) -> List[str]:
        # now time for decoding

        res = []
        i =0 
        while i <len(s):
            j = i 
            while s[j] != "$":
                j=j+1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])

            i=j+1+length

        return res

