class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"{self.data}"


class QueueIterator:  # Реализация протокола итерации.
    def __init__(self, first_node):
        self.current = first_node

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        result = self.current.data
        self.current = self.current.next

        return result


class Queue:
    def __init__(self):
        self._first_node = None
        self._last_node = None
        self._size = 0

    def enqueue(self, item):  # Добавление элемента в конец очереди.
        new_data = Node(item)
        if self._first_node is None:
            self._first_node = new_data
            self._last_node = self._first_node
            self._size += 1
        else:
            self._last_node.next = new_data
            self._last_node = new_data
            self._size += 1

    def dequeue(self):  # Удаление и возврат элемента из начала очереди.
        data = self._first_node.data
        self._first_node = self._first_node.next
        if self._first_node is None:
            self._last_node = None
        self._size -= 1
        return data

    def front(self):  # Возврат элемента из начала очереди без его удаления.
        return self._first_node.data

    def is_empty(self) -> bool:  # Проверяет пустая ли очередь.
        if self._first_node is None:
            return True
        return False

    def size(self) -> int:  # Количество элементов в очереди.
        if self._size > 0:
            return self._size
        else:
            return 0

    def display(self):  # Вывод от начала до конца.
        if self._first_node is None:
            print("List is empty.")
            return
        current = self._first_node
        for _ in range(self._size):
            print(current.data, end=" | ")
            current = current.next
        print()

    def __iter__(self):  # Итерация по списку.
        return QueueIterator(self._first_node)


if __name__ == "__main__":
    queue = Queue()
    print(queue.is_empty())
    for i in range(5):
        queue.enqueue(i)
    first_item = queue.front()
    print(first_item)
    print(queue.size())
    print(queue.is_empty())
    queue.display()
    print(queue.dequeue())
    for elem in queue:
        print(elem)
    queue.display()
    print(queue.size())
