class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #if small number to the left, doesn't matter
        dq=collections.deque()
        ans=[]
        l,r=0,0
        while r<len(nums):
            while dq and nums[dq[-1]]<nums[r]:
                dq.pop()
            dq.append(r)

            if dq[0]<l:
                dq.popleft()

            if (r+1)>=k:
                ans.append(nums[dq[0]])
                l+=1
            r+=1
            
        return ans
            



