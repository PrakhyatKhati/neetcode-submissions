class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for single_string in strs:
            key=''.join(sorted(single_string))
            if key not in res:
                res[key]=[]
            res[key].append(single_string)
        return list(res.values())