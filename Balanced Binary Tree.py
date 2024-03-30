# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #if not root:return True
        def height(root):
            if not root: return [True,0]
            left,right=height(root.left),height(root.right)
            bal= left[0] and right[0] and abs(right[1]-left[1])<=1
            return [bal,1+max(left[1],right[1])]

        return height(root)[0]
