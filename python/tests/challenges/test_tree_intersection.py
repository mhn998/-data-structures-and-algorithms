from Data_Structures.tree.tree import TNode , BinarySearchTree , BinaryTree
from code_challenges.tree_intersection.tree_intersection import tree_intersection
import pytest

def test_tree_intersection_1(tree1,tree2):
    assert tree_intersection(tree1,tree2) == [100, 160, 125, 175, 200, 350, 500]

def test_tree_intersection_2(tree1,tree3):
    assert tree_intersection(tree1,tree3) == 'Empty Tree 2'

def test_tree_intersection_3(tree1,tree4):
    assert tree_intersection(tree1,tree4) == 'No common values found'


@pytest.fixture
def tree1():
    bt = BinaryTree()
    bt.root = TNode(150)
    bt.root.left = TNode(100)
    bt.root.right = TNode(250)

    bt.root.left.left = TNode(75)
    bt.root.left.right = TNode(160)

    bt.root.left.right.left = TNode(125)
    bt.root.left.right.right = TNode(175)

    bt.root.right.left = TNode(200)
    bt.root.right.right = TNode(350)

    bt.root.right.right.right = TNode(500)
    bt.root.right.right.left = TNode(300)

    return bt

@pytest.fixture
def tree2():
    bt2 = BinaryTree()
    bt2.root = TNode(42)
    bt2.root.left = TNode(100)
    bt2.root.right = TNode(600)

    bt2.root.left.left = TNode(15)
    bt2.root.left.right = TNode(160)

    bt2.root.left.right.left = TNode(125)
    bt2.root.left.right.right = TNode(175)

    bt2.root.right.left = TNode(200)
    bt2.root.right.right = TNode(350)

    bt2.root.right.right.left = TNode(4)
    bt2.root.right.right.right = TNode(500)

    return bt2

@pytest.fixture
def tree3():
    bt3 = BinaryTree()

    return bt3

@pytest.fixture
def tree4():
    bt4 = BinaryTree()
    bt4.root = TNode(4)
    bt4.root.right = TNode(25)

    return bt4
