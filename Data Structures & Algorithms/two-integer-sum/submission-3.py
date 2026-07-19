class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        HashMap = {}

        for i in range(len(nums)):
            val = target - nums[i]

            if val in HashMap:
                return [HashMap[val], i]
            else:
                HashMap[nums[i]] = i
        
        return False