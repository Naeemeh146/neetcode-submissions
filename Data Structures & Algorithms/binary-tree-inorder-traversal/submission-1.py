class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list_visited = []
        if not root:
            return list_visited

        list_visited.extend(self.inorderTraversal(root.left))
        list_visited.append(root.val)
        list_visited.extend(self.inorderTraversal(root.right))

        return list_visited