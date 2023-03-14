"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = []

        def dfs(node):
            if not node:
                return
            output.append(node.val)

            for c in node.children:
                dfs(c)

        dfs(root)

        return output


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return
        output = []
        q = deque([root])

        while q:
            cand = q.popleft()
            output.append(cand.val)
            for c in reversed(cand.children):
                q.appendleft(c)

        return output
