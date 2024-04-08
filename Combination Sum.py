class Solution(object):
    def combinationSum(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        subset=[]
        res=[]
        total=0
        def dfs(i,total):
            if total==target:
                res.append(subset[:])
                return
            if i >= len(nums) or total>target:
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i,total+nums[i])
            # decision to include nums[i+1]
            subset.pop()
            dfs(i + 1,total)
        dfs(0,0)
        return res
