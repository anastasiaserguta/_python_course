import pytest
from stack import Stack


class TestStack:
    def test_push_to_empty(self):
        stack = Stack()
        stack.push(1)
        assert stack.peek() == 1
        assert stack.size() == 1

    def test_push_to_stack_with_data(self):
        stack = Stack()
        stack.push(2)
        stack.push(3)
        assert stack.peek() == 3
        assert stack.size() == 2

    def test_pop_from_empty_stack(self):
        stack = Stack()
        assert stack.pop() == None

    def test_pop_from_stack_one_data(self):
        stack = Stack()
        stack.push(1)
        assert stack.pop() == 1
        assert stack.pop() == None
        assert stack.size() == 0

    def test_pop_from_stack_with_data(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.peek() == 1
        assert stack.size() == 1

    def test_peek_empty_stack(self):
        stack = Stack()
        assert stack.peek() == None

    def test_peek_stack_with_data(self):
        stack = Stack()
        stack.push(1)
        assert stack.peek() == 1
        assert stack.size() == 1
        assert stack.peek() == 1
        assert stack.size() == 1

    def test_is_empty_empty_stack(self):
        stack = Stack()
        assert stack.is_empty() == True

    def test_is_empty_stack_with_data(self):
        stack = Stack()
        stack.push(1)
        assert stack.is_empty() == False

    def test_size_empty_stack(self):
        stack = Stack()
        assert stack.size() == 0

    def test_size_stack_with_data(self):
        stack = Stack()
        for i in range(5):
            stack.push(i)
        assert stack.size() == 5

    def test_iterator_empty_stack(self):
        stack = Stack()
        iterator = iter(stack)
        with pytest.raises(StopIteration):
            next(iterator)

    def test_iterator_stack_with_data(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        iterator = iter(stack)
        assert next(iterator) == 3
        assert next(iterator) == 2
        assert next(iterator) == 1

        with pytest.raises(StopIteration):
            next(iterator)
