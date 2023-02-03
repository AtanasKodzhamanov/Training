# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = dummy
        curr = head

        while curr:
            if curr.val == val:
                curr = curr.next
                prev.next = curr
                continue
            prev.next = curr
            prev = prev.next
            curr = curr.next
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        curr = head

        while curr:
            if curr.val == val:
                while curr != None and curr.val == val:
                    curr = curr.next
            slow.next = curr
            slow = slow.next
            if curr != None:
                curr = curr.next
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        curr = head

        while curr:
            nxt = curr.next
            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr

            curr = nxt

        return dummy.next
