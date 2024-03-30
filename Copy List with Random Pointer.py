"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        oldtonew={None:None}
        cur=head
        while cur:
            new=Node(cur.val)
            oldtonew[cur]=new
            cur=cur.next
        cur=head
        while cur:
            new=oldtonew[cur]
            new.next=oldtonew[cur.next]
            new.random=oldtonew[cur.random]
            cur=cur.next
        return oldtonew[head]
