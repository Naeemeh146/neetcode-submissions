class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.difference = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            
            self.difference = max(self.difference, abs(left - right))

            return 1 + max(left , right)

        dfs(root)

        if self.difference > 1:
            return False

        return True