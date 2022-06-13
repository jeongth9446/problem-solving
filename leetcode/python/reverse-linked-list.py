# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        rev = ListNode(head.val, None)
        head = head.next
        while head:
            rev, rev.next, head = head, rev, head.next

        print(rev)
        return rev