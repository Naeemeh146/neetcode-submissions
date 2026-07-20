class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        if len(nums) == 0:
            return nums
        
        n = len(nums)
        for i in range(n):
            nums.append(nums[i])


        return nums