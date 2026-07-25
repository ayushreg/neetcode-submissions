class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(len(nums)):
            for j in range(i +1, len(nums)):
                for k in range(j +1, len(nums)):
                    sum = nums[i] + nums[j] + nums[k]
                    if(sum == 0):
                        answer = tuple(sorted([nums[i],nums[j],nums[k]]))
                        if(answer not in ans):
                            ans.add(answer)
        return [list(a) for a in ans]