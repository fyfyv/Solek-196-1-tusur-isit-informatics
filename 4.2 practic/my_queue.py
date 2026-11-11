class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._head is None

    def enqueue(self, item):
        node = Node(item)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("очередь пуста")
        node = self._head
        self._head = node.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return node.data

    def front(self):
        if self.is_empty():
            raise IndexError("очередь пуста")
        return self._head.data

    def size(self):
        return self._size


if __name__ == "__main__":
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    print(q.front())    # a
    print(q.dequeue())  # a
    print(q.dequeue())  # b
    print(q.size())     # 1
