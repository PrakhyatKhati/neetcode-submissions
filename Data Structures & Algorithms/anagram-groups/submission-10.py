class Solution:
    from collections import defaultdict 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen= defaultdict(list)
        for i,word in enumerate(strs):
            anagram="".join(sorted(word))
            seen[anagram].append(word)
        return list(seen.values())

        