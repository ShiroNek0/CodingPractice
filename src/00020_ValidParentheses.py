from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        last = ''
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
                continue
            if len(stack) == 0:
                return False
            
            last = stack.pop()
            if s[i] == ')' and last == '(':
                continue
            if s[i] == '}' and last == '{':
                continue
            if s[i] == ']' and last == '[':
                continue
            
            return False

        if len(stack) > 0:
            return False

        return True