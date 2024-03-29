# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None: return head
        last=head.next
        while last.next:
            last=last.next
        # print(last)
        A=head.next
        P=head
        P.next=None
        while A:
            T=A.next
            A.next=P
            P,A=A,T
        #print(last)
        return last
            
