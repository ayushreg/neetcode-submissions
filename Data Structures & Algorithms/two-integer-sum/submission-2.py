class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # The key are the nums and values are index
        map = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if(difference in map):
                return[map[difference], i]
            else:
                map[nums[i]] = i
        
