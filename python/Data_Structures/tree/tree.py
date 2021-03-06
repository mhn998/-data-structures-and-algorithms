from Data_Structures.stacks_and_queues.stacks_and_queues import Queue
class TNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def preOrder(self):
        output=[]

        def _func(node):
            output.append(node.value)
            if node.left:
                _func(node.left)
            if node.right:
                _func(node.right)

        _func(self.root)
        return output

    def inOrder(self):
        output=[]

        def _func(node):
            if node.left:
                _func(node.left)
            output.append(node.value)
            if node.right:
                _func(node.right)

        _func(self.root)
        return output

    def postOrder(self):
        output=[]

        def _func(node):
            if node.left:
                _func(node.left)
            if node.right:
                _func(node.right)
            output.append(node.value)

        _func(self.root)
        return output

    def find_maximum_value(self):
        self.max=self.root.value

        def _func(node):
            if node.value > self.max:
                self.max =node.value
            if node.left:
                _func(node.left)
            if node.right:
                _func(node.right)

        _func(self.root)
        return self.max

    def breadth_first(self):
        if self.root:
            output=[]
            q = Queue()
            q.enqueue(self.root)

            while q.front != None:
                current = q.front.value

                if current.left:
                    q.enqueue(current.left)
                if current.right:
                    q.enqueue(current.right)

                output.append(current.value)
                q.dequeue()

            return output
        else:
            return 'Empty Tree'


class BinarySearchTree(BinaryTree):

    def add(self, value):
        if not self.root:
            self.root = TNode(value)
        else:
            def _func(node):
                if value < node.value:
                    if not node.left:
                        node.left = TNode(value)
                        return
                    else:
                        _func(node.left)
                else:
                    if not node.right:
                        node.right = TNode(value)
                        return
                    else:
                        _func(node.right)

            _func(self.root)

    def contains(self,value):
        if self.root:
            current = self.root
            def _func(current):
                if value == current.value:
                    return True
                elif value < current.value:
                    current = current.left
                    if current:
                        return _func(current)
                elif value > current.value:
                    current = current.right
                    if current:
                        return _func(current)

            if _func(current) == True:
                return True
            else:
                return False
        else:
            return False
