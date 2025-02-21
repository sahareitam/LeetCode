# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        fast = head.next
        slow = head
        if slow == None or fast == None:
            return head

        while  fast != None:
            slow = slow.next
            fast = fast.next
            if fast == None:
                return slow
            fast = fast.next
        return slow
