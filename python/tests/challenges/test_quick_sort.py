from code_challenges.quick_sort.quick_sort import *
import pytest

def test_quick_sort_1(test_list1):
    quick_sort(test_list1,0,len(test_list1)-1)
    assert test_list1 == [-2, 5, 8, 12, 18, 20]

def test_quick_sort_2(test_list2):
    quick_sort(test_list2,0,len(test_list2)-1)
    assert test_list2 == [5, 5, 5, 7, 7, 12]

def test_quick_sort_3(test_list3):
    quick_sort(test_list3,0,len(test_list3)-1)
    assert test_list3 == [2, 3, 5, 7, 11, 13]

# Reverse-sorted
@pytest.fixture
def test_list1():
    test = [20,18,12,8,5,-2]
    return test

# Few uniques
@pytest.fixture
def test_list2():
    test = [5,12,7,5,5,7]
    return test

# Nearly-sorted
@pytest.fixture
def test_list3():
    test = [2,3,5,7,13,11]
    return test
