# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        visited  = []
        if not root:
            return 


        
        if root.left or root.right:
            if not root in visited:
                tmp_r = root.right
                tmp_l = root.left
                root.left = tmp_r
                root.right = tmp_l
                
                visited.append(root)


        self.invertTree(root.left)
        self.invertTree(root.right)


        return root


