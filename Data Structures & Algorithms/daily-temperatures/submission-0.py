class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures) # Array length
        ans = [0]*n # answer array
        for i in range(n):
            for future in range(i + 1, n):
                if(temperatures[future] > temperatures[i]):
                    ans[i] = future - i
                    break
        
        return ans

