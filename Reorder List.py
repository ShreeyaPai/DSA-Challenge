# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        second=slow.next
        prev=slow.next=None
        
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        
        # print(fast)
        first,last=head,prev
        while last:
            ltemp,rtemp=first.next,last.next
            first.next=last
            last.next=ltemp
            first,last=ltemp,rtemp
        #print(head)
            

        
