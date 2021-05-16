from Data_Structures.linked_list.linked_list import Linked_list, Node

import pytest

#test instantiation

def test_instantiation():
    obj = Linked_list()
    assert isinstance(obj, Linked_list)

# test head properly point to the first node in the linkedlist

def test_insert(list_test):
    assert list_test.head.data == 7
    assert list_test.head.next.data  == 5

# test includes on True and False

def test_includes(list_test):
    assert list_test.includes(7) == True
    assert list_test.includes(10) == False

# test __str__ for returning all values in linkedlist

def test_linked_values(list_test):
    assert str(list_test) == f' {{7}} ->  {{5}} ->  {{2}} -> Null'


@pytest.fixture
def list_test():
        linked=Linked_list()
        linked.insert(7)
        linked.insert(5)
        linked.insert(2)
        return linked
