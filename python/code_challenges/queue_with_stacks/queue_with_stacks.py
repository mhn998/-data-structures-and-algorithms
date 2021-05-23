class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    def push(self, value):
        new_node = Node(value)
        if self.top:
            new_node.next = self.top
        self.top = new_node

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

    def peek(self):
        try:
            if self.top is not None:
                return self.top.value
            else:
                raise Exception("Empty Stack")
        except:
            return "Empty Stack"

    def isEmpty(self):
        return self.top is None


    def __str__(self):
        return f"{self.top}"

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

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

    def peek(self):
        check = self.front is None
        try:
            if check is True:
                raise Exception("Empty Queue")
            else:
                return self.front.value
        except:
            return "Empty Queue"

    def isEmpty(self):
        return self.front == None


class PseudoQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self,value):
        self.s1.push(value)

    def dequeue(self):
        if self.s2.top is None:
            if self.s1.top is None:
                return "Empty Queue"

            while self.s1.top:
                s1_top = self.s1.pop()
                self.s2.push(s1_top)

            result = self.s2.pop()
            node = self.s2
            self.s2 = Stack()

            while node.top:
                node_top = node.pop()
                self.s1.push(node_top)

            return result
