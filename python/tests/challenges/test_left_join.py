
from Data_Structures.hashtable.hashtable import Hashtable
from code_challenges.left_join.left_join import left_join
import pytest

def test_left_join_1(hash_t1,hash_t2):
    assert left_join(hash_t1,hash_t2) == [['diligent', 'employed', 'idle'], ['wrath', 'anger', 'delight'], ['outift', 'garb', None], ['guide', 'usher', 'follow'], ['fond', 'enamored', 'averse']]

def test_left_join_2(hash_t1,hash_t3):
    assert left_join(hash_t1,hash_t3) == [['diligent', 'employed', 'idle'], ['wrath', 'anger', 'delight'], ['outift', 'garb', None], ['guide', 'usher', None], ['fond', 'enamored', None]]

def test_left_join_3(hash_t4,hash_t3):
    assert left_join(hash_t4,hash_t3) == [['fond', 'averse', None]]

@pytest.fixture
def hash_t1():
    test1 = Hashtable()
    test1.add('fond', 'enamored')
    test1.add('wrath', 'anger')
    test1.add('diligent', 'employed')
    test1.add('outift', 'garb')
    test1.add('guide', 'usher')

    return test1

@pytest.fixture
def hash_t2():
    test2 = Hashtable()
    test2.add('fond', 'averse')
    test2.add('wrath', 'delight')
    test2.add('diligent', 'idle')
    test2.add('guide', 'follow')
    test2.add('flow', 'jam')

    return test2

@pytest.fixture
def hash_t3():
    test3 = Hashtable()
    test3.add('wrath', 'delight')
    test3.add('diligent', 'idle')

    return test3

@pytest.fixture
def hash_t4():
    test4 = Hashtable()
    test4.add('fond', 'averse')

    return test4
