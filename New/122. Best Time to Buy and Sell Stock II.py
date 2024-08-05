class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=0
        sell=buy+1
        profit=0
        while sell<len(prices) and buy<sell:
            if prices[sell]>prices[buy]:
                profit+=prices[sell]-prices[buy]
                buy+=1
                sell+=1
            else:
                buy=sell
                sell=buy+1
        return profit
