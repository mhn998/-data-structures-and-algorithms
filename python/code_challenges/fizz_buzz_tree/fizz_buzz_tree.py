from Data_Structures.stacks_and_queues.stacks_and_queues import Queue
from Data_Structures.tree.tree import TNode ,  BinaryTree

def FizzBuzzTree(tree):
    new_tree = tree
    if new_tree.root is not None:

        def _func(node):
            if node.value%3==0 and node.value%5==0:
                node.value = 'FizzBuzz'
            elif node.value%3==0:
                node.value = 'Fizz'
            elif node.value%5==0:
                node.value = 'Buzz'
            elif node.value%3!=0 and node.value%5!=0:
                node.value = str(node.value)

            if node.left:
                _func(node.left)
            if node.right:
                _func(node.right)

        _func(new_tree.root)
        return new_tree
    else:
        new_tree.root =TNode('Empty Tree')
        return new_tree

if __name__ == "__main__":
    b_tree = BinaryTree()
    b_tree.root = TNode(2)
    b_tree.root.right = TNode(6)
    b_tree.root.left = TNode(7)
    b_tree.root.right.left = TNode(9)
    b_tree.root.right.right = TNode(15)
    b_tree.root.left.left = TNode(3)
    b_tree.root.left.right = TNode(8)
    print(FizzBuzzTree(b_tree).breadth_first())
