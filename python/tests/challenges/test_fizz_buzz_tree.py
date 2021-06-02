from Data_Structures.tree.tree import TNode ,  BinaryTree
from code_challenges.fizz_buzz_tree.fizz_buzz_tree import FizzBuzzTree
import pytest


def test_FizzBuzzTree_2(test_tree_added):
    assert FizzBuzzTree(test_tree_added).breadth_first() == ['2', '7', 'Fizz', 'Fizz', '8', 'Fizz', 'FizzBuzz']

@pytest.fixture
def test_tree_added():
    b_tree = BinaryTree()
    b_tree.root = TNode(2)
    b_tree.root.right = TNode(6)
    b_tree.root.left = TNode(7)
    b_tree.root.right.left = TNode(9)
    b_tree.root.right.right = TNode(15)
    b_tree.root.left.left = TNode(3)
    b_tree.root.left.right = TNode(8)
    return b_tree
