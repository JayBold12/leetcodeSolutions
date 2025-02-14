class Solution:
    def isValid(self, s: str) -> bool:
        hm = {'}': '{', ')': '(', ']':'['}
        stack = []
        for char in s:
            if char not in hm:
                stack.append(char)
            else:
                if stack and stack[-1] != hm[char] or len(stack) == 0:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
