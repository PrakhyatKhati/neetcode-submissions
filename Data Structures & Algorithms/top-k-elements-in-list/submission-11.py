class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter  ={}
        array = []
        for i in nums:
            counter[i]=counter.get(i,0)+1
        sorted_counter= sorted(counter,key=counter.get,reverse=True)
            
        return(sorted_counter)[:k]

             
        
        