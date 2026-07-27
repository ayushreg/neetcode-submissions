class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashSet = set(nums)
        res = 0

        for num in nums:
            if((num-1) not in hashSet):
                curr = 0
                currNum = num
                while currNum in hashSet:
                    curr += 1
                    currNum +=1
                res = max(res, curr)

        return res
            