class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest=prices[0]
        best=0
        for i in range(1,len(prices)):
            best = max(best, prices[i]-lowest)
            lowest=min(lowest, prices[i])
        
        return best
        