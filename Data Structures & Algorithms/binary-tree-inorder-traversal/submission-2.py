class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    
        result = []
        stack = []

        cur = root


        while cur or stack:

            # add all the way left 
            while cur:
                stack.append(cur)
                cur = cur.left

            # visit the left most
            cur = stack.pop()
            result.append(cur.val)


            # go to right
            cur = cur.right


        return result