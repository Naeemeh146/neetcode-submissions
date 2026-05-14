class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dict = {}

        t_dict = {}

        for char in s:
            if char not in s_dict:
                s_dict[char] = 1

            s_dict[char] += 1     


        for char in t:
            if char not in t_dict:
                t_dict[char] = 1

            t_dict[char] += 1  

        if len(s_dict.keys()) != len(t_dict.keys()):

            return False

        if s_dict.keys() != t_dict.keys():
            return False

        for item in s_dict.keys():
            if s_dict[item] != t_dict[item]:
                return False

        return True