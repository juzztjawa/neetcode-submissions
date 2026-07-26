class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n ==1:
            return 0
        l = 0
        r = 1
        maxprof = 0
        currstock = prices[0]
        for i in range(n):
            if prices[i] - currstock  <= 0:
                currstock = prices[i]
                continue
            prof = prices[i] - currstock
            maxprof = max(prof,maxprof)
        return maxprof