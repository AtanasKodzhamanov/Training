# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()
        cur = head

        while cur and cur.next != None:

            if cur.next in hashset:
                return True
            hashset.add(cur.next)
            cur = cur.next
        return False
