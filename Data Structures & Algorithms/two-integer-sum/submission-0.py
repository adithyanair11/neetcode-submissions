class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if(map.get(comp) is None):
                map[nums[i]] = i
            else:
                return [map.get(comp), i]
        return []
        