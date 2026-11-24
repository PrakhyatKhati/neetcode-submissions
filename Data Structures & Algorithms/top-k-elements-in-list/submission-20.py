class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter= {}
        for x in nums:
            if x not in counter:
                counter[x]=0 
            
            counter[x]+=1

        return sorted(counter, key = counter.get, reverse= True)[:k]