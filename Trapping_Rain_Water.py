class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # water[i]= min (max_left_height,max_right_height)-arr[i]
        ans=0
        l=0
        r=len(height)-1
        lmax=-999999
        rmax=-999999
        while(l<r):
            lmax=max(lmax,height[l])
            rmax=max(rmax,height[r])
            if lmax<rmax:
                ans+=lmax-height[l]
                l+=1
            else:
                ans+=rmax-height[r]
                r-=1
        return ans
