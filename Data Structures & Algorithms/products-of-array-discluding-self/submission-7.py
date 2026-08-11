class Solution:

    def encode(self, strs: List[str]) -> str:
        encode =""
        for s in strs:
            encode=encode+str(len(s))+"#"+s
        return encode
        #[4#abcd5#abcd35#12345]
         #0123456    
    def decode(self, s: str) -> List[str]:
        result =[]
        i=0
        while i<len(s):
            j=i
            while s[j] != '#':
                j+=1
            length= int(s[i:j])
            start=j+1
            end=start+length #2+4
            result.append(s[start:end])
            i=end
        return result

        
