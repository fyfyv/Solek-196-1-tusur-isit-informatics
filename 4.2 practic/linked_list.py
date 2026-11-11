class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self._head = None

    def append(self, data):
        node = Node(data)
        if self._head is None:
            self._head = node
            return

        current = self._head
        while current.next is not None:
            current = current.next
        current.next = node

    def prepend(self, data):
        node = Node(data)
        node.next = self._head
        self._head = node

    def delete(self, data):
        if self._head is None:
            return

        if self._head.data == data:
            self._head = self._head.next
            return

        current = self._head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def to_list(self):
        result = []
        current = self._head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result


if __name__ == "__main__":
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.prepend(0)
    print(lst.to_list())   # [0, 1, 2]
    lst.delete(1)
    print(lst.to_list())   # [0, 2]
