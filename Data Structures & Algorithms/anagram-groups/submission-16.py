class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # first 
        output = defaultdict(list) 

        for w in strs:
            key =''.join(sorted(w))
            if key in output.keys():
                output[key].append(w)
            else:
                output[key] = [w] 

        return list(output.values())