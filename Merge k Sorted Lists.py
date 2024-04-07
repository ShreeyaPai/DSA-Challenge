# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        finalList=[]
        if not lists and len(lists)==0: return None
        while len(lists)>1:
            mergedList=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                if i+1<len(lists):
                    l2=lists[i+1]
                else: l2=None
                mergedList.append(self.mergeTwoLists(l1,l2))
            lists=mergedList
        return lists[0]


    def mergeTwoLists(self,l1,l2):
        dummy=ListNode()
        tail=dummy
        while l1 and l2:
            if l1.val<l2.val:
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            tail=tail.next
        if l1:
            tail.next=l1
        else:
            tail.next=l2
        return dummy.next
        
