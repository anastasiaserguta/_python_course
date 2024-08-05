import pytest
from linked_list import LinkedList


class TestLinked_list:
    def test_get_item_empty_linked_list(self):
        linked_list = LinkedList()
        assert linked_list[1] == None

    def test_get_item_not_empty_linked_list(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.prepend(3)
        linked_list.prepend(4)
        assert linked_list[0] == 4
        assert linked_list[1] == 3
        assert linked_list[2] == 1
        assert linked_list[3] == 2

    def test_prepend_data_linked_list(self):
        linked_list = LinkedList()
        linked_list.prepend(1)
        linked_list.prepend(2)
        assert linked_list[1] == 1
        assert linked_list._size == 2

    def test_append_data_linked_list(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        assert linked_list[1] == 2
        assert linked_list._size == 2

    def test_insert_data_linked_list_not_empty(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.insert(3, 1)
        assert linked_list[1] == 3
        assert linked_list._size == 3

    def test_insert_data_empty_linked_list(self):
        linked_list = LinkedList()
        assert linked_list.insert(3, 1) == None

    def test_delete_data_empty_linked_list(self):
        linked_list = LinkedList()
        assert linked_list.delete(3) == None

    def test_delete_data_not_empty_linked_list(self, capsys):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.display()
        captured = capsys.readouterr()
        assert "1 | 2 | 3 | 2 |" in captured.out
        assert linked_list._size == 4
        linked_list.delete(2)
        linked_list.display()
        captured = capsys.readouterr()
        assert "1 | 3 | 2 |" in captured.out
        assert linked_list._size == 3

    def test_find_data_linked_list(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        assert linked_list.find(5) == None
        assert linked_list.find(4) == 4

    def test_iterator_empty_linked_list(self):
        linked_list = LinkedList()
        iterator = iter(linked_list)
        with pytest.raises(StopIteration):
            next(iterator)

    def test_iterator_linked_list_with_data(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        linked_list.prepend(5)
        iterator = iter(linked_list)
        assert next(iterator) == 5
        assert next(iterator) == 1
        assert next(iterator) == 2
        assert next(iterator) == 3
        assert next(iterator) == 4

        with pytest.raises(StopIteration):
            next(iterator)
