class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        topFreq = [[] for _ in range(len(nums)+1)]

        hashMap = {}

        for num in nums:
            hashMap[num] = hashMap.get(num,0) + 1
        


        for key, value in hashMap.items():
            topFreq[value].append(key)
            
        ans = []
        for index in range(len(topFreq) -1, -1, -1):
            for num in topFreq[index]:
                ans.append(num)
                if len(ans) == k:
                    return ans
