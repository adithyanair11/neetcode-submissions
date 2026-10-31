class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        res = []

        for num in nums:
            freq[num]+=1
        
        sorted_list = sorted(freq.items(), key=lambda item: item[1]    ,reverse=True)

        for i in range(k):
            res.append(sorted_list[i][0])
        
        return res


