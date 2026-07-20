from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        depth = 0

        queue = deque([root])

        while queue:
            depth +=1
            # look all the nodes in each level and append childrens
            for _ in range(len(queue)):
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

        return depth

