# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0,head)
        groupPrev = dummy
        while True:
            kth = GetKthNode(groupPrev,k)
            if not kth:
                break #terminating condition
            groupNext=kth.next
            prev,curr=kth.next,groupPrev.next
            while curr!=groupNext:
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp
            #Linking the remaining with the reversed list
            newGroupPrev=groupPrev.next #store before modifying, this will be next groupPrev
            groupPrev.next=kth
            groupPrev=newGroupPrev
        return dummy.next


def GetKthNode(curr,k):
    while curr and k>0:
        curr=curr.next
        k-=1
    return curr
