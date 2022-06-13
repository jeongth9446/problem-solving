# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n, m = 0, 0
        np, mp = 1, 1
        while l1:
            n += np * l1.val
            np *= 10
            l1 = l1.next

        while l2:
            m += mp * l2.val
            mp *= 10
            l2 = l2.next

        npm = n + m
        res = ListNode()
        p = res
        l = ' '
        while l != '':
            t = npm % 10
            l = str(npm)[:-1]
            if l != '':
                npm = int(l)
            p.val = t
            if (l != ''):
                p.next = ListNode()
                p = p.next

        return res
