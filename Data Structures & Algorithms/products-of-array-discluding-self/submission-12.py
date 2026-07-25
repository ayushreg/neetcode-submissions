class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        total = 1
        zeroCnt = 0
        for num in nums:
            if num == 0:
                zeroCnt += 1
            else:
                total *= num

        result = [0] * len(nums)

        for i in range(len(nums)):
            if zeroCnt > 1:
                continue
                #b/c every element will be zero
            elif zeroCnt == 1:
                if nums[i] == 0:
                    result[i] = total
            else:
                result[i] = int(total / nums[i])
        return result