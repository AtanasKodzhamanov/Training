class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # inorder - left, root, right
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        # Recursion

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            answer.append(node.val)
            dfs(node.right)

        dfs(root)
        return answer

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        return res

    # preorder - root, left, right
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        # Recursion

        def dfs(node):
            if not node:
                return
            answer.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return answer

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

    # postorder - left, right, root
    def postorderTraversal(root):
        result = []

        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                result.append(node.val)
        traverse(root)
        return result

    def postorderTraversal(root):
        if not root:
            return []

        stack = [root]
        result = []
        prev = None

        while stack:
            curr = stack[-1]
            if (not curr.left and not curr.right) or (prev and (prev == curr.left or prev == curr.right)):
                result.append(curr.val)
                prev = curr
                stack.pop()
            else:
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)

        return result

    # level order traversal / breadth-first search (BFS)
    # Visit all the nodes at each level of the tree from left to right, starting from the root and moving down the tree
