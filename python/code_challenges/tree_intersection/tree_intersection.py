

from Data_Structures.tree.tree import TNode , BinarySearchTree , BinaryTree

def tree_intersection(tree1,tree2):
    if tree1.root is None:
        return 'Empty Tree 1'

    if tree2.root is None:
        return 'Empty Tree 2'

    arr_of_tree1 = tree1.preOrder() # traverse tree1 using preorder method which returns an array
    arr_of_tree2 = tree2.preOrder() # traverse tree2 using preorder method which returns an array
    common_values = []
    for i in arr_of_tree1:
        if i in arr_of_tree2:
            common_values.append(i)
    if len(common_values) > 0:
        return common_values
    else:
        return 'No common values found'



if __name__ == '__main__':
    pass

