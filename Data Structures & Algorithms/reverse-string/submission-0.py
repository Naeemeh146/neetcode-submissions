class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        i = 0

        j = len(s) - 1

        while i < j:
            end = s[j]
            start =  s[i]
            s[i] = end
            s[j] = start

            i +=1
            j -=1

        return
        