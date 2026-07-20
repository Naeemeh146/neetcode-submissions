class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        subset_tmp = []

        def dfs(i):

            # Base condition
            if i == len(nums):
                result.append(subset_tmp.copy())
                return

            #include
            subset_tmp.append(nums[i])
            dfs(i+1)
            
            #exclude
            subset_tmp.pop()
            dfs(i+1)
        
        dfs(0)

        return result