class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"{self.data}"


class StackIterator:  # Реализация протокола итерации.
    def __init__(self, top_node):
        self.current = top_node

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        result = self.current.data
        self.current = self.current.next
        return result


class Stack:
    def __init__(self):  # Инициализация стека.
        self._top_node = None
        self._size = 0

    def push(self, item):  # Добавление элемента в верхнюю часть стека.
        new_node = Node(data=item, next=self._top_node)
        self._top_node = new_node
        self._size += 1

    def pop(self):  # Удаления и возврат верхнего элемента стека.
        if self._top_node is not None:
            head = self._top_node
            self._top_node = self._top_node.next
            head.next = None
            self._size -= 1
            return head.data
        else:
            return None

    def peek(self):  # Возврата верхнего элемента без его удаления.
        if self._size > 0:
            return self._top_node.data
        else:
            return None

    def is_empty(self) -> bool:  # Проверка пустоты стека.
        if self._top_node is None:
            return True
        return False

    def size(self) -> int:  # Возврат размера стека.
        if self._size > 0:
            return self._size
        else:
            return 0

    def display(self):  # Вывод стека от начала до конца.
        if self._top_node is None:
            return None
        current = self._top_node
        for _ in range(self._size):
            print(current.data, end=" | ")
            current = current.next
        print()

    def __iter__(self):
        return StackIterator(self._top_node)


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    for i in range(5):
        stack.push(i)
    last_item = stack.peek()
    print(last_item)
    for object in stack:
        print(object)
    stack.display()
    print(stack.size())
    print(stack.is_empty())
    for _ in range(5):
        item = stack.pop()
        print(item)
    stack.display()
    print(stack.size())
