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
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        head = list2 if list1.val >= list2.val else list1
        pointer = ListNode()
        while list1 != None and list2 != None:
            if list1.val >= list2.val:
                pointer.next = list2
                list2 = list2.next
            else:
                pointer.next = list1
                list1 = list1.next
            pointer = pointer.next

        if list1 == None:
            pointer.next = list2
        else:
            pointer.next = list1
        return head