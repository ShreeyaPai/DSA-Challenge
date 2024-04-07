############ MORE EFFICIENT SOLUTION:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
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
        

########### INITIAL CODE I WROTE



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 and not list2:return list1
        if not list1: return list2
        if not list2: return list1
        if list1.val <= list2.val: 
            head=ListNode(list1.val)
            list1=list1.next
        else: 
            head=ListNode(list2.val)
            list2=list2.next
        temp=head
        print(head)
        print(list1)
        while list1 and list2:
            new=temp.next=ListNode()
            if list1.val <= list2.val:
                new.val=list1.val
                list1=list1.next
            else:
                new.val=list2.val
                list2=list2.next
            temp=new

        while list1:
            new=temp.next=ListNode()
            new.val=list1.val
            list1=list1.next
            temp=new
        while list2:
            new=temp.next=ListNode()
            new.val=list2.val
            list2=list2.next
            temp=new

        print(head)
        return head
        

