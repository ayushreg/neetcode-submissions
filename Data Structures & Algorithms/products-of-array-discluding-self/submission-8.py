class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create a output arr, same size as ans

        ans = [0] * len(nums)

        productBefore = 1
        for i in range(len(nums)):
            product = 1

            for j in range(i + 1, len(nums)):
                product *= nums[j]

            ans[i] = productBefore * product
            productBefore *= nums[i]

        return ans