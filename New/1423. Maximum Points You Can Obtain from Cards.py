class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        left,right=0,len(cardPoints)-k
        window=sum(cardPoints[right:])
        res=window

        while right < len(cardPoints):
            window += (cardPoints[left]-cardPoints[right])
            res=max(res,window)
            left+=1
            right+=1
        return res
            
