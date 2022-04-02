class CustomQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def len(self):
        return self.stack1.__len__() + self.stack2.__len__();
    def is_empty(self):
        return self.stack1.__len__() == 0 and self.stack2.__len__() == 0
    def top(self):
        if(self.stack2.__len__() != 0):
            while(self.stack1.__len__() != 0):
               self.stack2.append(self.stack1.pop())
        x = self.stack2.pop()
        self.stack2.append(x)
        return x
    def enqueue(self, x):
        self.stack1.append(x)
    def dequeue(self):
        if(self.stack2.__len__() == 0):
            while(self.stack1.__len__() != 0):
               self.stack2.append(self.stack1.pop())
        x = self.stack2.pop()
        return x