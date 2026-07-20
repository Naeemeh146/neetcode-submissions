class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = strs[0]

        for item in strs[1:]:
            i = 0

            while i < len(prefix) and i < len(item) and prefix[i] == item[i]:

                i += 1
            
            prefix = prefix[:i]

        return prefix


