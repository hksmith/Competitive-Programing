class MinStack:
    def __init__(self):
        self.stack = []
        self.m_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.m_stack or x <= self.m_stack[-1]:
            self.m_stack.append(x)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.m_stack[-1]:
                self.m_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.m_stack[-1] if self.m_stack else None