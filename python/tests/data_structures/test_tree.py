from Data_Structures.tree.tree import Node,BinarySearchTree,BinaryTree
import pytest

# Can successfully instantiate an empty tree
def test_empty_tree():
    new_tree = BinarySearchTree()
    assert new_tree.root == None

# Can successfully instantiate a tree with a single root node
def test_root_node(test_tree_empty):
    test_tree_empty.add(5)
    assert test_tree_empty.root.value == 5

# Can successfully add a left child and right child to a single root node
def test_left_right_node(test_tree_empty):
    test_tree_empty.add(7)
    test_tree_empty.add(3)
    test_tree_empty.add(9)
    assert test_tree_empty.root.left.value == 3
    assert test_tree_empty.root.right.value == 9
# Can successfully return a collection from a preorder traversal
def test_preOrder(test_tree_added):
    assert test_tree_added.preOrder() == [6, 4, 0, 8, 7, 10]

# Can successfully return a collection from an inorder traversal
def test_inOrder(test_tree_added):
    assert test_tree_added.inOrder() == [0, 4, 6, 7, 8, 10]

# Can successfully return a collection from a postorder traversal
def test_postOrder(test_tree_added):
    assert test_tree_added.postOrder() == [0, 4, 7, 10, 8, 6]

# Can successfully pick the maximum value in a tree
def test_find_maximum_value_1(test_tree_added):
    assert test_tree_added.find_maximum_value() == 10

# Can successfully traverse breadth-first

def test_breadth_1(test_tree_added):
    assert test_tree_added.breadth_first() == [6, 4, 8, 0, 7, 10]

def test_breadth_2():
    tree=BinarySearchTree()
    assert tree.breadth_first() == 'Empty Tree'


@pytest.fixture
def test_tree_empty():
    tree=BinarySearchTree()
    return tree

@pytest.fixture
def test_tree_added():
    tree=BinarySearchTree()
    tree.add(6)
    tree.add(8)
    tree.add(4)
    tree.add(10)
    tree.add(7)
    tree.add(0)
    return tree
