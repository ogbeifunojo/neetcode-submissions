class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ')' : '(',
            '}' : '{',
            ']' : '['
         }
        stack = []
        for brackets in s:
            if brackets in close_to_open: #closing
                if not stack:
                    return False 
                last = stack.pop()
                if close_to_open[brackets] != last:
                    return False
            else: # opening
                stack.append(brackets)
        if stack:
            return False
        else:
            return True
