class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []
        subset = []

        def dfs(i):

            if len(subset) == k:
                result.append(subset.copy())
                return

            if i > n:
                return

            # include i
            subset.append(i)
            dfs(i+1)
            subset.pop()


            # exclude i
            dfs(i+1)

        
        dfs(1)

        return result


        