class Solution:
    def maxProfit(self, prices: List[int]) -> int:



        minDay = 0
        profit = 0
        for i in range(len(prices)):
            curProfit = prices[i] - prices[minDay]
            profit = max(profit, curProfit)
            
            if prices[minDay] < prices[i]:
                continue
            else:
                minDay = i

        
        return profit



        