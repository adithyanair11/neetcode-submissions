class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        length = 0

        for num in lookup:
            if num-1 not in lookup:
                current = num
                count = 1
                while current + 1 in lookup:
                    current+=1
                    count+=1
                length = max(length, count)


        return length


