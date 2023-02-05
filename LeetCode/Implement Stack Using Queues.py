class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        self.top_element = None

    def push(self, x: int) -> None:
        self.queue1.append(x)
        self.top_element = x

    def pop(self) -> int:
        while len(self.queue1) > 1:
            self.top_element = self.queue1.pop(0)
            self.queue2.append(self.top_element)
        popped = self.queue1.pop(0)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return popped

    def top(self) -> int:
        return self.top_element

    def empty(self) -> bool:
        return len(self.queue1) == 0