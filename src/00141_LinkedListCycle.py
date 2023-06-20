# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        first = head
        second = head

        while (first is not None):
            first = first.next
            if second is not None:
                second = second.next

            if second is not None:
                second = second.next
            else:
                return False

            if first == second:
                return True

        return False