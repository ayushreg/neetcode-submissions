class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        # We need to loop until left and right == each other because after that, it means we didnt find our value
        while(l <= r):
            mid = (l+r) // 2

            if(nums[mid] == target):
                return mid
            elif(nums[mid] < target):
                l = mid + 1
            else:
                r = mid -1



        return -1