class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        order=[]
        counter =defaultdict(int)
        for n in nums :
            counter[n]+=1
        
        order= sorted(counter,key = counter.get, reverse = True)

        return order[:k]


        