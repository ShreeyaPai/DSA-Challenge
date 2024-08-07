# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return False
        slow,fast=head,head.next
        if not fast: return False
        if not fast.next: return False
        while slow and fast and fast.next and slow.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
        
        
