# Code 2
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums1=set(nums)
        if len(nums1)==len(nums): return False
        else: return True

# Code 1

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                return True
        return False
