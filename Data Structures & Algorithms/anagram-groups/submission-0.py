from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # composite key
        dict_str = defaultdict(list)

        for item in strs:
            count = [0] * 26
            for char in item:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)
            dict_str[key].append(item)
        
        return list(dict_str.values())