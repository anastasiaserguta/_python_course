from queue import Queue

import pytest


class TestQueue:
    def test_enqueue_in_empty_queue(self):
        queue = Queue()
        assert queue.front() == None

    def test_enqueue_in_queue_with_data(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.front() == 1
        assert queue.size() == 2

    def test_dequeue_in_empty_queue(self):
        queue = Queue()
        assert queue.dequeue() == None

    def test_dequeue_from_queue_with_data(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.size() == 2
        assert queue.dequeue() == 1
        assert queue.size() == 1
        assert queue.dequeue() == 2
        assert queue.size() == 0

    def test_front_empty_queue(self):
        queue = Queue()
        assert queue.front() == None

    def test_front_from_queue_with_data(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.front() == 1
        assert queue.size() == 2

    def test_is_empty_empty_queue(self):
        queue = Queue()
        assert queue.is_empty() == True

    def test_is_empty_queue_with_data(self):
        queue = Queue()
        queue.enqueue(1)
        assert queue.is_empty() == False

    def test_size_empty_queue(self):
        queue = Queue()
        assert queue.size() == 0

    def test_size_queue_with_data(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.size() == 2

    def test_display_empty_queue(self):
        queue = Queue()
        assert queue.display() == None

    def test_display_queue_with_data(self, capsys):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.display()
        captured = capsys.readouterr()
        assert "1 | 2 |" in captured.out

    def test_iterator_empty_queue(self):
        queue = Queue()
        iterator = iter(queue)
        with pytest.raises(StopIteration):
            next(iterator)

    def test_iterator_queue_with_data(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        iterator = iter(queue)
        assert next(iterator) == 1
        assert next(iterator) == 2
        assert next(iterator) == 3
        assert next(iterator) == 4

        with pytest.raises(StopIteration):
            next(iterator)
