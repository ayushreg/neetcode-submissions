class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = l + 1
        maxProfit = 0
        while(r < len(prices)):
            if(prices[r] < prices[l]): # Make sure to compare the prices and not the index 
                l =r
                r = l + 1
            else:
                maxProfit = max(maxProfit, (prices[r] - prices[l]))
                r += 1
        
        return maxProfit

            