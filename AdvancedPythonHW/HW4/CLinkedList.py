class Node:
     
    # Constructor to create  a new node
    def __init__(self, data):
        self.data = data
        self.next = None
 
class CircularLinkedList:
     
    # Constructor to create a empty circular linked list
    def __init__(self):
        self.head = None
 
    # Function to insert a node at the beginning of a
    # circular linked list
    def push(self, data):
        ptr1 = Node(data)
        temp = self.head
         
        ptr1.next = self.head
 
        # If linked list is not None then set the next of
        # last node
        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = ptr1
 
        else:
            ptr1.next = ptr1 # For the first node
 
        self.head = ptr1       
def len(self: CircularLinkedList):
    if(self.head is None):
        return 0
    temp = self.head.next
    count = 1
    while temp is not self.head:
        count += 1
        temp = temp.next
    return count
list = CircularLinkedList()
print(len(list))
list.push(1)
print(len(list))
list.push(1)
list.push(3)
list.push(1)
list.push(1)
print(len(list))
list.push(1)
list.push(5)
print(len(list))
print(len(list))
