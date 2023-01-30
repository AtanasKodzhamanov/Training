# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        answer = []
        stack.append(root)
        while stack:
            current_node = stack.pop()
            if current_node:
                answer.append(current_node.val)
                stack.append(current_node.right)
                stack.append(current_node.left)
        return answer
