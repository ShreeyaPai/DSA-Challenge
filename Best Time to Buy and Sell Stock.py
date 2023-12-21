class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=0
        sell=1
        Max=-1
        while sell < len(prices):
            if prices[buy]<prices[sell]:
                Max=max(Max,prices[sell]-prices[buy])
            else:
                buy=sell
            sell+=1
        return max(Max,0)
