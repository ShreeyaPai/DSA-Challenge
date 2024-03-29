# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first,second=l1,l2
        sum=first.val+second.val
        carry=sum/10
        digit=sum%10
        head=l3=ListNode(digit)
        # print(head)
        if not first.next and not second.next:
            if carry!=0:
                head.next=ListNode(carry)
            return head

        while first.next and second.next:
            first,second=first.next,second.next
            sum=first.val+second.val+carry
            carry=sum/10
            digit=sum%10
            new=ListNode(digit)
            l3.next=new
            l3=new
        # print(head)

        while first.next:
            first=first.next
            sum=first.val+carry
            carry=sum/10
            digit=sum%10
            new=ListNode(digit)
            l3.next=new
            l3=new
        while second.next:
            second=second.next
            sum=second.val+carry
            carry=sum/10
            digit=sum%10
            new=ListNode(digit)
            l3.next=new
            l3=new
        if carry!=0:
            new=ListNode(carry)
            l3.next=new      
        return head


