# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = nxt = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        curr = reversed = prev
        mx = curr.val
        while curr and curr.next:
            if curr.next.val < mx:
                curr.next = curr.next.next
            else:
                mx = curr.next.val
                curr = curr.next
        prev = None
        curr = nxt = reversed
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
