# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            return head

        prevNode = None
        curr = head
        
        nextNode = head.next

        while(nextNode is not None):
            curr.next = prevNode
            prevNode = curr
            curr = nextNode
            nextNode = nextNode.next

        curr.next = prevNode
        return curr