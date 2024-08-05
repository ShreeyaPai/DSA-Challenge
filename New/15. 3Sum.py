class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()

        for i,a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left < right:
                if (a + nums[left] + nums[right]<0):
                    left+=1
                elif a+nums[left]+nums[right] > 0:
                    right-=1
                else:
                    res.append([a,nums[left],nums[right]])
                    left+=1
                    while left<right and nums[left] == nums[left-1]:
                        left+=1
        return res

