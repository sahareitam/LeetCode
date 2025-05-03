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
        if not list1 and not list2:
            return None
        elif not list2:
            return list1
        elif not list1:
            return list2

        if list1.val >= list2.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next
        new = head

        while list1 and list2:
            if list1.val >= list2.val:
                new.next = list2
                new = new.next
                list2 = list2.next
            else:
                new.next = list1
                new = new.next
                list1 = list1.next
        if list1:
            new.next = list1
        else:
            new.next = list2
        return head
