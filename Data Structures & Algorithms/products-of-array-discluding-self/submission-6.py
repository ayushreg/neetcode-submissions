class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Make the prefix post fix array
        # We need to take care of the cases
        prefix= [0]*len(nums)
        prefix[0] = nums[0]
        postfix= [0]*len(nums)
        postfix[-1] = nums[-1]


        # Build the arrays
        for i in range(1, len(nums)):
            prefix[i] = prefix[i- 1] * nums[i]

        for i in range((len(nums) - 2), -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]


        res = [0]*len(nums)

        for i in range(len(nums)):
            if(i == 0):
                left = 1
                right = postfix[i + 1]
            elif(i == (len(nums) - 1)):
                left = prefix[i - 1]
                right = 1
            else:
                left = prefix[i-1]
                right = postfix[i + 1]

            res[i] = left * right

        return res