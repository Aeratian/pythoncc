from CustomStack import CustomQueue


class Stack:
    queue = CustomQueue()
def len(self):
    return self.queue.len()
def push(self, x):
    self.queue.enqueue(x)
def pop(self):
    for i in range(0, self.queue.len()-1):
        self.queue.enqueue(self.queue.dequeue())
    return self.queue.dequeue()
def top(self):
    for i in range(0, self.queue.len()-1):
        self.queue.enqueue(self.queue.dequeue())
    x = self.queue.dequeue()
    self.queue.enqueue(x)
    return x
stack = Stack()
stack.push(1)
print(stack.top())
stack.push(2)
print(stack.top())
stack.push(3)
print(stack.top())
stack.push(5)
print(stack.top())
stack.pop()
print(stack.top())
stack.pop()
print(stack.top())
stack.pop()
print(stack.top())