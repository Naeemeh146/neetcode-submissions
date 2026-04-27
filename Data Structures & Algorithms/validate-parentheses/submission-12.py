class Solution:
    def isValid(self, s: str) -> bool:
        result = True
        peer_dict = {')':'(',
                     '}':'{',
                     ']':'['}
        stack_open = []

        for item in s:
            if item in '({[':
                stack_open.append(item)
            else:
                if not stack_open or stack_open[-1] != peer_dict[item]:
                    return False
                stack_open.pop()
            
        return not stack_open
                    

        