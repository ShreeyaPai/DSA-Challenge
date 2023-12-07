class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        ans=-1
        right=len(height)-1
        while(left<right):
            #print(left,right,min(height[left],height[right]))
            value=min(height[left],height[right])*(right-left)
            if(value>ans): ans=value
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        #print(values)
        return ans
