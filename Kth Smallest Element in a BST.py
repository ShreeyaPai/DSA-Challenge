########### MORE OPTIMAL SOLUTION
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack=[]
        cur=root
        n=0
        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            n+=1
            if n==k: return cur.val
            cur=cur.right
        return -1 
################# INORDER SOLUTION

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        lis=[]
        def inorder(root):
            if not root:return None
            inorder(root.left)
            lis.append(root.val)
            inorder(root.right)
        inorder(root)
        # print(lis)
        return lis[k-1]
