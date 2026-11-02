class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        res = []

        for i in range(len(s)):
            if i > 0 and s[i] == s[i-1]:
                continue
            
            l = i+1
            r = len(s) - 1
            while l < r:
                sum = s[i] + s[l] + s[r]

                if sum > 0:
                    r-=1
                elif sum < 0:
                    l+=1
                else:
                    res.append([s[i], s[l], s[r]])
                    l+=1
                    r-=1
        return res