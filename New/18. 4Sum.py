class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        for first,a in enumerate(nums):
            if first>0 and a==nums[first-1]: continue
            for second in range(first+1,len(nums)):
                b=nums[second]
                if second>first+1 and b == nums[second-1]:
                    continue
                left,right = second+1, len(nums)-1
                while left<right:
                    fourSum = a + b + nums[left] + nums[right]
                    if fourSum > target:
                        right-=1
                    elif fourSum < target:
                        left+=1
                    else:
                        res.append([a,b,nums[left],nums[right]])
                        left+=1
                        while left<right and nums[left-1]==nums[left]:
                            left+=1
        return res


        
