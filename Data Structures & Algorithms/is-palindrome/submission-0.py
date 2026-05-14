class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:

            # Checking for not alphabetic-numeric chars from start
            while i < j and not s[i].isalnum():
                i = i + 1
            
            # Checking for not alphabetic-numeric chars from end
            while i < j and not s[j].isalnum():
                j = j - 1

            # make sure all lowercase
            if s[i].lower() != s[j].lower():
                return False

            i = i + 1
            j = j - 1


        return True