class HashSet:
    def __init__(self, size=10):
        self.size = size
        self._buckets = [[] for _ in range(size)]
        self._count = 0

    def _hash(self, value):
        return hash(value) % self.size

    def add(self, value):
        bucket = self._buckets[self._hash(value)]
        if value not in bucket:
            bucket.append(value)
            self._count += 1

    def remove(self, value):
        bucket = self._buckets[self._hash(value)]
        if value in bucket:
            bucket.remove(value)
            self._count -= 1

    def contains(self, value):
        return value in self._buckets[self._hash(value)]

    def __len__(self):
        return self._count


if __name__ == "__main__":
    s = HashSet()
    s.add(1)
    s.add(2)
    s.add(2)
    print(len(s))          # 2
    print(s.contains(2))   # True
    s.remove(1)
    print(s.contains(1))   # False
