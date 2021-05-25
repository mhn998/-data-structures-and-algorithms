import pytest
from code_challenges.fifo_animal_shelter.fifo_animal_shelter import AnimalShelter,Cat,Dog

def test_Animal_Shelter(test_shelter):
    test_shelter.enqueue(Dog('puppy2'))
    assert str(test_shelter) == f'{{kitten1}}->{{puppy1}}->{{kitten2}}->{{puppy2}}->Null'

    assert test_shelter.dequeue('Dog') == 'puppy1'
    assert str(test_shelter) == f'{{kitten1}}->{{kitten2}}->{{puppy2}}->Null'

    assert test_shelter.dequeue('Bird') == 'Null'
    assert str(test_shelter) == f'{{kitten1}}->{{kitten2}}->{{puppy2}}->Null'

    assert test_shelter.dequeue('Cat') == 'kitten1'
    assert str(test_shelter) == f'{{kitten2}}->{{puppy2}}->Null'

    assert test_shelter.dequeue() == 'kitten2'
    assert str(test_shelter) == f'{{puppy2}}->Null'



@pytest.fixture
def test_shelter():
    shelter =AnimalShelter()
    shelter.enqueue(Cat('kitten1'))
    shelter.enqueue(Dog('puppy1'))
    shelter.enqueue(Cat('kitten2'))

    return shelter
