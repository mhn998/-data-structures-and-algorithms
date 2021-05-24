import pytest
from code_challenges.queue_with_stacks.queue_with_stacks import Stack, Queue , PseudoQueue


def test_enqueue_and_dequeue(test_pseudoqueue):
    test_pseudoqueue.enqueue(6)
    assert test_pseudoqueue.dequeue() == 0
    assert test_pseudoqueue.dequeue() == 2
    assert test_pseudoqueue.dequeue() == 4
    assert test_pseudoqueue.dequeue() == 6
    assert test_pseudoqueue.dequeue() == "Empty Queue"


@pytest.fixture
def test_pseudoqueue():
        pq=PseudoQueue()
        pq.enqueue(0)
        pq.enqueue(2)
        pq.enqueue(4)
        return pq
