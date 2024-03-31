# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not t:return True
        if not s:return False

        if self.isSame(s,t):return True
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

    def isSame(self,s,t):
        if not t and not s: return True
        if s and t and t.val==s.val:
            return (self.isSame(s.left,t.left) and self.isSame(s.right,t.right))
        return False

        #return isSame(t,s) and isSame(t.right,s.right) and isSame(t.left,s.left)
    #print(isSame(root,subRoot))
