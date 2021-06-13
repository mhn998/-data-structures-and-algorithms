from code_challenges.insertion_sort.insertion_sort import InsertionSort
import pytest


def test_inserton_sort():
    test = [5,10,4,2,8,19,11]
    assert InsertionSort(test) == [2, 4, 5, 8, 10, 11, 19]

