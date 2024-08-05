class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=0
        sell=buy+1
        profit=-1
        while sell<len(prices) and buy<sell:
            if prices[sell]>prices[buy]:
                profit=max(profit,prices[sell]-prices[buy])
                sell+=1
            elif prices[sell]<=prices[buy]:
                buy=sell
                sell=buy+1
        if profit==-1: return 0
        return profit


        
