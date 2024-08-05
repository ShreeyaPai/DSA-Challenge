class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map={}
        for i in range(len(nums)):
            # print(map)
            if target-nums[i] in map:
                return [i,map.get(target-nums[i])]
            map.update({nums[i]:i})
