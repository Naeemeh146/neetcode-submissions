# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        visited_list = []
        stack = []

        if not root:
            return visited_list

        stack.append(root)

        while stack:
            node = stack.pop()
            visited_list.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)
        

        return visited_list
        
        
        



        