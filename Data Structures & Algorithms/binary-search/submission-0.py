class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        return self.binarySearch(nums,l,r,target)


    def binarySearch(self, nums, l, r, target):
        if(l > r):
            return -1
        
        mid = (l + r) // 2

        if(nums[mid] == target):
            return mid
        elif(nums[mid] < target):
            return self.binarySearch(nums,mid + 1,r,target)
        else:
            return self.binarySearch(nums,l,mid - 1,target)
