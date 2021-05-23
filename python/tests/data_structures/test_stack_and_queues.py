from Data_Structures.stacks_and_queues.stacks_and_queues import Node,Stack,Queue

import pytest

# ------- Stack ------#
# Can successfully push onto a stack

def test_push(test_stack):
    assert test_stack.top.value == 5
    test_stack.push(3)
    assert test_stack.top.value == 3

# Can successfully push multiple values onto a stack

def test_push_multi(test_stack):
    test_stack.push(3)
    test_stack.push(1)
    assert test_stack.top.value == 1
    assert test_stack.top.next.value == 3

# Can successfully pop off the stack

def test_pop(test_stack):
    assert test_stack.top.value == 5
    assert test_stack.pop() == 5
    assert test_stack.top.value == 7

# Can successfully empty a stack after multiple pops

def test_pop_all(test_stack):
    test_stack.pop()
    test_stack.pop()
    test_stack.pop()
    assert test_stack.top == None

# Can successfully peek the next item on the stack

def test_peek(test_stack):
    assert test_stack.peek() == 5

# Can successfully instantiate an empty stack

def test_is_empty(test_stack):
    assert test_stack.isEmpty() == False

# Calling pop or peek on empty stack raises exception

def test_call_empty(test_stack):
    test_stack.pop()
    test_stack.pop()
    test_stack.pop()
    assert test_stack.pop() == 'Empty Stack'
    assert test_stack.peek() == 'Empty Stack'

# ------- Queue ------#

# Can successfully enqueue into a queue

def test_enqueue(test_queue):
    assert test_queue.front.value == 5
    test_queue.enqueue(3)
    assert test_queue.front.value == 3

# Can successfully enqueue multiple values into a queue

def test_enqueue_multi(test_queue):
    test_queue.enqueue(3)
    test_queue.enqueue(1)
    assert test_queue.front.value == 1

# Can successfully dequeue out of a queue the expected value

def test_dequeue(test_queue):
    assert test_queue.dequeue() == 5
    assert test_queue.front.value ==7

# Can successfully peek into a queue, seeing the expected value

def test_peek_q(test_queue):
    assert test_queue.peek() == 5
    assert test_queue.front.value == 5

# Can successfully empty a queue after multiple dequeues

def test_emptying(test_queue):
    test_queue.dequeue()
    test_queue.dequeue()
    test_queue.dequeue()
    assert test_queue.isEmpty() == True

# Can successfully instantiate an empty queue

def test_is_empty_Q(test_queue):
    assert test_queue.isEmpty() == False

# Calling dequeue or peek on empty queue raises exception

def test_emptying_exception(test_queue):
    test_queue.dequeue()
    test_queue.dequeue()
    test_queue.dequeue()
    assert test_queue.peek() == 'Empty Queue'
    assert test_queue.dequeue() == 'Empty Queue'


@pytest.fixture
def test_stack():
        s=Stack()
        s.push(9)
        s.push(7)
        s.push(5)
        return s

@pytest.fixture
def test_queue():
        q=Queue()
        q.enqueue(9)
        q.enqueue(7)
        q.enqueue(5)
        return q
