# Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
#  Create a Stack class that has a top property. It creates an empty Stack when instantiated.
class Stack:
    def __init__(self):
        self.top = None # This object should be aware of a default empty value assigned to top when the stack is created.

    # Define a method called push which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
    def push(self, value):
        new_node = Node(value)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    # Define a method called pop that does not take any argument, removes the node from the top of the stack, and returns the node’s value. Should raise exception when called on empty stack
    def pop(self):
        try:
            if self.top is not None:
                node = self.top
                self.top = self.top.next
                return node.value
            else:
                raise Exception("Empty Stack")
        except:
            return "Empty Stack"
    # Define a method called peek that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack. Should raise exception when called on empty stack
    def peek(self):
        try:
            if self.top is not None:
                return self.top.value
            else:
                raise Exception("Empty Stack")
        except:
            return "Empty Stack"
    # Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the stack is empty.
    def isEmpty(self):
        return self.top is None


    def __str__(self):
        return f"{self.top}"

    # Create a Queue class that has a front property. It creates an empty Queue when instantiated.
class Queue:
    def __init__(self):
        self.front = None
        self.rear= None #This object should be aware of a default empty value assigned to front when the queue is created.
        # Define a method called enqueue which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.

    def enqueue(self,value):
        new_node = Node(value)
        if self.front is None:
            self.front= new_node
            self.rear = new_node
        self.rear.next = new_node
        self.rear = self.rear.next

    def dequeue(self):
        try:
            if self.front is not None:
                node = self.front
                self.front = self.front.next
                return node.value
            else:
                raise Exception("Empty Queue")
        except:
            return "Empty Queue"

        #Define a method called peek that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue. Should raise exception when called on empty queue

    def peek(self):
        check = self.front is None
        try:
            if check is True:
                raise Exception("Empty queue")
            else:
                return self.front.value
        except:
            return "Empty Queue"

    def isEmpty(self):
        return self.front == None # is None is more pythonic way

# s = Stack()
# print(s.isEmpty())

# s.pop()
# s.push(1)
# s.push(33)
# # print(s.top.value)
# s.pop()
# print(s.top.value)
# s.push(44)
# print(s.peek())
# print(s.isEmpty())
# # print(repr(s))
