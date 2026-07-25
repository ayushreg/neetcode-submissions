class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    
        n = len(temperatures)
        ans = [0]*n
        stack = []
        stack.append((temperatures[0], 0)) #tuple of value,index
        for i in range(1, n):
            # We can short-circuit so we dont check out of bounds
            while(stack and temperatures[i] > stack[-1][0]):  # If our current val is greater than top of stack
                val = stack.pop()
                ans[val[1]] = i - val[1]

            stack.append((temperatures[i], i))

        return ans

    




        
