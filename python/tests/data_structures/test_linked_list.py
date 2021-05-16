from Data_Structures.linked_list.linked_list import Linked_list, Node

import pytest

#test instantiation

def test_instantiation():
    obj = Linked_list()
    assert isinstance(obj, Linked_list)

# test head properly point to the first node in the linkedlist

def test_insert(list_test):
    assert list_test.head.value == 7
    assert list_test.head.next.value  == 5

# test includes on True and False

def test_includes(list_test):
    assert list_test.includes(7) == True
    assert list_test.includes(10) == False


# test __str__ for returning all values in linkedlist

def test_linked_values(list_test):
    assert str(list_test) == f' {{7}} ->  {{5}} ->  {{2}} -> Null'



# Can successfully add a node to the end of the linked list

def test_linked_append(list_test):
    list_test.append(0)
    assert str(list_test) == f' {{7}} ->  {{5}} ->  {{2}} ->  {{0}} -> Null'

# Can successfully add multiple nodes to the end of a linked list

def test_linked_multiple_append(list_test):
    list_test.append(8)
    list_test.append(11)
    list_test.append(9)
    assert str(list_test) == f' {{7}} ->  {{5}} ->  {{2}} ->  {{8}} ->  {{11}} ->  {{9}} -> Null'

# Can successfully insert a node before a node located in the middle of a linked list

def test_linked_insert_before(list_test):
    list_test.insertBefore(5,1)
    assert str(list_test) == f' {{7}} ->  {{1}} ->  {{5}} ->  {{2}} -> Null'

# Can successfully insert a node before the first node of a linked list

def test_linked_insert_before_first(list_test):
    list_test.insertBefore(7,1)
    assert str(list_test) == f' {{1}} ->  {{7}} ->  {{5}} ->  {{2}} -> Null'

# Can successfully insert after a node in the middle of the linked list

def test_linked_insert_after(list_test):
    list_test.insertAfter(5,3)
    assert str(list_test) == f' {{7}} ->  {{5}} ->  {{3}} ->  {{2}} -> Null'

# Can successfully insert a node after the last node of the linked list

def test_linked_insert_after_last(list_test):
    list_test.insertAfter(2,4)
    assert str(list_test) == f' {{7}} ->  {{5}} ->  {{2}} ->  {{4}} -> Null'

@pytest.fixture
def list_test():
        linked=Linked_list()
        linked.insert(7)
        linked.insert(5)
        linked.insert(2)
        return linked




