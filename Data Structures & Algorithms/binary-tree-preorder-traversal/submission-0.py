# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        visited_node = []

        if not root:
            return visited_node

        visited_node.append(root.val)
        visited_node.extend(self.preorderTraversal(root.left))
        visited_node.extend(self.preorderTraversal(root.right))

        return visited_node

        