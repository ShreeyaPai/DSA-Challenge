class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left,right=0,len(height)-1
        ans=-1
        while left<right:
            currVal=min(height[left],height[right])*(right-left)
            ans=max(ans,currVal)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return ans
