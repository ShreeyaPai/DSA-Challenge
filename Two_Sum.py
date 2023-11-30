# Code 2
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map={}
        for i in range(len(nums)):
            if(target-nums[i] in map):
                return [i,map.get(target-nums[i])]
            else:
                map.update({nums[i]:i})
        return []

# Brute Force

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    ans.append(i)
                    ans.append(j)
                    return ans
