class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def is_empty(self):
        return self._top is None

    def push(self, item):
        node = Node(item)
        node.next = self._top
        self._top = node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("стек пуст")
        node = self._top
        self._top = node.next
        self._size -= 1
        return node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("стек пуст")
        return self._top.data

    def size(self):
        return self._size


if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())   # True
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.size())       # 3
    print(s.peek())       # 3
    print(s.pop())        # 3
    print(s.pop())        # 2
    print(s.is_empty())   # False
