from Data_Structures.hashtable.hashtable import *
import pytest

def test_hash(hashtable):
    assert hashtable._buckets[hashtable._hash('age')].head.value == '23'
    assert hashtable._hash('delicious') == 221


def test_add(hashtable):
    hashtable.add('why','so serious')
    assert hashtable._buckets[hashtable._hash('why')].head.value == 'so serious'

def test_contains(hashtable):
    assert hashtable.contains('age') == True
    assert hashtable.contains('reason') == False

def test_get(hashtable):
    assert hashtable.get('age') == '23'

def test_collision(hashtable):
    assert hashtable._buckets[hashtable._hash('there')].head.value == 127
    assert hashtable._buckets[hashtable._hash('there')].head.next.value == 95
    assert hashtable.get('there') == 127

@pytest.fixture
def hashtable():
    test_hash = Hashtable()
    test_hash.add('age', '23')
    test_hash.add('there', 95)
    test_hash.add('there', 127)
    return test_hash
