class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Make output array
        result = [0]*len(nums)
        prefix = 1

        # Make the prefix array, get the prefix or all element up until that point
        for i in range(len(nums)):
            result[i] = prefix 
            prefix *= nums[i] 
        
        # Now go backwards and get the postfix 
        postfix = 1
        for i in range((len(nums)- 1), -1, -1):
            result[i] = result[i] * postfix
            postfix *= nums[i]


        return result