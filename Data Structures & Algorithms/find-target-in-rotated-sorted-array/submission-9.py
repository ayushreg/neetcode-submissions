class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        l = 0
        r = len(nums) - 1
        while(l <= r):
            mid = (l+r) // 2

            if(nums[mid] == target):
                return mid
            elif(nums[mid] >= nums[l]): # This means the left side of the array is sorted so like 2,3,4,5,1 or 3,4,5,1,2, or 1,2,3,4,5
                if(nums[l] <= target and nums[mid] >= target):
                    r = mid - 1
                else:
                    l = mid + 1
            else: # This means we are on the sorted part on the right so 5,1,2,3,4 or 4,5,1,2,3 or 
                if(target >= nums[mid] and target <= nums[r]):
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
