def len():
    return stack1.len() + stack2.len()
def is_empty():
    return stack1.is_empty() and stack2.is_empty()
def top():
    if(stack2.is_empty()):
        while(stack1.is_empty() is False):
            stack2.push(stack1.pop())
    x = stack2.top()
    return x
def enqueue(x):
    stack1.push(x)
def dequeue():
    if(stack2.is_empty):
        while(stack1.is_empty() is False):
            stack2.push(stack1.pop())
    x = stack2.pop()
    return x