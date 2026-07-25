class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        ans = float('inf')
        while(l <= r):
            mid = (l + r) // 2
            ans = min(ans, nums[mid])
            #This means the left part of the array is strictly increasing
            if(nums[mid] >= nums[l]):
                ans = min(ans, nums[l])
                l = mid + 1
            else:
                r = mid - 1
            
        return ans

            
