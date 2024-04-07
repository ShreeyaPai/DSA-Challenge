# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ##SIMILAR TO DIAMETER PROBLEM
        res=[root.val] # initialise to array element to easily use in recursion
        def dfs(root):
            if not root: return 0
            leftMax=dfs(root.left)
            rightMax=dfs(root.right)
            leftMax=max(leftMax,0)
            rightMax=max(rightMax,0)
            res[0]=max(res[0],root.val+leftMax+rightMax) # val with ssplitting
            return root.val+max(leftMax,rightMax) # return val without splitting

        dfs(root)
        return res[0]
