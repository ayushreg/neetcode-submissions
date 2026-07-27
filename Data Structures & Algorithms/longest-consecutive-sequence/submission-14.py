class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Edge case
        if len(nums) == 0:
            return 0

        nums.sort()
        ans = 1
        current =1

        for i in range(len(nums) - 1):
            if(nums[i+1] == (nums[i] +1)):
                current += 1
                ans = max(current, ans)
            elif  nums[i+1] == nums[i]:
                continue
            else:
                current = 1

        return ans
            


