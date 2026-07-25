class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # For hash maps we need brackets
        hashMap = {}

        # Loop through the whole array
        for i in range(len(nums)):
            # Get the difference
            diff = target - nums[i]
            # if our difference is in the hash map then we found the pair
            if diff in hashMap:
                return [hashMap[diff], i ]
            
            # If its not in our hash map we need to add it
            hashMap[nums[i]] = i
       
        