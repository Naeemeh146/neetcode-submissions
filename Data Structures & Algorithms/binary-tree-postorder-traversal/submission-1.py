class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        stack = []
        curr = root

        while curr or stack:

            while curr:
                result.append(curr.val)
                stack.append(curr)
                curr = curr.right

            curr = stack.pop()

            curr = curr.left


        return result[::-1]