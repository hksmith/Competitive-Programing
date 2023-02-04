class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == ')' and stack[-1] != '(':
                    return False
                if char == ']' and stack[-1] != '[':
                    return False
                if char == '}' and stack[-1] != '{':
                    return False
                stack.pop()
        return not stack


# Here is more in Enhanced Soln


# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         mapping = {')': '(', '}': '{', ']': '['}
        
#         for char in s:
#             if char in mapping:
#                 if not stack or stack.pop() != mapping[char]:
#                     return False
#             else:
#                 stack.append(char)
        
#         return not stack