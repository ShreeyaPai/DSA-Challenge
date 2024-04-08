class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        def backtrack(perm,rem):
            if len(rem)==0:
                res.append(perm[:])
                return
            for i in range(len(rem)):
                curPerm=perm[:]
                curPerm.append(rem[i])
                newRem=rem[:]
                newRem.pop(i)
                backtrack(curPerm,newRem)
        backtrack([],nums)
        return res
