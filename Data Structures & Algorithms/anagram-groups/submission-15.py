class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # first 
        output = defaultdict(list) 

        for w in strs:
            key =''.join(sorted(w))
            output[key].append(w)

        return list(output.values())