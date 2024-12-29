# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p = head
        counter = 0
        while p != None:
            counter += 1
            p = p.next
        if counter == 1:
            return True

        if counter % 2 == 0:
            n = counter // 2
        else:
            n = counter // 2

        prev = None
        cur = head

        for i in range(counter):
            if i < n:
                holder = cur.next
                cur.next = prev
                prev = cur
                cur = holder
            else:
                if i == n and counter % 2 == 1:
                    cur = cur.next
                if prev.val == cur.val:
                    prev = prev.next
                    cur = cur.next
                    if prev == None and cur == None:
                        return True
        return False



