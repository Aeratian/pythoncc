from typing import Any


class CustomQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self, x):
        self.stack1.append(x)
    def dequeue(self):
        for i in range(0, self.stack1.__len__()):
            self.stack2.append(self.stack1.pop())
        x = self.stack2.pop()
        for i in range(0, self.stack2.__len__()):
            self.stack1.append(self.stack2.pop())
        return x
    def __str__(self) -> str:
        return self.stack1.__str__()



