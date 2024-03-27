# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next==None: 
            head=None
            return head
        end=head
        count=1
        remove=None
        while end.next!=None:             
            if(count>=n):
                if(remove==None):remove=head
                remove=remove.next
            end=end.next
            count+=1
            
        #print(remove)
        #print(end,count)
        if(remove==None):
            head=head.next
            return head
        prev=head
        while prev.next!=remove:
            prev=prev.next
        #print(prev)
        prev.next=remove.next
        return head
