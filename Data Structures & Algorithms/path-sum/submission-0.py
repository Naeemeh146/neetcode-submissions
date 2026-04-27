# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root, 0, targetSum)

    def dfs(self, root, sum_track, targetSum):
        if not root:
            return False
        
        sum_track = sum_track + root.val

        if not root.left and not root.right:
            if sum_track == targetSum:
                return True

        result = self.dfs(root.left, sum_track, targetSum) or self.dfs(root.right, sum_track, targetSum)       

        return result   
        