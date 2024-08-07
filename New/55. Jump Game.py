class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        currGoal = len(nums)-1
        step = currGoal - 1
        while step>=0:
            if nums[step] >= currGoal - step :
                currGoal = step
                step -= 1
            else:
                step-=1
        return currGoal == 0 and step == -1
        



        


        
