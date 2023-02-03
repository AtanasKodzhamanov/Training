# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashset = set()
        cur = head
        while cur and cur.next != None:
            if cur in hashset:
                return cur
            else:
                hashset.add(cur)
            cur = cur.next
        return None
