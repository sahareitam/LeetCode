# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        p_check = head
        p = head

        for i in range(n):
            p_check = p_check.next
        if p_check == None:
            if p.next == None:
                head = None
            else:
                head = head.next
            return head
        while p_check.next != None:
            p = p.next
            p_check = p_check.next
        if p.next.next == None:
            p.next = None
        else:
            p.next = p.next.next
        return head



