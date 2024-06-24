class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f'{self.data}'

class Stack:
    all_data = []

    def __init__(self):
        self._top_node = None
        self._size = 0

    def push(self, item):
        new_node = Node(data=item, next=self._top_node)
        self._top_node = new_node
        self._size += 1
        Stack.all_data.append(self.__str__())

    def pop(self):
        head = self._top_node
        self._top_node = self._top_node.next
        head.next = None
        self._size -= 1
        return head

    def peek(self):
        return f'The last object - {self._top_node}.'

    def is_empty(self):
        if self._top_node is None:
            return 'Stack is empty.'
        return 'Stack has data.'

    def size(self):
        return f'The stack contains {self._size} objects.'

    def display(self):
        return Stack.all_data
    
    def __str__(self) -> str:
        return f'{self._top_node}'

if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    for i in range(5):
        stack.push(i)
    last_item = stack.peek()
    print(last_item)
    stack_size = stack.size()
    print(stack_size)
    print(stack.is_empty())
    for _ in range(5):
        item = stack.pop()
        print(item)
    print(*stack.display())
