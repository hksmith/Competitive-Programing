class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                y = stack.pop()
                x = stack.pop()
                if token == "+":
                    stack.append(x + y)
                elif token == "-":
                    stack.append(x - y)
                elif token == "*":
                    stack.append(x * y)
                else:
                    stack.append(int(float(x) / float(y)) if x * y >= 0 else -int(float(abs(x)) / float(abs(y))))
            else:
                stack.append(int(token))
        return stack[-1]