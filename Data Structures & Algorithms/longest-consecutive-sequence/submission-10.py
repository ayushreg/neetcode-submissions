class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
            
        nums.sort()
        longest = 0
        cnt = 1
        for i in range(0,len(nums)-1):
            diff = nums[i+1] - nums[i]

            if diff == 1:
                cnt += 1
            elif diff == 0:
                continue
            else:
                if cnt > longest:
                    longest = cnt
                cnt = 1


        return max(longest, cnt)


