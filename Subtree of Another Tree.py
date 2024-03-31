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
        if not t:return True #s is not empty but t is empty
        if not s:return False #t is not empty (checked w first condn) but s is empty

        if self.isSame(s,t):return True
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

    def isSame(self,s,t):
        if not t and not s: return True
        if s and t and t.val==s.val:
            return (self.isSame(s.left,t.left) and self.isSame(s.right,t.right))
        return False #One is empty one is non empty case
