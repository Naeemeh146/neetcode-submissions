class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        visited = set()


        for item in nums:
            if item in visited:
                return True
            visited.add(item)

        return False