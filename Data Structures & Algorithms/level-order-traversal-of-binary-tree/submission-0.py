# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        queue = deque()
        queue.append(root)
        list_return = [[root.val]]

        while queue:
            inside_list = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    inside_list.append(curr.left.val)
                if curr.right:
                    queue.append(curr.right)
                    inside_list.append(curr.right.val)
            if inside_list:
                list_return.append(inside_list)

        return list_return
        
        