class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0

        for num in nums:
            if((num - 1) not in nums):
                start = num +1
                length = 1
                while(start in nums):
                    start += 1
                    length += 1
                max_length = max(length, max_length)
        
        return max_length