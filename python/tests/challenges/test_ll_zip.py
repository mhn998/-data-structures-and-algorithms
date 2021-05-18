import pytest
from Data_Structures.linked_list.linked_list import Linked_list
from code_challenges.ll_zip.ll_zip import zipLists

def test_ll_zip_1(list_test_1,list_test_2):
    assert str(zipLists(list_test_1,list_test_2)) == ' {1} ->  {5} ->  {3} ->  {9} -> Null'

@pytest.fixture
def list_test_1():
    ll1=Linked_list()
    ll1.append(1)
    ll1.append(3)

    return ll1

@pytest.fixture
def list_test_2():
    ll2=Linked_list()
    ll2.append(5)
    ll2.append(9)

    return ll2
