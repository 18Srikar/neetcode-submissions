# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=list1
        curr2=list2
        new=ListNode(-1)
        curr_new=new
        while curr1 and curr2:
            if curr1.val<=curr2.val:
                curr_new.next=curr1
                curr_new=curr_new.next
                curr1=curr1.next
            else:
                curr_new.next=curr2
                curr_new=curr_new.next
                curr2=curr2.next
        if curr1:
            curr_new.next=curr1
        if curr2:
            curr_new.next=curr2
        return new.next
