class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return f"{self.data}"


class LinkedListIterator:  # Реализация протокола итерации.
    def __init__(self, head_node):
        self.current = head_node

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        result = self.current.data
        self.current = self.current.next

        return result


class LinkedList:
    def __init__(self):
        self._head_node = None
        self._tail_node = None
        self._size = 0

    def prepend(self, item):  # Добавление в конец списка.
        new_node = Node(item)
        if self._size == 0:
            self._head_node = self._tail_node = new_node
        else:
            new_node.next = self._head_node
            self._head_node.prev = new_node
            self._head_node = new_node
        self._size += 1

    def append(self, item):  # Добавление в начало списка.
        new_node = Node(item)
        if self._size == 0:
            self._head_node = self._tail_node = new_node
        else:
            new_node.prev = self._tail_node
            self._tail_node.next = new_node
            self._tail_node = new_node

        self._size += 1

    def insert(self, item, index):  # Добавление элемента на позицию i.
        try:
            if index < 0 or index > self._size:
                raise IndexError
        except IndexError:
            return None
        if index == 0:
            self.prepend(item)
        elif index == self._size:
            self.append(item)
        else:
            new_node = Node(item)
            current = self._head_node
            for _ in range(index - 1):
                current = current.next
            new_node.prev = current
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
            self._size += 1

    def delete(self, item):  # Удаление первого вхождения элемента.
        current = self._head_node
        previous = None
        while current.data != item and current.next:
            previous = current
            current = current.next
        if current.data == item:
            if previous:
                previous.next = current.next
            else:
                self._head_node = current.next
        self._size -= 1

    def find(self, item):  # Возврат узла с элементом либо None, если элемент не найден.
        current = self._head_node
        index = 1
        flag = False

        if self._head_node is None:
            return None

        while current:
            if current.data == item:
                flag = True
                break
            current = current.next
            index += 1

        if flag:
            return index
        else:
            return None

    def display(
        self, reverse=False
    ):  # Вывод списка от начала до конца, если reverse=False, или от конца до начала, если True.
        if self._head_node is None:
            print("List is empty.")
            return
        if reverse is not True:
            current = self._head_node
            while current:
                print(current.data, end=" | ")
                current = current.next
            print()
        else:
            current = self._tail_node
            while current:
                print(current.data, end=" | ")
                current = current.prev
            print()

    def __getitem__(self, index):  # Получение элемента списка на позиции i.
        try:
            if index < 0 or index >= self._size:
                raise IndexError
        except IndexError:
            return None
        current = self._head_node
        for _ in range(index):
            current = current.next
        return current.data

    def __iter__(self):  # Итерация по списку.
        return LinkedListIterator(self._head_node)


if __name__ == "__main__":
    linked_list = LinkedList()
    for i in range(5):
        linked_list.append(i)
    linked_list.display()
    print(f"Size: {linked_list._size}.")
    for j in range(10, 15):
        linked_list.prepend(j)
    linked_list.display()
    linked_list.display(reverse=True)
    print(f"Size: {linked_list._size}.")
    linked_list.insert(33, 5)
    linked_list.insert(55, 67)
    print(f"Size: {linked_list._size}.")
    linked_list.delete(3)
    linked_list.delete(0)
    print(f"Size: {linked_list._size}.")
    for object in linked_list:
        print(object)
    print(linked_list.find(33))
    print(linked_list.find(9))
    linked_list.display()
    print(linked_list[6])
    print(linked_list[20])
